import json

import streamlit as st
from pydantic import BaseModel, Field, ValidationError

from react_jsonform_component import pydantic_jsonform, raw_jsonform

# Initial page config

st.set_page_config(
    page_title="Prompt template validator",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    cs_body()


class Form(BaseModel):
    age: int = Field(..., gt=0, lt=115)
    name: str = Field(default="", max_length=20)


def cs_body():
    st.header("Streamlit app to preview prompt templates")
    schema_file = st.file_uploader(
        "Upload a schema file",
        key="schema_file",
        type=["json", "yaml"],
        accept_multiple_files=False,
    )
    if not schema_file:
        st.write("Please upload a schema file to get started")
        pydantic_jsonform(schema=Form, key="pydantic_form")
        return
    schema = json.load(schema_file)

    try:
        data = raw_jsonform(schema=schema, key="form")
    except ValidationError as e:
        st.error(e)
        data = None

    if data:
        st.header("Form data")
        st.write(dict(data))


if __name__ == "__main__":
    main()
