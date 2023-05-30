import streamlit as st
from matplotlib import pyplot as plt
import albumentations as A

from sidebar_utils import handle_uploaded_image_file, plot_original_image, plot_modified_image

st.set_page_config(page_title="Scaling Demo", page_icon="📈")

st.markdown("# Scaling")
st.sidebar.header("Image selection")
st.write(
    """This demo shows the effects of the `Scaling` transformation and its parameters.
    Enjoy!"""
)

st.sidebar.markdown("(Optional) Upload an image file here:")
file_uploader = st.sidebar.file_uploader(label="", type=[".png", ".jpg", ".jpeg"])
st.sidebar.markdown("Or select a sample file here:")
selected_provided_file = st.sidebar.selectbox(
    label="", options=["Flower", "Dog"]
)
st.sidebar.markdown("---")
st.sidebar.header("Parameters")
limit1 = st.sidebar.slider('f(x)?', 0.0, 10.0, value=3.0)
limit2 = st.sidebar.slider('f(y)?', 0.0, 10.0, value=1.0)


import numpy as np
import cv2
def scaling(img, limit1, limit2):
        new_img = cv2.resize(img, (0, 0), fx=limit1, fy=limit2, interpolation=cv2.INTER_NEAREST)
        return new_img

@st.cache
def get_transformation(img, limit1: float, limit2: float):
    return scaling(img=img, limit1=limit1, limit2=limit2)


def run():
    global limit1, limit2
    additional_information = None
    if file_uploader is not None:
        img, additional_information = handle_uploaded_image_file(file_uploader)
    else:
        if selected_provided_file == "Dog":
            additional_information = 'Image by <a href="https://pixabay.com/users/dm-jones-9527713/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3582038">Marsha Jones</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3582038">Pixabay</a>'
            img = plt.imread("samples/dog.jpg")
        elif selected_provided_file == "Flower":
            img = plt.imread("samples/flower.jpg")
            additional_information = 'Image by <a href="https://pixabay.com/users/engin_akyurt-3656355/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3616249">Engin Akyurt</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3616249">Pixabay</a>'
    plot_original_image(img, additional_information)
    transformation = get_transformation(img=img, limit1=limit1, limit2=limit2)
    #transformed_img = transformation(image=img)["image"]
    plot_modified_image(transformation)


if st.sidebar.button("Apply"):
    run()
