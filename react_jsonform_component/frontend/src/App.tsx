import Form from "@rjsf/core";
import validator from "@rjsf/validator-ajv8";
import { ReactNode } from "react";
import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib";

interface Args {
  schema: any;
  uiSchema: any;
}
class JsonformComponent extends StreamlitComponentBase {
  public state = { formData: null };
  public render = (): ReactNode => {
    const { schema, uiSchema }: Args = this.props.args;
    return (
      <Form
        schema={schema}
        validator={validator}
        uiSchema={uiSchema}
        onSubmit={this._submitFormData}
      />
    );
  };
  private _submitFormData = (formData: any): void => {
    Streamlit.setComponentValue({
      errors: formData.errors,
      formData: formData.formData,
      schemaValidationErrors: formData.schemaValidationErrors,
    });
  };
}

export default withStreamlitConnection(JsonformComponent);
