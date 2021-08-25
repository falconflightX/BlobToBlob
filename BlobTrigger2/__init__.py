import os,io

from io import BytesIO
import logging

import azure.functions as func
import pandas as pd

def main(blobin: func.InputStream, blobout: func.Out[bytes], context: func.Context):

    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {blobin.name}\n"
                 f"Blob Size: {blobin.length} bytes")

    ## Reading the text file
    
    
    df = pd.read_csv(BytesIO(blobin.read()))

    logging.info(f"Loaded textfile \n")
    
    df.columns = ['Name', 'Type', 'email']

    # storing this dataframe in a csv file
    output_data = df.to_csv()
       
    blobout.set(output_data)