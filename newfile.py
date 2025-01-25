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


#with col2:
    #st.image("itry.jpeg")

with col3:
    st.image("https://cdn.pixabay.com/photo/2024/02/28/07/42/european-shorthair-8601492_1280.jpg", caption="Real Image of Cat", width=500, use_container_width=False)
    st.image("itry.jpeg", width=500, use_container_width=False)
with col4:
    st.image("catai.png", caption="AI Generated Cat", width=500, use_container_width=False)


with tab2:
    st.header("Learn About Us!")
    st.write("IntegrePic is a web app that differenciates between AI-generated images and authentic images. IntegriPic delivers a result with high accurary.")
    st.write("It has a dataset of around 3000 images that are used to train the AI model. It is in it's beta version now. Try out IntegriPic to upload an image and it let's you know if it's AI generated or Real")
    st.header("How does IntegriPic work?")
    st.write("IntegrePic is an AI image detector. It works by analyzing an image for patterns and characteristics that are typically found in AI-generated images.")
    st.write("Like unusual textures, inconsistent lighting, or digital artifacts, comparing them to a database of known REAL images to determine if the image is likely generated by an AI model.")
    st.write("Essentially, they learn to identify the telltale signs of AI-created imagery by analyzing pixel data and identifying irregularities that would not naturally occur in a real photograph.")
    #st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    
    st.header("Technology IntegriPic uses to detect Images")
    st.header("Machine Learning:")
    st.write("IntegriPic uses machine learning algorithms trained on large datasets of both real and AI-generated images to identify patterns that distinguish between the two.")
    st.header("Pixel Analysis:")
    st.write("The detector examines the pixel arrangement within an image, looking for anomalies like unnatural gradients, sharp edges, or repetitive patterns that might indicate AI generation.")
    st.header("Feature Extraction:")
    st.write("It extracts specific features from an image like texture, color distribution, and edge sharpness to analyze if they align with typical characteristics of AI-generated images.")
    st.header("Comparison to Training Data:")
    st.write("The extracted features are compared to the detector's training data to determine the likelihood of the image being AI-generated.")
    
    st.write("")
    
with tab3:
    st.header("Upload your image here!")
    st.write("Upload your image by brwosing an image file (JPEG, PNG) and submit the Upload button. Your image will be displayed infront of you.")
    st.write("Now submit the Analyze button.")
    #file2=st.file_uploader("Upload img")



    st.write("Please enter your name")
    st.text_input("Your name", key="name")

# You can access the value at any point with:
    st.session_state.name
