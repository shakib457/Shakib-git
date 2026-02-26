from stegano import lsb
from PIL import Image
import io
import streamlit as st

st.set_page_config(page_title='stegano project', layout='centered')

menu = st.sidebar.selectbox('choose your option',
                            ('Hiding text', 'Reveal text'))

if menu == 'Hiding text':
    uploaded_file = st.file_uploader(
        'upload your pic', type=['png', 'jpg', 'jpeg'])
    secret_msg = st.text_area('Enter your text')

    if uploaded_file and secret_msg:
        image = Image.open(uploaded_file)

        secret_img = lsb.hide(image, secret_msg)

        buffer = io.BytesIO()

        secret_img.save(buffer, format='png')
        st.success('Hiding Operation Done successfuly')

        st.download_button(
            label='download new image',
            data=buffer.getvalue(),
            mime='image/png',
            file_name='secret_image.png'
        )

elif menu == 'Reveal text':
    secret_file_upload = st.file_uploader('choose new picture', type=['png'])
    image = Image.open(secret_file_upload)

    if st.button('Extract'):

        hide_msg = lsb.reveal(image)

        if hide_msg:
            st.success('Message extract successfuly')
            st.code(hide_msg)

        else:
            st.error('picture Not found')
