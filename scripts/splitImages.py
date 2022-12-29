# python script to split up a PDF into multiple jpegs
# start off hard coding it, but will add arguments later

import argparse
from pdf2image import convert_from_path
import os

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

# Set up the parser

parser = argparse.ArgumentParser(description='Split a multipage PDF into individual jpegs')

parser.add_argument('input', help = "path to a PDF file" )
parser.add_argument('--out', help = "optional output folder for jpegs", default="split_temp")

#args = parser.parse_args()

args = parser.parse_args(['/Users/jmaloof/Library/CloudStorage/GoogleDrive-jnmaloof@ucdavis.edu/Shared drives/IntBioTeam/Common Gardens/Data Scans/Size_survey_20221128.pdf',
                '--out', 'test_folder'])

if(not os.path.exists(args.out)):
    os.makedirs(args.out)

file = os.path.basename(args.input)

file = os.path.splitext(file)[0] + "-"

images = convert_from_path(args.input, dpi=300, output_folder = args.out, fmt="jpg", output_file=file)
