import React, { ReactNode } from "react";
import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib";

import Form from "@rjsf/core";
import { RJSFSchema } from "@rjsf/utils";
import validator from "@rjsf/validator-ajv8";

const schema: RJSFSchema = {
  title: "Test form",
  type: "string",
};

class JsonformComponent extends StreamlitComponentBase {
  public state = { numClicks: 0, isFocused: false };
  public render = (): ReactNode => {
    const { theme } = this.props;
    // const { name } = this.props.args;

    const style: React.CSSProperties = {};

    // Maintain compatibility with older versions of Streamlit that don't send
    // a theme object.
    if (theme) {
      // Use the theme object to style our button border. Alternatively, the
      // theme style is defined in CSS vars.
      const borderStyling = `1px solid ${
        this.state.isFocused ? theme.primaryColor : "gray"
      }`;
      style.border = borderStyling;
      style.outline = borderStyling;
    }

    return <Form schema={schema} validator={validator} />;
  };
}

export default withStreamlitConnection(JsonformComponent);
