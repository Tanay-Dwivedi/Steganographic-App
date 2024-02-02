import streamlit as sl
from stegano import lsb
from PIL import Image

sl.set_page_config(page_title="Steganographic App", page_icon="🧐")

sl.title("Steganographic App")
sl.write("##")

sl.write("### To make a secret image")

with sl.form("Upload your image"):
    upload_img = sl.file_uploader("Upload your image", accept_multiple_files=False)
    input_text = sl.text_input("Enter the secret text")
    img_name = sl.text_input("Enter the secret image name")
    submit_btn = sl.form_submit_button("Hide Text")

sl.write("##")


def text_to_secret_message(org_text):
    binary_representation = " ".join(format(ord(char), "08b") for char in org_text)
    return binary_representation


def secret_to_text_message(sec_text):
    binary_values = sec_text.split()
    ascii_characters = [chr(int(binary, 2)) for binary in binary_values]
    original_string = "".join(ascii_characters)
    return original_string


if submit_btn:
    sl.write("### Your secret image")
    new_img_name = img_name.replace(" ", "_")
    new_img_name = new_img_name + ".png"
    input_text = text_to_secret_message(input_text)
    secret = lsb.hide(upload_img, input_text)
    secret.save(new_img_name)
    sl.image(new_img_name)
    image = Image.open(new_img_name)
    sl.write("##")

    with open(new_img_name, "rb") as file:
        btn = sl.download_button(
            label="Download image",
            data=file,
            file_name=new_img_name,
            mime="image/png",
        )

sl.write("##")
sl.write("### To find the secret message")

with sl.form("Upload the secret image"):
    upload_img = sl.file_uploader(
        "Upload the secret image", accept_multiple_files=False
    )
    submit_btn = sl.form_submit_button("Reveal secret message")

sl.write("##")

if submit_btn:
    sl.write("### Your secret message is :")
    sl.write(f"**{secret_to_text_message(lsb.reveal(upload_img))}**")
