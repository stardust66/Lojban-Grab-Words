import argparse
from urllib.request import urlopen

# Requires --type [word_type] argument, which specifies from which
# dictionary the program searches for words.
parser = argparse.ArgumentParser(description="Grab words from vlasisku.")
parser.add_argument("--type", required=True, choices=["gismu",
                    "cmavo", "experimental-cmavo", "fu'ivla", "cmene"], help="The type of word to grab.")

# Only execute the following if used in the command line.
if __name__ == "__main__":
    word_type = parser.parse_args().type

    # Words of type [word_type] can be found at the url below
    url = "http://vlasisku.lojban.org/vlasisku/" + word_type
    content = urlopen(url).read()
