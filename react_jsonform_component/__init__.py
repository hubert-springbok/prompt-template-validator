from pathlib import Path
from typing import TypeVar

import streamlit.components.v1 as components
from pydantic import BaseModel, ValidationError

COMPONENT_NAME = "react_jsonform_component"

_RELEASE = False
if not _RELEASE:
    # Serve the npm server directly to get hot reloading.
    _component_func = components.declare_component(
        COMPONENT_NAME,
        url="http://localhost:3000",
    )
else:
    # Serve static build files
    here = Path(__file__).parent.absolute()
    build_dir = here / "frontend/build"
    _component_func = components.declare_component(COMPONENT_NAME, path=str(build_dir))


Schema = TypeVar("Schema", bound=BaseModel)


class FormData(BaseModel):
    errors: list = []
    formData: dict = {}
    schemaValidationErrors: list = []


def pydantic_jsonform(
    schema: type[Schema], ui_schema: dict = {}, key: str | None = None
) -> None | Schema:
    """Render a web form corresponding to a pydantic model."""
    schema_dict = schema.model_json_schema()
    data = raw_jsonform(schema_dict, ui_schema, key)
    if data is None:
        return None
    return schema.model_validate(data)


def raw_jsonform(
    schema: dict, ui_schema: dict = {}, key: str | None = None
) -> None | dict:
    """Render a web form using a json schema."""
    component_value = _component_func(
        schema=schema,
        uiSchema=ui_schema,
        key=key,
        default=None,
        height=None,
    )
    if component_value is None:
        print("Not submitted yet!")
        return None

    data = FormData.model_validate(component_value)
    if data.errors:
        raise ValidationError.from_exception_data("Invalid form data", data.errors)
    return data.formData
