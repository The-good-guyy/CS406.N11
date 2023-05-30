import streamlit as st
from matplotlib import pyplot as plt
import albumentations as A

from sidebar_utils import handle_uploaded_image_file

def main():
    placeholder = st.empty()
    placeholder2 = st.empty()
    placeholder.markdown(
        "### Digital Image Processing and Applications - CS406.N11.KHCL\n"
        "| Trần Vĩ Hào - 19521482 | Tô Thanh Hiền - 19521490 | Lê Đặng Đăng Huy - 19521612 |\n"
        "#### Visualize an image augmentation pipeline\n"
        "##### Select the components of the pipeline in the sidebar.\n"
        "Once you have chosen the augmentation techniques, select or upload an image.\n"
        "Then click 'Apply' to start!\n"
    )
    placeholder2.markdown(
        "After clicking start, the individual steps of the pipeline are visualized. The ouput of the previous step is the input to the next step."
    )

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Image Augmentation Visualizer")
    main()
