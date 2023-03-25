#!/home/cacaprog/anaconda3/bin/python
"""
Author : cacaprog <cacaprog@localhost>
Date   : 2023-03-25
Purpose: Test to create a new program
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python test',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--name',
                        help='Name to greet',
                        metavar='name',
                        type=str,
                        default='World')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print('Hello, ' + args.name + '!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
