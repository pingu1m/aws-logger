import argparse
import sys

from clog import clog


def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='commands', dest="command")

    for parser_name, parser_func, subparser in clog.get_parsers():
        new_subparser = subparsers.add_parser(parser_name, add_help=False, parents=[subparser()])
        new_subparser.set_defaults(func=parser_func)

    return parser


def main():
    args = create_parser().parse_args()

    if not args.text and not sys.stdin.isatty() and args.command == 'put':
        input_stream = sys.stdin
        for line in input_stream:
            args.text = line
            args.func(args)
            # print(line, end='')
    else:
        args.func(args)
