import os
import json
import glob
from collections import Counter
import MeCab
import click

def collect_japanese_text(directory_path):
    output_file_path = os.path.join(directory_path, "all_japanese_text.txt")
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for root, dirs, files in os.walk(directory_path):
            if '_ocr' in root:
                os.chdir(root)
                for json_file in glob.glob("*.json"):
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    for block in data.get("blocks", []):
                        for line in block.get("lines", []):
                            output_file.write(line + "\n")
    return output_file_path

def generate_frequency_list(directory, output_file_path):
    freq_file_path = os.path.join(directory, "frequency_list.txt")
    mecab = MeCab.Tagger("-Owakati")
    counter = Counter()
    with open(output_file_path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            words = mecab.parse(line).split()
            counter.update(words)
    with open(freq_file_path, "w", encoding="utf-8") as freq_file:
        for word, count in counter.most_common():
            freq_file.write(f"{word}: {count}\n")

@click.command()
@click.argument('directory', type=click.Path(exists=True))
def main(directory):
    """Collect all Japanese text from JSON files in a specified directory and its subdirectories."""
    output_file_path = collect_japanese_text(directory)
    generate_frequency_list(directory, output_file_path)

if __name__ == '__main__':
    main()

