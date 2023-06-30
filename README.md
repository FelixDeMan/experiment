# Fine-Tuning Stable Diffusion
This repo has most of the code I used to do my thesis on the topic of personalizing diffusion models. The experiment (1).ipynb should download all subrepos and install all the dependencies, as most of the code originates from https://github.com/Linaqruf/kohya-trainer. In this same notebooks there are examples of how to fine-tune models and generate pictures. The most user-friendly way of generating images using the models is by using Automatic1111 (https://github.com/AUTOMATIC1111/stable-diffusion-webui). 
All the models are saved to my HuggingFace account (https://huggingface.co/FelixDiffusion) together with the sample images generated.
The final presentation is added to the git as a pdf. The same will happen with my written thesis once it is finished. 

## Automatic1111
Remember, the unique token is "red_hugo_logo", please use these in your prompt!
In order to use Automatic1111 with the custom models, please make sure to download the weights for SD 1.5 (https://huggingface.co/runwayml/stable-diffusion-v1-5) and paste them in this folder: 'AUTOMATIC1111/stable-diffusion-webui/models/Stable-diffusion'. The Dreambooth models can be added to the same folder.
For LoRA models, just paste the files in 'AUTOMATIC1111/stable-diffusion-webui/models/lora'. Then insert the following phrase in the prompt: "<lora:filename:multiplier>". This page can help you if you're stuck: https://stable-diffusion-art.com/lora/
For textual inversion weights, paste them into "AUTOMATIC1111/stable-diffusion-webui/embeddings", then use the small icon next to the bin icon uner the "Generate" button to activate the embeddings.