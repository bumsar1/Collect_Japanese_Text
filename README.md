# Collect_Japanese_Text
The Python script is designed to automatically collect all Japanese text from a series of JSON files located in a specified folder.

Requirements
Python 3.x: Make sure Python 3.x is installed on your system. You can download it from the official website.
MeCab Library: This is used for parsing Japanese text.
"pip install mecab-python3"

Step 2: Run the Script
Open your command prompt or terminal.
Navigate to the folder containing the Python script.
Run the command:
python collect_and_analyze_japanese_text.py "path_to_your_folder"
Replace path_to_your_folder with the directory containing your JSON files for single volume.
Replace path_to_your_folder with the directory _ocr for all the volumes of series combined
Replace path_to_your_folder with the directory containing all your manga for getting a frequency of all your manga.


The collect_japanese_text function scans through all the JSON files in the specified directory and writes the Japanese text to a file named all_japanese_text.txt.

The analyze_frequency function processes the collected text, breaks it down into individual words, and counts the frequency of each word. The frequency data is saved to a file named word_frequencies.txt.
