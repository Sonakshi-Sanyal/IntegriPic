import streamlit as st

st.set_page_config(layout="wide")
st.title("IntegriPic")


tab1, tab2, tab3 = st.tabs(["Home", "About Us", "Upload Image"])
with tab1:
    st.header("Home Page")
    col1, col2 = st.columns(2)

with col1: 
    st.header("STOP PIRATED PICTURES!!! ")
#   st.header("_Streamlit_ is :blue[cool] :smile:")
    st.write("Reality or illusion? Know the difference. Authentic images reflect truth, while AI-generated ones deceive. Don't be fooled – verify the source, demand transparency, and seek the truth.")
    st.button("Submit")
    file=st.file_uploader("Upload ig")
    st.image("https://cdn.pixabay.com/photo/2024/02/28/07/42/european-shorthair-8601492_1280.jpg")



with col2:
    st.image("https://news.ubc.ca/wp-content/uploads/2023/08/AdobeStock_559145847.jpeg")
    st.image("https://cdn.pixabay.com/photo/2024/02/28/07/42/european-shorthair-8601492_1280.jpg")
    #st.image("C:/Users/Lenovo/Documents/Sonakshi/Python/Academy/Test images to detect before/catai")
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
   # file2=st.file_uploader("Upload img")



    st.write("Please enter your name")
    st.text_input("Your name", key="name")

# You can access the value at any point with:
    st.session_state.name
