#!/home/cacaprog/anaconda3/bin/python
"""
Author : cacaprog <cacaprog@gmail.com>
Date   : 2023-04-22
Purpose: Jump the five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Send your message',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Type the message')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a progrock here"""

    args = get_args()
    
    jumper = {'1':'9', '2':'8', '3':'7', '4':'6', '5':'0', '6':'4', '7':'3', '8':'2', '9':'1', '0':'5'}     
# solution 1
 #   for char in args.text:
 #       print(jumper.get(char, char), end='')
 #   print() # print a new line after done

# solution 2
 #   new_text = ''
#   for char in args.text:
#        new_text += jumper.get(char, char)
#    print(new_text)

# solution 3
#    new_text = []
#    for char in args.text:
#        new_text.append(jumper.get(char, char))
#    print(''.join(new_text))

# solution 4
#    print(''.join([jumper.get(char, char) for char in args.text]))


# solution 5
    print(args.text.translate(str.maketrans(jumper)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
