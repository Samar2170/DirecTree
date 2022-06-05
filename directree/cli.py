import argparse
import os
import sys
from directree import __version__
from directree.directree import DirecTree
from directree.cloc import Director
from directree.cfm import Accountant

def parse_cmd_line_args():
    parser = argparse.ArgumentParser(
        prog='directree',
        description='Directories tree generator',
        epilog='Example: directree -fs /home/user/dir1')
    parser.__version__ = __version__

    parser.add_argument('-v','--version',action='version')
    parser.add_argument("root_dir",metavar="ROOT_DIR",nargs="?", default=".", help="Directory to Analyse")
    
    parser.add_argument('-d','--dirs',action='store_true',help='Directory only')
    parser.add_argument('-fs','--files',help='List of Files by extension',action="store_true")
    parser.add_argument('-c','--cloc',action='store_true',help='Count lines of code in each directory')
    parser.add_argument('-t','--tree',action='store_true',help='Print directories tree')
    return parser.parse_args()

def call():
    args = parse_cmd_line_args()
    root_dir=args.root_dir
    if args.tree:
        if args.cloc or args.files:
            print("Cant select -c and -fs with -t")
            sys.exit(1)
        tree=DirecTree(root_dir,dirs_only=args.dirs)
        tree.generate()
    if args.cloc:
        director = Director(root_dir)
        director.build_cloc()
    if args.files:
        accountant=Accountant(root_dir)
        accountant.build_cfm()
    
