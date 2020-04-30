import os
import argparse

parser = argparse.ArgumentParser(description="Generic argument parser to be used for web scraping")
groupParser = parser.add_mutually_exclusive_group()
groupParser.add_argument("--links", type=str, nargs="+", const=None, help="take links from STDI")
groupParser.add_argument("--read" , type=argparse.FileType("r", encoding="UTF-8"), const=None, metavar="FILE.txt", help="read links from file")
parser.add_argument("--dest" ,type=str, nargs=1, default=os.getcwd(), metavar="DESTINATION", help="specify download directory")
parser.add_argument("--version", action="version", version="%(prog)s 1.0")
args = parser.parse_args()

destination = args.dest

#check if atleast one argument is passed
if not (args.read or args.links):
    
    print("[-] No options specified, use --help for available options")
    exit()

else:

    if args.links:
        suppliedLinks = list(dict.fromkeys(args.links)) 
    else:
        suppliedLinks = list(dict.fromkeys(list(args.read.read().splitlines())))
        args.read.close()
