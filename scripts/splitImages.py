# python script to split up a PDF into multiple jpegs
# start off hard coding it, but will add arguments later

from pdf2image import convert_from_path
from os import path

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


pdfpath = "/Users/jmaloof/Library/CloudStorage/GoogleDrive-jnmaloof@ucdavis.edu/Shared drives/IntBioTeam/Common Gardens/Data Scans/Size_survey_20221128.pdf"

file = path.basename(pdfpath)

file = path.splitext(file)[0] + "-"

images = convert_from_path(pdfpath, dpi=300, output_folder = "test_folder", fmt="jpg", output_file=file)
