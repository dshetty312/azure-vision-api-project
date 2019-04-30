"""
Python client code to connect to computer vision api and extract tag information
- Dikshith Shetty
"""


from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

# Get endpoint and key from environment variables
import os
endpoint = os.environ['ACCOUNT_ENDPOINT']
key = os.environ['ACCOUNT_KEY']

# Set credentials
credentials = CognitiveServicesCredentials(key)

# Create client
client = ComputerVisionClient(endpoint, credentials)

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"

domain = "landmarks"
url = "http://www.public-domain-photos.com/free-stock-photos-4/travel/san-francisco/golden-gate-bridge-in-san-francisco.jpg"
language = "en"
max_descriptions = 3

analysis = client.describe_image(url, max_descriptions, language)

print("Printing text information with confidence for the golden gate image:\n")

for caption in analysis.captions:
    print(caption.text)
    print(caption.confidence)


print('\n')

print("Printing tag information for the golden gate image:\n")
image_analysis = client.analyze_image(url,visual_features=[VisualFeatureTypes.tags])

print(type(image_analysis))
print('\n')

keyList=[]
for tag in image_analysis.tags:
    print(tag.name)
    keyList.append(tag.name)

print(type(image_analysis.tags))
print("Image -> %s and list of tags -> %s"%(url,keyList))

"""
This code prints domain information like landmarks or celebrity
print("Printing model information:\n")
models = client.list_models()

for x in models.models_property:
    print(x)
"""
