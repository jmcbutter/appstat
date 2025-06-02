#!/usr/bin/env python3
import argparse


def create_new_application(args):
    print(args.company, args.position)


def main():
    parser = argparse.ArgumentParser(prog='PROG')

    command_parsers = parser.add_subparsers()

    # New Application
    new_parser = command_parsers.add_parser('new')
    new_parser.add_argument('-c', '--company', required=True)
    new_parser.add_argument('-p', '--position', required=True)
    new_parser.set_defaults(func=create_new_application)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
