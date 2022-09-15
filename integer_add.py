'''Simple code to try out pytest'''

import argparse

def main(argv=None):
    '''Main program to add to integers together
    If a non-integer is passed it will be
    set to 0.'''

    parser = argparse.ArgumentParser()
    parser.add_argument('value1')
    parser.add_argument('value2')
    args = parser.parse_args(argv)

    try:
        value1_int = int(args.value1)
    except ValueError:
        value1_int = 0

    try:
        value2_int = int(args.value2)
    except ValueError:
        value2_int = 0

    print(f'{ value1_int + value2_int }')

if __name__ == '__main__':
    main()
