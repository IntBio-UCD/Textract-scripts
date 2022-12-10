# Textract-scripts
Notes and scripts for interacting with AWS Textract to process hand written data sheets

AWS's documentation is [here](https://docs.aws.amazon.com/textract/index.html)

If you're using the AWS CLI, you can't pass image bytes to Amazon Textract operations. Instead, you must reference an image stored in an Amazon S3 bucket.

Also AWS CLI returns JSON not csv

So...it looks like developing an app from the examply Python code is the way to go...

Note that if we need to breakdown the PDFs in to individual files we can use [ImageMagick](https://wiki.python.org/moin/ImageMagick) (python or command line)
