import requests
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

# Set image_path to the local path of an image that you want to analyze.
#image_path = "C:/Documents/ImageToAnalyze.jpg"
image_path="/home/azureuser/dikshith/golden-gate-bridge-in-san-francisco.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
              'Content-Type': 'application/octet-stream'}
params     = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
#print(analysis)
#image_caption = analysis["description"]["captions"][0]["text"].capitalize()
#image_tag=analysis["description"]["tags"]
#print(image_caption)

#print('\n')

#print(image_tag)
#print('\n')

#Converting object to json at tag level
import json
out=json.dumps(analysis)
data = json.loads(out) #data becomes a dictionary

data['image_path'] = 'https://cumulusstoragetest.file.core.windows.net/input/golden-gate-bridge-in-san-francisco.jpg'
with open("/home/azureuser/dikshith/test1json",'w') as f:
    f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))

#print(out)
