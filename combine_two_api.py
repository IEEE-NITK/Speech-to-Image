# -*- coding: utf-8 -*-
"""combine two api

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GiW-hV2wBGuusO9yRP8mfVlgkEh4oE1d
"""

pip install openai
pip install whisper
pip install -U openai-whisper

import openai
import whisper
import requests
from PIL import Image
#Change the variable API_KEY with global variable of your API_KEY
openai.api_key = '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'
model = whisper.load_model("base")
audio = whisper.load_audio("/content/audio.unknown")
audio = whisper.pad_or_trim(audio)
mel = whisper.log_mel_spectrogram(audio).to(model.device)
_, probs = model.detect_language(mel)
options = whisper.DecodingOptions(fp16 = False)
result = whisper.decode(model, mel, options)
print(result.text)
response = openai.Image.create(prompt = f"{result.text}", n = 1 , size = "1024x1024")
image_url = response['data'][0]['url']
img = Image.open(requests.get(f"{image_url}",stream = True).raw)
img.show()