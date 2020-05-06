import argparse


def get_parser():
    return 'get', parse, parser


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--generate', action='store_true', help='Directory to list')
    parser.add_argument('-l', '--level', action='store_true', help='Directory to list')
    return parser


def parse(args):
    print("Get command")
    print(args)
