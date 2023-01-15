# import libraries
import os
import openai
from speechToText import *
from requests_python_img_dl import *

openai.api_key = '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'
openai.Model.list()

response = openai.Image.create(
  prompt=text,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

file_name = input('Save image as (string):')

download_image(image_url, 'images/', file_name)