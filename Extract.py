import streamlit as st
import matplotlib.pyplot as plt
import cv2
import easyocr
import pylab
from IPython.display import Image
plt.rcParams['figure.figsize'] = 8,16
reader = easyocr.Reader(['en'])
def extract(img):
    output = reader.readtext(img)
    l = []
    for i in range(len(output)):
        l.append(output[i][1])
    name=[]
    num=[]
    mail=[]
    website=[]
    address=[]
    for i in range(len(l)):
        if i == 0 or i==len(l)-1:
            name.append(l[i])
        elif i == 1:
            des = l[i]
        elif '-' in l[i]:
            num.append(l[i])
        elif '@' in l[i]:
            mail.append(l[i])
        elif '.com' in l[i]:
            website.append(l[i])
        else:
            address.append(l[i])
    st.write('Extracted Infromation from the uploaded Image : \n')  
    st.write('Name : ',*name)
    st.write('Designation : ',des)
    st.write('Contact Number : ',*num)
    st.write("Mail-id : ",*mail)
    st.write('Website-URL : ', *website)
    st.write('Address : ',*address)