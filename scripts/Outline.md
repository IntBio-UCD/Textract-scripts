## Installations and set up python environment

    brew install graphicsmagick
    conda create -n textract python=3.10.8
    conda activate textract
    #conda install -n textract boost #only if we need graphicsmagick
    conda install -n textract poppler # needed for pdf2image
    pip install boto3 #aws bindings
    #pip install pgmagick #grapicsmagick bindings
    pip install pdf2image

## Outline of steps

* split images: input PDFs output jpegs
* move jpegs to AWS bucket
* invoke textract
* download csvs if necessary; name intelligently

