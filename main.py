import streamlit as sl
from stegano import lsb
from PIL import Image

sl.title("Steganographic")

with sl.form("Upload the image"):
    upload_img = sl.file_uploader("Upload")
    input_text = sl.text_input("Enter the secret text")
    img_name = sl.text_input("Enter the secret image name")
    submit_btn = sl.form_submit_button("Hide Text")

sl.write("##")

if submit_btn:
    sl.write("### Your secret image")
    img_name = img_name + ".png"
    secret = lsb.hide(upload_img, input_text)
    secret.save(img_name)
    sl.image(img_name)
    image = Image.open(img_name)
    sl.write("##")

    with open(img_name, "rb") as file:
        btn = sl.download_button(
            label="Download image",
            data=file,
            file_name=img_name,
            mime="image/png",
        )
