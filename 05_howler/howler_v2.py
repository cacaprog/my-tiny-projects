#!/home/cacaprog/anaconda3/bin/python
"""
Author : cacaprog <cacaprog@localhost>
Date   : 2023-05-20
Purpose: Howler something cool in lower-case, a low memory option
"""

import argparse
import os
import sys
import io

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler lower-case input',
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
        args.text = open(args.text)
    else:
        # io.StringIO will act like an open file handle
        args.text = io.StringIO(args.text + '\n') 
    
    return args

# --------------------------------------------------
def main():
    """Make a progrock here!"""

    args = get_args()
    # I don't have to call open() on sys.stdout cause it's always avaiable and open for business 
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    # read the input (io.StringIO() or file handle  line by line)
    for line in args.text: 
        out_fh.write(line.lower())
    out_fh.close()

# --------------------------------------------------
if __name__ == '__main__':
    main()
