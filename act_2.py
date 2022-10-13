import requests
import json
import hashlib
import pandas as pd
import datetime
import string
from pprint import pprint as pp
import time
from pandas import json_normalize
import os
import argparse
ts=datetime.datetime.now()
parser = argparse.ArgumentParser(description='provide api and private key')
parser.add_argument('api_key',type=str,help='provide public key')
parser.add_argument('private_key',type=str,help='provide private key')
args=parser.parse_args()
public_key=getattr(args,'api_key')
private_key=getattr(args,'private_key')
def hash_params():
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{ts}{private_key}{public_key}'.encode('utf-8'))
    hash_params = hash_md5.hexdigest()
    return hash_params
