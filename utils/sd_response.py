import io
import base64
import requests

def response_generate(prompt, image, wight, height):
    img_bytes = image

    img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')

    img2img_payload = {
        "init_images": [img_base64],
        "prompt": prompt,
        "negative_prompt": "bad picture, bad light",
        "width": f"{wight}",
        "height": f"{height}",
        "samples": "1",
        "num_inference_steps": "50",
        "safety_checker": "no",
        "enhance_prompt": "yes",
        "guidance_scale": 5,
        "strength": 0.6,
        "seed": None,
        "webhook": None,
        "track_id": None
    }
    
    url=""
    
    img2img_response = requests.post(url=f'{url}/sdapi/v1/img2img', json=img2img_payload)

    r = img2img_response.json()

    for i in r['images']:
        image = io.BytesIO(base64.b64decode(i.split(",", 1)[0]))

    return image
