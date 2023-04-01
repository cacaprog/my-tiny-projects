#!/home/cacaprog/anaconda3/bin/python
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Choose the article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='The thing I see from here')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make things happen!"""

    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')



# --------------------------------------------------
if __name__ == '__main__':
    main()

