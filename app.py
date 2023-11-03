import streamlit as st
from pydantic import ValidationError
from ruamel.yaml import YAML

from react_jsonform_component import SchemaError, raw_jsonform

yaml = YAML(typ="safe")
# Initial page config

st.set_page_config(
    page_title="Prompt template validator",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    cs_body()


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
        return
    schema = yaml.load(schema_file)

    try:
        data = raw_jsonform(schema=schema, key="form")
    except SchemaError as e:
        st.error("Please upload a valid jsonschema file!")
        st.error(e)
        data = None
    except ValidationError as e:
        st.error(e)
        data = None

    if data:
        st.header("Form data")
        st.write(dict(data))


if __name__ == "__main__":
    main()
