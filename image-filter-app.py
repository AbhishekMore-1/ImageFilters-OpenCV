# -*- coding: utf-8 -*-
# Import required libraries

import cv2
import numpy as np
import streamlit as st
import requests
import os

# Home UI 

def main():

    st.set_page_config(layout="wide")

    font_css = """
    <style>
    button[data-baseweb="tab"] {
    font-size: 26px;
    }
    </style>
    """

    st.write(font_css, unsafe_allow_html=True)

    tabs = st.tabs(('About Me','Average Filter', 'Median Filter', 'Gaussian Filter', 'Salt & Pepper Noise'))

    # UI Options 
    with tabs[0]:
        aboutMe() 
    with tabs[1]:
        averageFilter()
    with tabs[2]:
        medianFilter()
    with tabs[3]:
        gaussianFilter()
    with tabs[4]:
        saltNpepper()

# Pre-process Image
def preProcessImg(img):
    # Pre-processing image: resize image
    height, width, _ = img.shape
    width = int(480/height*width)
    height = 480
    img = cv2.resize(img,(width,height))
    return img

# Upload Image
def uploadImage(key):

    uploaded_file = st.file_uploader("Choose a Image file",key=key)
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        # Pre-processing image: resize image
        return preProcessImg(img)
    
    return cv2.cvtColor(preProcessImg(cv2.imread('sample.jpg')),cv2.COLOR_BGR2RGB)

# About Me UI 

def aboutMe():
    
    st.markdown(requests.get(os.getenv('ABOUT_ME','https://raw.githubusercontent.com/AbhishekMore-1/AbhishekMore-1/main/README.md')).text, unsafe_allow_html=True)

# Average Filter 

def averageFilter():

    st.header("Average Filter")

    img = uploadImage(0)

    selected_box = st.selectbox(
    'Choose one of the following',
    ('3x3 Kernel','5x5 Kernel','11x11 Kernel','15x15 Kernel'),
    key=4
    )

    originalImg, filteredImg = st.columns(2)

    with originalImg:
        # Original Image
        st.subheader("Original Image")
        st.image(img,use_column_width=True)

    with filteredImg:    
        st.subheader("Filtered Image")

        if selected_box == '3x3 Kernel':
            img_blur = cv2.blur(src=img, ksize=(3,3))
            st.image(img_blur,use_column_width=True)

        if selected_box == '5x5 Kernel':
            img_blur = cv2.blur(src=img, ksize=(5,5))
            st.image(img_blur,use_column_width=True)

        if selected_box == '11x11 Kernel':
            img_blur = cv2.blur(src=img, ksize=(11,11))
            st.image(img_blur,use_column_width=True)

        if selected_box == '15x15 Kernel':
            img_blur = cv2.blur(src=img, ksize=(15,15))
            st.image(img_blur,use_column_width=True)

# Median Filter 

def medianFilter():

    st.header("Median Filter")

    img = uploadImage(1)

    selected_box = st.selectbox(
    'Choose one of the following',
    ('3x3 Kernel','5x5 Kernel','11x11 Kernel','15x15 Kernel'),
    key=5
    )

    originalImg, filteredImg = st.columns(2)

    with originalImg:
        # Original Image
        st.subheader("Original Image")
        st.image(img,use_column_width=True)

    with filteredImg:
        st.subheader("Filtered Image")

        if selected_box == '3x3 Kernel':
            img_blur = cv2.medianBlur(src=img, ksize=3)
            st.image(img_blur,use_column_width=True)

        if selected_box == '5x5 Kernel':
            img_blur = cv2.medianBlur(src=img, ksize=5)
            st.image(img_blur,use_column_width=True)

        if selected_box == '11x11 Kernel':
            img_blur = cv2.medianBlur(src=img, ksize=11)
            st.image(img_blur,use_column_width=True)

        if selected_box == '15x15 Kernel':
            img_blur = cv2.medianBlur(src=img, ksize=15)
            st.image(img_blur,use_column_width=True)



# Gaussian Filter 

def gaussianFilter():

    st.header("Gaussian Filter")

    img = uploadImage(2)

    selected_box = st.selectbox(
    'Choose one of the following',
    ('3x3 Kernel','5x5 Kernel','11x11 Kernel','15x15 Kernel'),
    key=6
    )

    originalImg, filteredImg = st.columns(2)

    with originalImg:
        # Original Image
        st.subheader("Original Image")
        st.image(img,use_column_width=True)

    with filteredImg:
        st.subheader("Filtered Image")

        if selected_box == '3x3 Kernel':
            img_blur = cv2.GaussianBlur(src=img, ksize=(3,3),sigmaX=0, sigmaY=0)
            st.image(img_blur,use_column_width=True)

        if selected_box == '5x5 Kernel':
            img_blur = cv2.GaussianBlur(src=img, ksize=(5,5),sigmaX=0, sigmaY=0)
            st.image(img_blur,use_column_width=True)

        if selected_box == '11x11 Kernel':
            img_blur = cv2.GaussianBlur(src=img, ksize=(11,11),sigmaX=0, sigmaY=0)
            st.image(img_blur,use_column_width=True)

        if selected_box == '15x15 Kernel':
            img_blur = cv2.GaussianBlur(src=img, ksize=(15,15),sigmaX=0, sigmaY=0)
            st.image(img_blur,use_column_width=True)


# Add Salt & Pepper Noise 
# Add Noise Function 

def add_noise(img):
    import random
    # Getting the dimensions of the image
    row , col = img.shape
     
    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
       
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
         
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
         
        # Color that pixel to white
        img[y_coord][x_coord] = 255
         
    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
       
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
         
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
         
        # Color that pixel to black
        img[y_coord][x_coord] = 0
         
    return img

# Noised Image with Average, Median, Gaussian filter 

def saltNpepper():

    st.header("Gaussian Filter")

    img = uploadImage(3)

    selected_box = st.selectbox(
    'Choose one of the following',
    ('Average Filter', 'Median Filter', 'Gaussian Filter'),
    key=7
    )

    originalImg, filteredImg = st.columns(2)

    with originalImg:
    # Original Image
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        noised_img = add_noise(img_gray)
        st.subheader("Salt & Pepper Noised Image")
        st.image(noised_img,use_column_width=True)

    with filteredImg:
        st.subheader("Filtered Image")

        if selected_box == 'Average Filter':
            # Average Filter
            img_blur = cv2.blur(src=noised_img, ksize=(5,5))
            st.image(img_blur,use_column_width=True)
        if selected_box == 'Median Filter':
            # Median Filter
            img_blur = cv2.medianBlur(src=noised_img, ksize=5)
            st.image(img_blur,use_column_width=True)
        if selected_box == 'Gaussian Filter':
            # Gaussian Filter
            img_blur = cv2.GaussianBlur(src=noised_img, ksize=(5,5),sigmaX=0, sigmaY=0)
            st.image(img_blur,use_column_width=True)

if __name__ == "__main__":
    main()