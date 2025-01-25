import streamlit as st
from ultralytics import YOLO
from PIL import Image
# Load the model
@st.cache_resource
def models():
    mod = YOLO('best.pt')
    return mod
st.set_page_config(layout="wide")
st.title("IntegriPic")
    

tab1, tab2, tab3 = st.tabs(["Home", "About Us", "Upload Image"])
with tab1:
    st.header("Welcome to IntegriPic!")
    st.header("STOP PIRATED PICTURES!!! ")
    
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

with col1: 
    
#   st.header("_Streamlit_ is :blue[cool] :smile:")
    st.write("Reality or illusion? Know the difference. Authentic images reflect truth, while AI-generated ones deceive. Don't be fooled – verify the source, demand transparency, and seek the truth.")
    
    #file=st.file_uploader("Upload ig") 
    # Image uploader and analyze button
with st.container():
    img = st.file_uploader('Upload your image', type=['jpg', 'png', 'jpeg'])
    analyse = st.button('Analyze')

    if analyse:
        if img is not None:
            img = Image.open(img)
            st.markdown('Image Visualization')
            st.image(img)
            model = models()
            res = model.predict(img)
            label = res[0].probs.top5
            conf = res[0].probs.top5conf
            conf = conf.tolist()
            st.write('Detected: ' + str(res[0].names[label[0]].title()))        
            st.write('Confidence level: ' + str(conf[0]))



# with col2:
#     st.image("https:/news.ubc.ca/wp-content/uploads/2023/08/AdobeStock_559145847.jpeg")

with col3:
    st.image("https://cdn.pixabay.com/photo/2024/02/28/07/42/european-shorthair-8601492_1280.jpg", caption="AI Generated Cat", width=500, use_container_width=False)
    st.image("https://cdn.pixabay.com/photo/2024/02/28/07/42/european-shorthair-8601492_1280.jpg", caption="AI Generated Cat", width=500, use_container_width=False)
with col4:
    st.image("catai.png", caption="Real Image of Cat", width=500, use_container_width=False)


with tab2:
    st.header("Learn About IntegriPic!")
    st.header("STOP PIRATED PICTURES!!! ")
    st.write("IntegrePic is a web app that differenciates between AI-generated images and authentic images. IntegriPic delivers a result with 50% accurary.")
    st.write("It has a dataset of around 3000 images that are used to train the AI model. It is in it's beta version now. Try out IntegriPic to upload an image and it let's you know if it's AI generated or Real")
    
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    file2=st.file_uploader("Upload img")



    st.write("Please enter your name")
    st.text_input("Your name", key="name")

# You can access the value at any point with:
    st.session_state.name
