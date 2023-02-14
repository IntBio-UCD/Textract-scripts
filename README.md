# Textract-scripts
This script takes an input PDF that is data sheet scans and returns a csv with the contents.

AWS's documentation is [here](https://docs.aws.amazon.com/textract/index.html)



## Install prerequisites

### AWS CLI

You will need an AWS KEY and Secret.  See AWS for more info.  (Or ask Julin for a key)

Once you have a key, you will need [AWS CLI](https://aws.amazon.com/cli/) to manage your access to AWS.

You can either download an installer from the above link, or on a mac with [homebrew]() installed:
    brew install awcli

Then configure aws with your key.   You can leave region as us-east-1 ; select text for your default output type.
    aws configure

### Miniconda
If you don't already have conda installed, install [miniconda](https://docs.conda.io/en/latest/miniconda.html)

If you are on a mac running homebrew, you can use

    brew install miniconda
    conda init "$(basename "${SHELL}")"

Once conda is installed:
    conda create -n textract python=3.10.8 poppler
    conda activate textract
    pip install boto3 #aws bindings
    pip install pdf2image


## To run the script
     conda activate textract

you will need to have google drive running on your computer  
then `cd` to the `Common Gardens` folder in `IntBioTeam`
On my computer it is like this
     cd ~/library/CloudStorage/GoogleDrive-jnmaloof@ucdavis.edu/Shared\ drives/IntBioTeam/Common\ Gardens/
     
now run the script.  
     python pdf2csv.py  -o UCD2022_2023/RawCSVs/ UCD2022_2023/DataScans/*.pdf   
     # this will process ALL pdf files in `UCD2022_2023/DataScans`.

you will need to manually move the PDFs to `UCD2022_2023/DataScans-Processed/` afterwards, e.g.
     mv UCD2022_2023/DataScans/*.pdf UCD2022_2023/DataScans-Processed

Note: __Existing csvs with the same name will be overwritten__