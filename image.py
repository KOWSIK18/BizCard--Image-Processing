import streamlit as st
from PIL import Image
from Extract import extract
import os

def load_image(image_file):
	img = Image.open(image_file)
	return img

st.title('BizCardX-Image Processing')
st.header("Image Processing")
image_file = st.file_uploader("Upload Images", type= ["png","jpg","jpeg"])

if image_file is not None:
        a = load_image(image_file)
        st.image(a)
        option = st.radio('To Extract Text from Image :',('','Yes','No'))
        if option == 'Yes':
            extract(image_file.name)
        elif option == 'No':
                st.write('Thank You!')
        else:
                st.write('')
        st.write('Press button to insert the extracted data with Image in DB')
        if st.button('Insert'):
               insert(image_file.name)


    



             


