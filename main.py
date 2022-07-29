import argparse

parser = argparse.ArgumentParser(description='Hack Simulator')
parser.add_argument('path', type=str, metavar='path', help="absolute or relative path to the hack file")

args = parser.parse_args()

if __name__ == '__main__':
    print(args.path)
