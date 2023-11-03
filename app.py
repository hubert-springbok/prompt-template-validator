import streamlit as st
from pydantic import BaseModel, Field, ValidationError

from react_jsonform_component import pydantic_jsonform

# Initial page config

st.set_page_config(
    page_title="Prompt template validator",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    cs_sidebar()
    cs_body()

    return None


def cs_sidebar():
    st.header("Streamlit app to preview prompt templates")


class Form(BaseModel):
    age: int = Field(..., gt=0, lt=115)
    name: str = Field(default="", max_length=20)


def cs_body():
    # schema = st.file_uploader(
    #     "Upload a schema file",
    #     type=["json", "yaml"],
    #     key="schema_file",
    #     accept_multiple_files=False,
    # )
    # template = st.file_uploader(
    #     "Upload a template file",
    #     type=["text", "jinja2"],
    #     key="template_file",
    #     accept_multiple_files=False,
    # )

    try:
        data = pydantic_jsonform(schema=Form, key="form")
    except ValidationError as e:
        st.error(e)
        data = None

    if data:
        st.header("Form data")
        st.write(dict(data))


if __name__ == "__main__":
    main()
