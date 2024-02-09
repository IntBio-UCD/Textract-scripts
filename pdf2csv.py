# python script to split up a PDF into multiple jpegs

import argparse
import os
import boto3
import glob
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import webbrowser
import json
import io
from io import BytesIO
import sys
import tempfile
# from pprint import pprint

# Functions from AWS code example at https://docs.aws.amazon.com/textract/latest/dg/examples-export-table-csv.html

def get_rows_columns_map(table_result, blocks_map):
    rows = {}
    for relationship in table_result['Relationships']:
        if relationship['Type'] == 'CHILD':
            for child_id in relationship['Ids']:
                cell = blocks_map[child_id]
                if cell['BlockType'] == 'CELL':
                    row_index = cell['RowIndex']
                    col_index = cell['ColumnIndex']
                    if row_index not in rows:
                        # create new row
                        rows[row_index] = {}
                        
                    # get the text value
                    rows[row_index][col_index] = get_text(cell, blocks_map)
    return rows


def get_text(result, blocks_map):
    text = ''
    if 'Relationships' in result:
        for relationship in result['Relationships']:
            if relationship['Type'] == 'CHILD':
                for child_id in relationship['Ids']:
                    word = blocks_map[child_id]
                    if word['BlockType'] == 'WORD':
                        text += word['Text'] + ' '
                    if word['BlockType'] == 'SELECTION_ELEMENT':
                        if word['SelectionStatus'] =='SELECTED':
                            text +=  'X '    
    return text


def get_table_csv_results(file_name):

    with open(file_name, 'rb') as file:
        img_test = file.read()
        bytes_test = bytearray(img_test)
        print('Image loaded', file_name)

    # process using image bytes
    # get the results
    client = boto3.client('textract')

    response = client.analyze_document(Document={'Bytes': bytes_test}, FeatureTypes=['TABLES'])

    # Get the text blocks
    blocks=response['Blocks']
#    pprint(blocks)

    blocks_map = {}
    table_blocks = []
    for block in blocks:
        blocks_map[block['Id']] = block
        if block['BlockType'] == "TABLE":
            table_blocks.append(block)

    if len(table_blocks) <= 0:
        return "<b> NO Table FOUND </b>"

    csv = ''
    for index, table in enumerate(table_blocks):
        csv += generate_table_csv(table, blocks_map, index +1)
#        csv += '\n\n'

    return csv

def generate_table_csv(table_result, blocks_map, table_index):
    rows = get_rows_columns_map(table_result, blocks_map)

    table_id = 'Table_' + str(table_index)
    
    # get cells.
 #   csv = 'Table: {0}\n\n'.format(table_id)
    csv = '' #initiate the csv

    for row_index, cols in rows.items():
        
        for col_index, text in cols.items():
            csv += '{}'.format(text) + ","
        csv += '\n'
        
 #   csv += '\n\n\n'
    return csv

# Set up the parser

parser = argparse.ArgumentParser(description='Use textract to extract text from a [multipage] PDF of data sheets into csv files')
parser.add_argument('-o', '--out', dest = 'csvpath', help = "Folder for output csv files", default = ".")

parser.add_argument('pdfs', help = "PDF file or files, or a single directory that contains PDF files to process", nargs = "+" )

args = parser.parse_args()

if(not os.path.exists(args.csvpath)):
    os.makedirs(args.csvpath)

if(os.path.isdir(args.pdfs[0])):
    pdfFiles = glob.glob(os.path.join(args.pdfs[0], '*.pdf'))
else:
    pdfFiles = args.pdfs

for pdf in pdfFiles:

    # create temp directory for jpegs:
    jpeg_temp_dir = tempfile.TemporaryDirectory()
    jpeg_dir = jpeg_temp_dir.name


    filestem = os.path.basename(pdf)

    filestem = os.path.splitext(filestem)[0]

    # define output file path and open it.  Note: all csvs from a PDF appended into a single csv
    output_file = os.path.join(args.csvpath, filestem + ".csv")
    csv = open(output_file, "wt") #will overwite existing content

    # Get the file and split it up

    images = convert_from_path(pdf, dpi=300, output_folder = jpeg_dir, fmt="jpg", output_file=filestem + "-")

    jfiles = os.listdir(jpeg_dir)

    jfiles.sort()

    for jfile in jfiles:
        # print(jfile)
        table_csv = get_table_csv_results(os.path.join(jpeg_dir,jfile))
        # print(table_csv)


        # append content
        csv.write(table_csv)


    csv.close()

    # show the results
    print('CSV OUTPUT FILE: ', output_file)

    jpeg_temp_dir.cleanup() 



