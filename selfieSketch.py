import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tempfile

st.set_page_config(page_title="Selfie on the fly", layout="wide")

st.title("*Need a quick selfie* while on your laptop? :sunglasses:")
st.subheader("*sometimes you just need that mug shot for creating your profile on the fly...*:smiley:")

def lineApp(img, lower, upper, line_color, bg_color):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(blur, lower, upper)

    colored_edges = np.zeros_like(img)
    colored_edges[np.where(edges != 0)] = line_color
    colored_edges[np.where(edges == 0)] = bg_color

    return colored_edges

col1, col2, col3, col4 = st.columns([1,1,1,1])

selfie = col1.camera_input("")

if selfie is not None:
    col2.image(selfie)
else:
    col2.write("""     
               what are you waiting for?  
               take a selfie! :smile:   
               """)

if selfie is not None:
    col2.download_button("download your selfie", selfie)
else:
    col2.download_button("take a selfie and click download", data="", disabled=True)

if selfie is not None:
    selfie_pil = Image.open(selfie).convert('RGB')
    selfie_np = np.array(selfie_pil)
    img = cv2.cvtColor(selfie_np, cv2.COLOR_RGB2BGR)
    lower_threshold = col3.slider("Lower Threshold", 0, 255, 100)
    upper_threshold = col3.slider("Upper Threshold", 0, 255, 150)
    line_color = col3.color_picker("Line Color", "#000000")
    bg_color = col3.color_picker("Background Color", "#FFFFFF")

    result = lineApp(img, lower_threshold, upper_threshold, tuple(int(line_color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)), tuple(int(bg_color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)))
    col4.image(result, caption="Line Drawing", use_column_width=True)

    if col4.button("Download Line Drawing"):
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        cv2.imwrite(temp_file.name, result)
        col4.markdown(f"[Download Line Drawing]({temp_file.name})", unsafe_allow_html=True)
else:
    col3.write("Please take a selfie.")
    col4.write("Line drawing will be displayed here.")
