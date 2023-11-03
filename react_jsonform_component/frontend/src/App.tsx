import Form from "@rjsf/core";
import { RJSFSchema, UiSchema } from "@rjsf/utils";
import validator from "@rjsf/validator-ajv8";
import { ReactNode } from "react";
import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib";

const schema: RJSFSchema = {
  title: "Test form",
  type: "object",
  properties: {
    name: {
      type: "string",
    },
    age: {
      type: "number",
    },
  },
};
const uiSchema: UiSchema = {
  "ui:classNames": "custom-css-class",
};

class JsonformComponent extends StreamlitComponentBase {
  public state = { numClicks: 0, isFocused: false };
  public render = (): ReactNode => {
    // const { name } = this.props.args;
    return (
      <Form
        schema={schema}
        uiSchema={uiSchema}
        validator={validator}
        onSubmit={this._submitFormData}
      />
    );
  };
  private _submitFormData = (formData: any): void => {
    console.log({ formData });
  };
}

export default withStreamlitConnection(JsonformComponent);
