import argparse

# Requires --type [word_type] argument, which specifies from which
# dictionary the program searches for words.
parser = argparse.ArgumentParser(description="Grab words from vlasisku.")
parser.add_argument("--type", required=True, choices=["gismu",
                    "cmavo", "experimental-cmavo", "fu'ivla", "cmene"], help="The type of word to grab.")

word_type = parser.parse_args().type

# Displays the url that will be used to grab words. This will be
# replaced with the urlopen code using urllib.
print("http://vlasisku.lojban.org/vlasisku/" + word_type)
