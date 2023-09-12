import os
import json
import glob
import MeCab
from collections import Counter
import click

def collect_japanese_text(directory_path):
    mecab = MeCab.Tagger("-Owakati")
    word_freq = Counter()

    # Create a single output file at the root directory
    with open(os.path.join(directory_path, "all_japanese_text_combined.txt"), "w", encoding="utf-8") as output_combined_file:
        for subdir, _, _ in os.walk(directory_path):
            os.chdir(subdir)
            for json_file in glob.glob("*.json"):
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for block in data.get("blocks", []):
                    for line in block.get("lines", []):
                        output_combined_file.write(line + "\n")
                        parsed_text = mecab.parse(line).split()
                        word_freq.update(parsed_text)
                        
    # Write the frequency data to a file
    with open(os.path.join(directory_path, "word_frequency_combined.txt"), "w", encoding="utf-8") as freq_file:
        for word, freq in word_freq.most_common():
            freq_file.write(f"{word}: {freq}\n")

@click.command()
@click.argument('directory', type=click.Path(exists=True))
def main(directory):
    """Collect all Japanese text from JSON files in a specified directory."""
    collect_japanese_text(directory)

if __name__ == '__main__':
    main()
