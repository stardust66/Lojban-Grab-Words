import argparse
from urllib.request import urlopen
import re

# Requires --type [word_type] argument, which specifies from which
# dictionary the program searches for words.
parser = argparse.ArgumentParser(description="Grab words from vlasisku.")
parser.add_argument("--type", required=True, choices=["gismu", "cmavo",
                    "experimental-cmavo", "fu'ivla", "cmene"], help="The type\
                    of word to grab.")

# Only execute the following if used in the command line.
if __name__ == "__main__":
    word_type = parser.parse_args().type

    # Words of type [word_type] can be found at the url below
    url = "http://vlasisku.lojban.org/vlasisku/" + word_type
    content = str(urlopen(url).read())

    # Look for words in the content. This step is dependent on the structure
    # of the website.
    word_count = 0
    words = {}
    word_index = content.find("On type:")
    start_index = content.find("<dt>", word_index)

    # Regex object for matching html tags (things inside angle brackets)
    html_tags = re.compile("<.*?>")

    while word_count < 20 and start_index != -1:
        end_index = content.find("</dt>", start_index)
        def_start_index = content.find("<dd>", end_index)
        def_end_index = content.find("</dd>", def_start_index)

        word = content[start_index:end_index + 5]
        definition = content[def_start_index:def_end_index + 5]

        # Use regex to remove tags
        word = re.sub(html_tags, '', word)
        definition = re.sub(html_tags, '', definition)

        # Store result in dictionary
        words[word] = definition

        start_index = content.find("<dt>", def_end_index)
