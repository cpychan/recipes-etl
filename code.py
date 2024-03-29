import os
import json
import re
import csv

# Get the directory of the current script
file_path = "recipes.json"

# Load Data
data = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Parse each line as a JSON object and append to the list
        data.append(json.loads(line))

# check if data is loaded properly 
print(data[1])


# Task 1
# Compile a regular expression to include misspelling of the word
chilies_misspell = re.compile(r'\bchil(?:i|e|le|ies|is)?s?\b', re.IGNORECASE)

# Function to search for chilies in the ingredients of a recipe
def contains_chilies(ingredients):
    return any(chilies_misspell.search(ingredient) for ingredient in ingredients.split("\n"))

# Extract recipes that contain chilies or its variations
recipes_with_chilies = [recipe for recipe in data if contains_chilies(recipe['ingredients'])]

# Print or process the matching recipes
for recipe in recipes_with_chilies:
    print(recipe['name'])  # Print the name of each recipe that matches

# Task 2 Proceed with the extracted recipes from Task 1 
# Adjusted function to convert ISO 8601 duration to minutes
def duration_to_minutes(iso_duration):
    if not iso_duration:
        return 0  # Return 0 if the input is None or empty
    # Pattern to extract hours and minutes
    pattern = re.compile(r'PT(?:(\d+)H)?(?:(\d+)M)?')
    match = pattern.match(iso_duration)
    if not match:
        return 0  # Return 0 if there's no match
    hours, minutes = match.groups(default='0')
    return int(hours) * 60 + int(minutes)

# Function to determine the difficulty based on total time
def determine_difficulty(prep_time, cook_time):
    total_minutes = duration_to_minutes(prep_time) + duration_to_minutes(cook_time)
    if total_minutes > 60:
        return "Hard"
    elif 30 < total_minutes <= 60:
        return "Medium"
    elif total_minutes > 0 and total_minutes <= 30:
        return "Easy"
    else:
        return "Unknown"

# Add difficulty columns to each recipe
for recipe in recipes_with_chilies:
    recipe['difficulty'] = determine_difficulty(recipe.get('prepTime', 'PT0M'), recipe.get('cookTime', 'PT0M'))

# Print example output to check the result
for recipe in recipes_with_chilies:
    print(recipe['name'], "-", recipe['difficulty'])

# Covert output CSV file
output_file_path = 'recipes-with-difficulty.csv'

# Define the column headers for the CSV file
headers = ['name', 'ingredients', 'url', 'image', 'cookTime', 'prepTime', 'difficulty']

# Open the file in write mode and create a csv.writer object
with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)

    # Write the header row
    writer.writeheader()
    
    # Write recipe data
    for recipe in recipes_with_chilies:
        # Ensure only the fields defined in headers are written to the CSV
        row = {field: recipe.get(field, '') for field in headers}
        writer.writerow(row)

print(f'Recipes with difficulty exported to {output_file_path}')
