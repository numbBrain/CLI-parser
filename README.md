# CLI to be used for web scraping

This is a simple command-line argument parser intended to be used for web scraping tasks

`$ python parser.py --help`

```
usage: parser.py [-h] [--links LINKS [LINKS ...] | --read FILE.txt] [--dest DESTINATION] [--version]

Generic argument parser to be used for web scraping

optional arguments:
  -h, --help            show this help message and exit
  --links LINKS [LINKS ...]
                        take links from STDI
  --read FILE.txt       read links from file
  --dest DESTINATION    specify download directory
  --version             show program's version number and exit
```

`--links` and `--read` can be used to read links. They are  mutually exclusive. Hence, `--links` and `--read` cannot be used together.

`--read` reads links from a file. One link per line, redundant links are removed and links are stored in a list.

`--links` reads links from standard input and stores them in a list. Space is the delimiter, no need to use comma in-between links. Redundant links are removed

`--dest` can be used to get download location. By default, it takes the current working directory.

## Usage:
Add this to your script:

    from parser import suppliedLinks, destination

## Requirements:

Was made using argparse, doesn't require any third-party modules

**Feedbacks are appreciated**

