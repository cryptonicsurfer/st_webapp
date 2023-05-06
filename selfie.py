import streamlit as st

st.set_page_config(page_title="Selfie on the fly", layout="wide")

st.title("*Need a quick selfie* while on your laptop? :sunglasses:")
st.subheader("*sometimes you just need that mug shot for creating your profile on the fly...*:smiley:")

col1, col2, col3, col4 = st.columns([1,1,1,1])
selfie =col1.camera_input("")

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

