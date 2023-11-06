import io

import streamlit as st
from pydantic import ValidationError
from ruamel.yaml import YAML
from streamlit_rjsf import SchemaError, raw_jsonform

yaml = YAML(typ="safe")

st.set_page_config(
    page_title="Prompt template validator",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    body()


def body():
    st.header("Streamlit app to preview prompt templates")

    schema, user_data = file_pickers()
    if not schema:
        st.write("Please upload a schema file to get started")
        return

    try:
        form_data = raw_jsonform(schema=schema, user_data=user_data, key="form")
    except SchemaError as e:
        st.error("Please upload a valid jsonschema file!")
        st.error(e)
        form_data = None
    except ValidationError as e:
        st.error(e)
        form_data = None

    if form_data:
        st.header("Export your data")
        file_content = io.BytesIO()
        yaml.dump(form_data, stream=file_content)
        st.download_button(
            "Download form data as yaml",
            file_name="form_data.yaml",
            key="form_data_download",
            data=file_content,
        )


def file_pickers():
    col1, col2 = st.columns(2)

    schema_file = col1.file_uploader(
        "Upload a schema file",
        key="schema_file",
        type=["json", "yaml"],
        accept_multiple_files=False,
    )
    user_data_file = col2.file_uploader(
        "Upload your existing data (optional)",
        key="user_data_file",
        type=["json", "yaml"],
        accept_multiple_files=False,
    )
    schema = yaml.load(schema_file) if schema_file else None
    user_data = yaml.load(user_data_file) if user_data_file else None
    return schema, user_data


if __name__ == "__main__":
    main()
