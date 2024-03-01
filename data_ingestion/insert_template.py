import pandas as pd
import requests

# Putting down your End Point of AWS
# URL of your endpoint
URL = "https://319eb87oog.execute-api.us-east-2.amazonaws.com/beta/test"


# read the testfile
data = pd.read_csv('data_ingestion/testdata.csv', sep=',')

# write all the rows from the testfile to the api as put request
for i in data.index:
    try:
        # convert the row to json
        export = data.loc[i].to_json()

        # send it to the api
        response = requests.post(URL, data=export)

        # print the returncode
        # print(export)
        print(response)
    except:
        print(data.loc[i])
