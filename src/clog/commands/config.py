import argparse
import sys
from configparser import ConfigParser, ParsingError
from pathlib import Path

import boto3
from clog.dynamo import is_table_created, create_table
from clog.exceptions.exceptions import ConfigNotSetException


def get_parser():
    return 'config', parse, parser


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--generate', action='store_true', help='Output a config sample')
    parser.add_argument('-l', '--level', action='store_true', help='Show configured levels')
    parser.add_argument('-d', '--dump', action='store_true', help='Dump current config')
    parser.add_argument('--check-levels', action='store_true', help='Dump current config')

    return parser


def level_flag():
    for level in get_levels():
        print(level)


def generate_flag():
    temp_parser = ConfigParser()
    temp_parser.add_section('main')
    temp_parser.set('main', 'default_engine', 'dynamodb')

    temp_parser.add_section('level_backups')
    temp_parser.set('level_backups', 'storage', 'dynamodb')
    temp_parser.set('level_backups', 'table', 'backups')

    temp_parser.add_section('level_production_updates')
    temp_parser.set('level_production_updates', 'storage', 'aurora')
    temp_parser.set('level_production_updates', 'username', 'dhellmann')
    temp_parser.set('level_production_updates', 'password', 'secret')
    temp_parser.set('level_production_updates', 'table', 'prod_updates')


    temp_parser.add_section('level_magento')
    temp_parser.set('level_magento', 'storage', 'dynamodb')
    temp_parser.set('level_magento', 'table', 'magento')

    temp_parser.write(sys.stdout)


def dump_flag():
    config_parser = get_config_parser()
    for level in get_levels():
        has_section = config_parser.has_section(f"level_{level}")
        print('{} section exists: {}'.format(level, has_section))

        for name, value in config_parser.items(f"level_{level}"):
            print('  {} = {}'.format(name, value))
        print()


def is_config_set():
    return get_config_parser().has_section('main')


def get_levels():
    config_parser = get_config_parser()
    return [section.replace("level_", '') for section in config_parser.sections() if section.startswith('level_')]


def get_config_parser():
    curr_config = Path.home() / '.clogrc'
    try:
        config_parser = ConfigParser(allow_no_value=True)
        config_parser.read(curr_config)
    except ParsingError as err:
        print('Could not parse config:', err)

    return config_parser


def get_config():
    config_parser = get_config_parser()
    if is_config_set():
        return {level: {inner_k: inner_v for inner_k, inner_v in config_parser.items(f"level_{level}")} for level in
                get_levels()}
    else:
        raise ConfigNotSetException("Config not set. Please run 'clog config -h' for help")

def check_levels_flag():
    engine = boto3.client('dynamodb')
    print("Checking Levels")
    config = get_config()
    levels = get_levels()
    for level in levels:
        if config[level]['storage'] == 'dynamodb':
            if is_table_created(engine, level):
                print(f"Level {level} dynamodb table exists")
            else:
                result = create_table(engine, level)
                print(f"Creating dynamodb table {level} status: " + str(result))
        if config[level]['storage'] == 'aurora':
            print("Storage aurora not yet implemented")


def parse(args):
    # TODO: Setup argparse arguments group
    if args.generate:
        generate_flag()
    if args.level:
        level_flag()
    if args.dump:
        dump_flag()
    if args.check_levels:
        check_levels_flag()
