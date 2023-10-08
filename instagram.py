GIVEN - 
1. Instagram Page description
2. Interval

import os
from dotenv import load_dotenv
import openai

OPENAI_KEY = os.getenv("OPENAI_KEY")

def generate_instagram_image_url(desc: str):

    prompt = to chatgpt -> generate a detailed 500 character description for an image in instagram page about $(desc)

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    image_url = response['data'][0]['url']

    # INV : image is an image that fits the instagram aspect ratio

    return image_url
    
def generate_caption(desc: str):

    # INV : caption is the caption created using chatGPT

    return caption

def instagram_api_post(image, caption: str):

    Using the instagram API, add the image to instagram

    # status determines that status of the post request

    return status


def single_post(desc: str):
    image_url = generate_instagram_image_url(desc)
    caption = generate_caption(desc)

    status = instagram_api_post(image_url, caption)

every INTERVAL seconds:
    if total images posted today >= 50:
        break
    else:
        post(desc)