import easyocr
import os

reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
results = []
path = r'C:\Users\Jan-FelixdeMan\experiment\lora_output\UNet0_0001TE0_0001dim4\red_hugo_logo-000027'
for img in os.listdir(r'C:\Users\Jan-FelixdeMan\experiment\lora_output\UNet0_0001TE0_0001dim4\red_hugo_logo-000027'):
    if img.endswith(".png"):
        result = reader.readtext(f'{path}/{img}', detail = 0)
        print(result)
        results.append(result)
print(results)
