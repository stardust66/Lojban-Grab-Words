# sutyjai lo valsi

This is a command-line program written in Python that takes Lojban words from [vlasisku.lojban.org](http://vlasisku.lojban.org) and puts them in a file named ```valsi.txt``` for easy importing into Quizlet, perfect for studying Lojban vocabulary.

## How to Use

Using the program is simple. Make sure you have Python3 and type the following in your command-line:
```
valsi.py --type (word_type) [--limit (limit)]
```
where (word_type) can be gismu, cmavo, experimental-cmavo, fu'ivla, and cmene, corresponding to different types of words in Lojban. The limit option is optional. You can use it to set the number of words you want in your file. If you leave the generated file in the same directory as ```valsi.py```, the program will pick up where it left off if you're pulling words from the same page as last time.
