from chat_gpt_api import chatgpt_api_call
import cv2


def main():
    image_path = "toilet.jpg" #mode 1: imgae
    prompt = "" #mode 2: user input
    chatgpt_api_call(image_path, prompt)


if __name__ == "__main__":
    main()
