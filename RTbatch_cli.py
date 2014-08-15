#!/usr/bin/python
__author__ = 'Horea Christian'
import argparse
import RTbatch as rtb

parser = argparse.ArgumentParser()
parser.add_argument("input", help="Input file for RT processing", type=str)
parser.add_argument("-f", "--do-fullsize", help="Export files in full-size", action="store_true")
parser.add_argument("-m", "--do-minis", help="Export file as thumbnails (minis)", action="store_true")
parser.add_argument("-w", "--mini-width", help="Thumbnail (mini) width", type=int)
parser.add_argument("-i", "--iptc-profile", help="Path to IPTC profile (defaults to .../RTbatch/profiles/iptc.pp3)", type=str)
parser.add_argument("-o", "--output-dir", help="Specify the output directory (by default .../RTbatch/output/)", type=str)
parser.add_argument("-t", "--template", help="Markup template  for obtaining a codeblock with which you can display your images (choose from under .../RTbatch/templates)", type=str)
args = parser.parse_args()

rtb.main(input_file=args.input, output_dir=args.output_dir, iptc_profile=args.iptc_profile, do_minis=args.do_minis, do_fullsize=args.do_fullsize, template_name=args.template, mini_width=args.mini_width)
