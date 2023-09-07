import streamlit as st
import base64
import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import ResponseSchema ,StructuredOutputParser
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
# os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

# Initialize chat model
chat_llm = ChatOpenAI(temperature=0.0)
def generator(context,function,language,outcome_expected):
    title_template = """You are Computer Programming Expert ,
                    Provide a code for "{context}" in "{language}".
                    it should perform these "{function}" and result should be look like "{outcome_expected}".
                    """ 
    
    prompt = ChatPromptTemplate.from_template(template=title_template)
    messages = prompt.format_messages(context=context,function=function,language=language,outcome_expected=outcome_expected)
    response = chat_llm(messages)
    content = str(response.content)
    st.write(content)
    pass


def main():
    st.title("👨‍💻 Code Generation")
    
    # Text Input Fields
    context = st.text_area("Context", "")
    function = st.text_input("Function", "")
    language = st.text_input("Language", "")
    outcome_expected = st.text_area("Outcome Expected", "")
    
    # Submit Button
    if st.button("Submit"):
        st.write("Submitted Data:")
        generator(context,function,language,outcome_expected)

if __name__ == "__main__":
    main()
