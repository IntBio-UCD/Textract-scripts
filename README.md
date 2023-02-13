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
     conda activate textract
     # you will need to have google drive running on your computer
     # then `cd` to the `Common Gardens` folder in `IntBioTeam`
     # On my computer it is like this
     cd ~/library/CloudStorage/GoogleDrive-jnmaloof@ucdavis.edu/Shared\ drives/IntBioTeam/Common\ Gardens/
     
     # then run the program.  
     python pdf2csv.py  -o UCD2022_2023/RawCSVs/ UCD2022_2023/DataScans/*.pdf   
     # this will process ALL pdf files in `UCD2022_2023/DataScans`.
     # you will need to manually move them to `UCD2022_2023/DataScans-Processed/` afterwards, e.g.
     mv UCD2022_2023/DataScans/*.pdf UCD2022_2023/DataScans-Processed

Note: __Existing csvs with the same name will be overwritten__