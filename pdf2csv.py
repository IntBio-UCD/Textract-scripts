# python script to split up a PDF into multiple jpegs
# start off hard coding it, but will add arguments later

import argparse
import os
import boto3
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
        csv += '\n\n'

    return csv

def generate_table_csv(table_result, blocks_map, table_index):
    rows = get_rows_columns_map(table_result, blocks_map)

    table_id = 'Table_' + str(table_index)
    
    # get cells.
    csv = 'Table: {0}\n\n'.format(table_id)

    for row_index, cols in rows.items():
        
        for col_index, text in cols.items():
            csv += '{}'.format(text) + ","
        csv += '\n'
        
    csv += '\n\n\n'
    return csv

# Set up the parser

parser = argparse.ArgumentParser(description='Split a multipage PDF into individual jpegs')

parser.add_argument('pdf', help = "PDF file to process" )
parser.add_argument('-o', '--out', dest = 'csvpath', help = "Folder for output csv files", default = ".")

args = parser.parse_args()

# temp directory for jpegs:

jpeg_dir = tempfile.TemporaryDirectory()

# Get the file and split it up

if(not os.path.exists(args.out)):
    os.makedirs(args.out)

filestem = os.path.basename(args.pdf)

filestem = os.path.splitext(filestem)[0] + "-"

images = convert_from_path(args.pdf, dpi=300, output_folder = args.out, fmt="jpg", output_file=filestem)

for jfile in os.listdir(jpeg_dir):
    table_csv = get_table_csv_results(os.path.join(jpeg_dir,jfile))

    output_file = os.path.join(args.out, os.path.splitext(jfile)[0] + ".csv")

    # replace content
    with open(output_file, "wt") as fout:
        fout.write(table_csv)

    # show the results
    print('CSV OUTPUT FILE: ', output_file)



