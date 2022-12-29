## Installations and set up python environment

    brew install graphicsmagick
    conda create -n textract python=3.10.8
    conda activate textract
    conda install -n textract boost
    pip install boto3 #aws bindings
    pip install pgmagick #grapicsmagick bindings

## Outline of steps

* split images: input PDFs output jpegs
* move jpegs to AWS bucket
* invoke textract
* download csvs if necessary; name intelligently

