import streamlit as st
from stegano import lsb
from PIL import Image
import base64
import io

st.set_page_config(page_title="Image in Image Steganography", page_icon="🖼️")

st.title("🖼️ pic in pic")

menu = st.sidebar.selectbox(
    "choose option",
    ["Hide", "Reveal"]
)

# -------------------------------------------------
# 🔐 Hide Image Inside Image
# -------------------------------------------------
if menu == "Hide":

    cover_file = st.file_uploader("host pic", type=["png"])
    secret_file = st.file_uploader("guest pic", type=["png"])

    if cover_file and secret_file:

        cover_img = Image.open(cover_file).convert("RGB")
        secret_img = Image.open(secret_file)

        buffer = io.BytesIO()
        secret_img.save(buffer, format="PNG")
        secret_bytes = buffer.getvalue()

        secret_base64 = base64.b64encode(secret_bytes).decode()

        if st.button("🔒 Hide Pic"):

            encoded_img = lsb.hide(cover_img, secret_base64)

            result_buffer = io.BytesIO()
            encoded_img.save(result_buffer, format="PNG")

            st.success("Done!")

            st.download_button(
                "📥 Download New Pic",
                result_buffer.getvalue(),
                "Hidden_image.png",
                "image/png"
            )

# -------------------------------------------------
# 🔎 Reveal Hidden Image
# -------------------------------------------------
elif menu == "Reveal":

    encoded_file = st.file_uploader("", type=["png"])

    if encoded_file:

        encoded_img = Image.open(encoded_file)

        if st.button("📖Extract"):

            hidden_data = lsb.reveal(encoded_img)

            if hidden_data:

                image_bytes = base64.b64decode(hidden_data)

                secret_image = Image.open(io.BytesIO(image_bytes))

                st.success('extract sucessfully')
                st.image(secret_image)

            else:
                st.error("No picture found")
