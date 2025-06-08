import json
import csv
import pandas as pd
import os

# Change the current working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def json_to_csv(json_file, output_file, json_type=None):
    """
    Converts a JSON file into a CSV file based on the structure and type.

    Parameters:
    json_file (str): Path to the JSON file.
    output_file (str): Path to save the CSV file.
    json_type (str): Type of JSON ('plants', 'zombies', 'flat', 'achievements'). Determines the structure.
    """
    try:
        # Load the JSON data
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Handle different JSON structures
        if json_type == 'plants':
            # Extract the 'plants' array
            records = data.get('plants', [])
            df = pd.DataFrame(records, columns=['seedType', 'name', 'introduce', 'info', 'cost'])
        elif json_type == 'zombies':
            # Extract the 'zombies' array
            records = data.get('zombies', [])
            df = pd.DataFrame(records, columns=['theZombieType', 'name', 'introduce', 'info'])
        elif json_type == 'flat':
            # Convert flat dictionary to DataFrame
            df = pd.DataFrame(list(data.items()), columns=['Key', 'Value'])
        elif json_type == 'achievements':
            # Handle achievements JSON structure
            headers = ["ID", "achievement", "Name", "Text"]
            rows = [
                {
                    "ID": key,
                    "achievement": value.get("achievement"),
                    "Name": value.get("Name"),
                    "Text": value.get("Text")
                }
                for key, value in data.items()
            ]
            df = pd.DataFrame(rows, columns=headers)
        else:
            raise ValueError("Invalid json_type. Must be 'plants', 'zombies', 'flat', or 'achievements'.")
        
        # Save DataFrame to CSV
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"CSV file created successfully at {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
if __name__ == "__main__":
    # Convert Achievements JSON to CSV
    json_to_csv('AchievementsTextTranslate.json', 'aoutput.csv', json_type='achievements')

    # Convert Plants JSON to CSV
    json_to_csv('LawnStringsTranslate.json', 'poutput.csv', json_type='plants')

    # Convert Zombies JSON to CSV
    json_to_csv('ZombieStringsTranslate.json', 'zoutput.csv', json_type='zombies')

    # Convert Translation Strings JSON (Flat) to CSV
    json_to_csv('translation_strings.json', 'soutput.csv', json_type='flat')

    # Convert Translation Regexes JSON (Flat) to CSV
    json_to_csv('translation_regexs.json', 'routput.csv', json_type='flat')