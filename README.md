# PVZRH-Multi-language-Mod-Translation files
Translation files of the Multi-language Mod for PvZ: Fusion. The download for the Multi-language Mod can be found [here](https://rentry.co/playpvzfusion/). Current supported base game version: 2.6.1.

## Notice to Translators
The translator mod, PvZ_Fusion_Translator.dll, is currently closed source, but you can grab the latest build dll on the root directory of this repo's main branch. It is constantly updated.

## Instructions on Using the Scripts in [`Useful Scripts`](https://github.com/Teyliu/PVZF-Translation/tree/main/Useful%20Scripts)

There are 4 Python scripts.

csver.py converts [json files](https://en.wikipedia.org/wiki/JSON?oldformat=true) to [csv files](https://en.wikipedia.org/wiki/Comma-separated_values?oldformat=true). The translation mod reads jsons to apply translations, while csvs can be imported to an online spreadsheet like Google Spreadsheet to faciliate group editing, but with the downside of not being able to reflect changes in-game very easily. You can find the jsons by grabbing them from the mod files or download the spreadsheet as xlsx and convert them to json using another script, jsonifier.py.

jsonifier.py converts an xlsx file into different jsons that are readily usable for the translation mod. When you have finished with the online spreadsheet, download it as xlsx and convert them to jsons, copy to where the mod reads them (usually, `[Your Game Location]\Game Files\Mods\PvZ_Fusion_Translator\Localization\X Language\Almanac or Strings`)

almanac_json_comparer.py and strings_json_comparer.py handle comparisons of jsons between different translations, mostly between your language and English. These specifically compare jsons. Look inside the scripts to see the name requirements for the input files. They both prioritize using the language that's being worked on for entries that exists in both inputs, and append the entries only present in the English version (untranslated) at the bottom. N.B.: For the almanac, it only compares IDs, so balance changes are not reflected. 

All 4 scripts read from the path where the script is located.


ReadMe is under construction.
> Reminder for myself to update the RM to include instructions for the scripts and a general guide to translating the game.


## License

All translation files in this repository are licensed under  
**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**  
🔗 https://creativecommons.org/licenses/by-nc/4.0/

Commercial use is not permitted.
