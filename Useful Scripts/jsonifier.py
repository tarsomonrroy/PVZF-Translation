import pandas as pd
import json
import os

# Change the current working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Now all relative paths will be relative to this script's location

def excel_to_json(input_file, output_file, sheet_name, data_type):
    """
    Converts an Excel sheet to a JSON file based on the specified data type.

    Parameters:
    input_file (str): Path to the Excel file.
    output_file (str): Path to save the JSON file.
    sheet_name (str): Name of the sheet to process.
    data_type (str): Type of JSON structure ('plants', 'zombies', 'dictionary', 'achievements').
    """
    try:
        # Read the Excel sheet
        if data_type == 'dictionary':
            # For dictionary-type sheets without headers
            df = pd.read_excel(input_file, sheet_name=sheet_name, header=None)
            # Replace NaN with empty string in the entire DataFrame
            df = df.fillna('')
            # Convert to a dictionary
            json_data = dict(zip(df[0], df[1]))
        elif data_type == 'achievements':
            # For achievements sheet, we expect columns like: ID, achievement, Name, Text
            df = pd.read_excel(input_file, sheet_name=sheet_name)

            # Replace NaN with empty string in the entire DataFrame
            df = df.fillna('')

            # Initialize an empty dictionary for achievements
            json_data = {}

            # Iterate through rows to create a dictionary for each achievement
            for _, row in df.iterrows():
                json_data[row['ID']] = {
                    'achievement': int(row['achievement']),
                    'Name': row['Name'],
                    'Text': row['Text']
                }

        else:
            # For 'plants' or 'zombies' sheets
            df = pd.read_excel(input_file, sheet_name=sheet_name)

            # Replace NaN with empty string in the entire DataFrame
            df = df.fillna('')

            # Handle missing 'cost' column for plants
            if data_type == 'plants' and 'cost' in df.columns:
                df['cost'] = df['cost'].fillna('')

            # Convert to a list of dictionaries
            records_data = df.to_dict(orient='records')
            # Wrap the data in the appropriate JSON structure
            json_data = {data_type: records_data}

        # Save to JSON file
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)

        print(f"JSON file created successfully at {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
if __name__ == "__main__":
    # Process each sheet and save to the corresponding JSON file

    # Replace with path to your spreadsheet, where X is the language in question
    da_file = 'Fusion English Translation.xlsx'
    
    # Convert Plants sheet to JSON
    excel_to_json(
        input_file=da_file,
        output_file='LawnStringsTranslate.json',
        sheet_name='Plants',
        data_type='plants'
    )

    # Convert Zombies sheet to JSON
    excel_to_json(
        input_file=da_file,
        output_file='ZombieStringsTranslate.json',
        sheet_name='Zombies',
        data_type='zombies'
    )

    # Convert Strings sheet to JSON (Dictionary)
    excel_to_json(
        input_file=da_file,
        output_file='translation_strings.json',
        sheet_name='Strings',
        data_type='dictionary'
    )

    # Convert Regexes sheet to JSON (Dictionary)
    excel_to_json(
        input_file=da_file,
        output_file='translation_regexs.json',
        sheet_name='Regexes',
        data_type='dictionary'
    )

    # Convert Achievements sheet to JSON
    excel_to_json(
        input_file=da_file,
        output_file='AchievementsTextTranslate.json',
        sheet_name='Achievements',
        data_type='achievements'
    )
