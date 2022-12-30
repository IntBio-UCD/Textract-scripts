# Textract-scripts
This script takes an input PDF that is data sheet scans and returns a csv with the contents.

AWS's documentation is [here](https://docs.aws.amazon.com/textract/index.html)

## Install prerequisites
    conda create -n textract python=3.10.8 poppler
    conda activate textract
    pip install boto3 #aws bindings
    pip install pdf2image

## AWS authentication.
You will need an AWS KEY and Secret.  See AWS for more info.

## To run the script
     python pdf2csv.py UCD2022_2023/DataScans/Size_survey_20221128.pdf -o UCD2022_2023/RawCSVs/  
