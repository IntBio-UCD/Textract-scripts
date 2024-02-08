# Textract-scripts
This script takes an input PDF that is data sheet scans and returns a csv with the contents.

AWS's documentation is [here](https://docs.aws.amazon.com/textract/index.html)

## Install prerequisites

### AWS CLI

You will need an AWS KEY and Secret.  See AWS for more info.  (Or ask Julin for a key)

Once you have a key, you will need [AWS CLI](https://aws.amazon.com/cli/) to manage your access to AWS.

#### AWS install for PC 

Download an installer from the above link

#### AWS install for MAC

Download an installer from the above link or if you have [homebrew](https://brew.sh/) installed:

    brew install awscli

#### AWS configure (MAC and PC)

Open up terminal (Mac) or command prompt (PC) and type

    aws configure

Then configure aws with your key.   You set region as `us-west-2` or `us-east-2` ; select `text` for your default output type.  Note us-west-1 (Northern California) is more expensive than the others. 

### Miniconda
If you don't already have conda installed, install [miniconda](https://docs.conda.io/en/latest/miniconda.html)

#### PC or MAC
Use the installer at the link above

#### MAC optional alternative
If you are on a mac running homebrew, you can use

    brew install miniconda
    conda init "$(basename "${SHELL}")"

#### Create a conda environment for textract

Once conda is installed:

Open terminal (MAC) or Anaconda Prompt (PC)

    conda create -n textract python=3.10.8 poppler
    conda activate textract
    pip install boto3 #aws bindings
    pip install pdf2image

## Clone the repository
First `cd` to wherever you want the repository to go.  Then clone it.

__MAC:__
    cd ~/git
    git clone https://github.com/IntBio-UCD/Textract-scripts.git

__PC:__
Similar to above, but use `\` instead of `/`.  

## Google Drive
If your images are stored on google drive (e.g. Intbio project), you will need to have google drive running on your computer.

You will also need to enable offline access for the folder that has the images.  On a mac this means clicking on the "cloud" icon in the finder on the folder or right-clicking on the folder and selecting "available offline".  PC: right click and select "available offline"

It is easiest if you make a symbolic link pointing to the data folder `UCD2022_2023` from the repository.  On my computer it is like this:

__MAC:__
     cd ~/git/Textract-scripts
     ln -s ~/Library/CloudStorage/GoogleDrive-jnmaloof@ucdavis.edu/Shared\ drives/IntBioTeam/Common\ Gardens/UCD2022_2023/ ./

__PC:__
We do not have this figured out yet. `mklink` gave a permissions error.  Creating a link in Windows Explorer didn't create a link that worked at the command prompt.

## Run the script
Now we can run the script!

__MAC__ work in terminal.  __PC__ work in Anaconda Prompt

First activate the conda environment:

     conda activate textract
     
Next, run the script.  

__MAC__ with symbolic links to the Google Drive folder
     python pdf2csv.py  -o UCD2022_2023/RawCSVs/ UCD2022_2023/DataScans/*.pdf   
     # this will process ALL pdf files in `UCD2022_2023/DataScans` and create corresponding csvs in `UCD2022_2023/RawCSVs/`

__PC__ without symbolic links.  We can't get file globbing to work, so currently have to run a separate command for each file.
    Maya please put in an example command.

__IMPORTANT__ you will need to manually move the PDFs to `UCD2022_2023/DataScans-Processed/` afterwards, e.g.

     mv UCD2022_2023/DataScans/*.pdf UCD2022_2023/DataScans-Processed

Note: __Existing csvs with the same name will be overwritten__
