import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


# function to get response from LLAma 2 Model
def getLLamaresponse(input_text, no_words, blog_style):

    # Llama2 model
    llm = CTransformers(model='D:/Internship - Generative AI/Blog Generation/models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})

    # prompt template
    template = f"""
    Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
    """

    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                            template=template)

    # generate response from the LLama 2 model
    response = llm(prompt.format(style=blog_style, text=input_text, n_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Generate Blogs",
                   page_icon="🤖",
                   layout="centered",
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

# creating two more columns for additional two fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input("Number of words")

with col2:
    blog_style = st.selectbox("Writing the blog for", ("Researchers", "Data Scientist", "Common People"), index=0)

submit = st.button("Generate")

# final response
if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))
