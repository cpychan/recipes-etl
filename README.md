# Recipes ETL Script
## Overview
This script performs an Extract, Transform, and Load (ETL) process on a dataset of recipes stored in a JSON file. It filters recipes containing any variation of the word "chilies" in their ingredients, determines the difficulty of each recipe based on its preparation and cooking times, and exports the filtered list with the difficulty level to a CSV file.

# Features
### Extract: 
Reads a JSON file line by line to accommodate large files.
### Transform:
Identifies recipes containing "chilies" or common misspellings in the ingredients.
Calculates the total preparation and cooking time to classify the difficulty of each recipe.
### Load: 
Outputs the filtered recipes with their difficulty level to a CSV file.

### Requirements
Python 3.11.5
No external third-party modules are required.
### Installation
Ensure you have Python 3.11.5 installed on your system. You can download it from the official Python website.

## How to Run
1. Place your recipes.json file in a directory named recipes-etl at the same location as the script.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python:  code.py


## Understanding the Code
- The script starts by defining the path to the JSON file containing the recipes.
- It then loads the data from the JSON file into a list of dictionaries.
- A regular expression is compiled to match the word "chilies" and its common misspellings in the ingredients list of each recipe.
- Recipes containing chilies are filtered and processed to determine their cooking difficulty based on the total time required for preparation and cooking.
- Finally, the filtered recipes, along with their difficulty levels, are exported to a CSV file in the specified directory.
Notes
- The script assumes the presence of a recipes-etl directory in the same location as the script itself.
- The JSON file should contain one recipe per line, each as a separate JSON object.
- For further assistance or to report bugs, please open an issue in the repository or contact the maintainer.

