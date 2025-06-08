import json
import os

# Change the current working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Now all relative paths will be relative to this script's location

def compare_json_files(a_file, b_file, c_file):
    """
    Compares two JSON files (A and B) and generates a new JSON file (C) based on the rules:
    a. If a key is present in both A and B, use A's value in C.
    b. If a key is only in A, don't include it in C.
    c. If a key is only in B, include it in C with B's value.

    Parameters:
    a_file (str): Path to the first JSON file (A).
    b_file (str): Path to the second JSON file (B).
    c_file (str): Path to save the generated JSON file (C).
    """
    try:
        # Load the JSON data from files
        with open(a_file, 'r', encoding='utf-8') as file:
            a_data = json.load(file)
        
        with open(b_file, 'r', encoding='utf-8') as file:
            b_data = json.load(file)
        
        # Ensure A and B are dictionaries
        if not isinstance(a_data, dict) or not isinstance(b_data, dict):
            raise ValueError("Both A and B must be dictionaries.")
        
        # Generate the output dictionary
        c_data = {}

        # Rule (a): Keys present in both A and B, use A's value
        for key in a_data:
            if key in b_data:
                c_data[key] = a_data[key]
        
        # Rule (c): Keys only in B, include them with B's value
        for key in b_data:
            if key not in a_data:
                c_data[key] = b_data[key]
        
        # Save the generated dictionary to C.json
        with open(c_file, 'w', encoding='utf-8') as file:
            json.dump(c_data, file, indent=4, ensure_ascii=False)
        
        print(f"Comparison completed successfully. Output saved to {c_file}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
# Replace 'A.json', 'B.json', and 'C.json' with your file paths
compare_json_files('translation_regexs_fr.json', 'translation_regexs_en.json', 'translation_regexs.json')
compare_json_files('translation_strings_fr.json', 'translation_strings_en.json', 'translation_strings.json')