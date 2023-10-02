from yolo_opencv import output_label
import openai

openai.api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

TOKEN = 3000

def chatgpt_api_call(image_path, prompt=""):
    lines = ""
    with open('prompt.txt') as f:
        lines = f.readlines()

    if len(prompt) == 0:
        label = output_label(image_path)
        hint = lines
        print("IMAGE MODE")
        print("Image recgonised as:" + label)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "What is {} in Japan? {}".format(label, hint)},
            ],
            max_tokens=TOKEN
        )
        output = response.choices[0]["message"]["content"].strip()
    else:
        print("PROMPT MODE")
        hint = lines
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "{}{}".format(prompt, hint)},
            ],
            max_tokens=TOKEN
        )
        output = response.choices[0]["message"]["content"].strip()
        
    return output
