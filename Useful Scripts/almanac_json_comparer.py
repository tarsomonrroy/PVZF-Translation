import json
import os

# Change the current working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def merge_entries(primary_list, fallback_list, key):
    """
    Merge two lists of dictionaries based on a shared key.
    Prioritizes entries in primary_list when the key is present in both.
    """
    primary_dict = {item[key]: item for item in primary_list}
    fallback_dict = {item[key]: item for item in fallback_list}

    result = []

    # Use primary when present in both
    for k in sorted(primary_dict):
        if k in fallback_dict:
            result.append(primary_dict[k])

    # Add fallback-only entries
    for k in sorted(fallback_dict):
        if k not in primary_dict:
            result.append(fallback_dict[k])

    return result

# ================== WORKING AREA ==================

# Input file paths (X = target language, Y = English fallback)
lawn_primary_file = 'LawnStringsTranslate_fr.json'
lawn_english_file = 'LawnStringsTranslate_en.json'

zombie_primary_file = 'ZombieStringsTranslate_fr.json'
zombie_english_file = 'ZombieStringsTranslate_en.json'

# Output file paths
output_lawn_file = 'LawnStringsTranslate.json'
output_zombie_file = 'ZombieStringsTranslate.json'

# Load JSON data
with open(lawn_primary_file, 'r', encoding='utf-8') as f:
    lawn_primary_data = json.load(f)
with open(lawn_english_file, 'r', encoding='utf-8') as f:
    lawn_english_data = json.load(f)

with open(zombie_primary_file, 'r', encoding='utf-8') as f:
    zombie_primary_data = json.load(f)
with open(zombie_english_file, 'r', encoding='utf-8') as f:
    zombie_english_data = json.load(f)

# Merge plant entries
merged_plants = merge_entries(
    lawn_primary_data.get('plants', []),
    lawn_english_data.get('plants', []),
    key='seedType'
)
with open(output_lawn_file, 'w', encoding='utf-8') as f:
    json.dump({'plants': merged_plants}, f, indent=4, ensure_ascii=False)

# Merge zombie entries
merged_zombies = merge_entries(
    zombie_primary_data.get('zombies', []),
    zombie_english_data.get('zombies', []),
    key='theZombieType'
)
with open(output_zombie_file, 'w', encoding='utf-8') as f:
    json.dump({'zombies': merged_zombies}, f, indent=4, ensure_ascii=False)

print("✓ Merged output saved to:")
print(f"  - {output_lawn_file}")
print(f"  - {output_zombie_file}")

