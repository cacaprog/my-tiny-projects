#!/home/cacaprog/anaconda3/bin/python
"""
Author : cacaprog <cacaprog@localhost>
Date   : 2023-05-20
Purpose: Howler something cool in uppercase
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler upper-case input',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')
    
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    
    return args

# --------------------------------------------------
def main():
    """Make a jazz rock here!"""

    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + '\n')
    out_fh.close()

# --------------------------------------------------
if __name__ == '__main__':
    main()
