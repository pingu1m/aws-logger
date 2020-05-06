import argparse
import boto3
from clog.dynamo import put


def get_parser():
    return 'put', parse, parser


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--level', action='store', help='Directory to list', required=True)
    parser.add_argument('text', nargs="?", help='Directory to list')
    return parser


def level_flag():
    pass

def parse(args):
    # TODO: Setup argparse arguments group
    if args.level and args.text:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(args.level)
        result = put(table, args.text)
        # print(result)

