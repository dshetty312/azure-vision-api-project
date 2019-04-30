#Created by - Dikshith S shetty
import requests
import time
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
#import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Replace <Subscription Key> with your valid subscription key.
subscription_key = "3cd70cd09bf7461b9faa9d8e28735dc7"

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the "westus" region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
#vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"
vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v2.0/"

analyze_url = vision_base_url + "analyze"
import json
import glob
headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
              'Content-Type': 'application/octet-stream'}

params     = {'visualFeatures': 'Categories,Description,Color'}

files=glob.glob("/home/azureuser/dikshith/input/*.jpg")
print("Number of images processed:%d"%(len(files)))
counter=0#batch size of 20 calls per minute
for i in files:
    counter+=1
    if counter % 20 == 0:
        time.sleep(60)

    image_data = open(i, "rb").read()
    response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()
    analysis = response.json()
    out=json.dumps(analysis)

    data = json.loads(out) #data becomes a dictionary
    data['image_path'] = "https://cumulusstoragetest.blob.core.windows.net/input/"+i.split("/")[5]
    filepath="/home/azureuser/dikshith/json-input/" +"image-tag-"+i.split("/")[5]
    print(filepath+".json")
    with open('%s.json' % filepath,'w') as f:
        f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
print("Json output at location:/home/azureuser/dikshith/json-input")
