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
ts=datetime.datetime.now()
def dataframe_generator(nameStartsWith,APIKEY=None,Hash=None):
    global df
    if APIKEY is None or Hash is None:
        raise Exception("Expected arguments!!!")
    else:
        request_url = 'http://gateway.marvel.com/v1/public/characters'
        params ={'ts':ts,'apikey':APIKEY,'hash':Hash,
          'nameStartsWith':nameStartsWith,'limit':100}
        response = requests.get(request_url,params=params)
        data_1 =response.json()
        df = pd.json_normalize(data_1,record_path=['data','results'])
        df_new=df[['name','id','comics.available','stories.available',
                       'events.available','series.available']]
        return df_new