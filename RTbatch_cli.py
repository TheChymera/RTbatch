#!/usr/bin/python
__author__ = 'Horea Christian'
import argparse
import RTbatch as rtb

parser = argparse.ArgumentParser()
parser.add_argument("input", help="input file for RT processing", type=str)
parser.add_argument("-t", "--template", help="markup template  for obtaining a codeblock with which you can display your images (choose from under .../RTbatch/templates)", type=str)
parser.add_argument("-m", "--do-minis", help="export", action="store_true")
parser.add_argument("-w", "--mini-width", help="export", type=int)
parser.add_argument("-f", "--do-fullsize", help="specify the number of faces on the dice", action="store_true")
parser.add_argument("-p", "--profile", help="specify the number of faces on the dice", type=str)
parser.add_argument("-o", "--output-dir", help="specify the number of faces on the dice", type=str)
args = parser.parse_args()

rtb.main(input_file=args.input, output_dir=args.output_dir, profile=args.profile, do_minis=args.do_minis, do_fullsize=args.do_fullsize, template_name=args.template, mini_width=args.mini_width)
