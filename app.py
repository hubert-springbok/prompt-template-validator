import streamlit as st

from react_jsonform_component import jsonform_component

# Initial page config

st.set_page_config(
     page_title='Prompt template validator',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    cs_sidebar()
    cs_body()

    return None

def cs_sidebar():
    st.header("Streamlit app to preview prompt templates")
    
def cs_body():
    schema = st.file_uploader("Upload a schema file", type=["json", "yaml"], key="schema_file", accept_multiple_files=False)
    template = st.file_uploader("Upload a template file", type=["text", "jinja2"], key="template_file", accept_multiple_files=False)

    data = jsonform_component("jsonform", {}, key='form')
    if data:
        st.header("Form data")
        st.write(data)

if __name__ == '__main__':
    main()