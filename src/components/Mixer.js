import React from 'react';
import { SketchPicker } from 'react-color';

export default class Mixer extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      background: '#fff',
    };
  }

  callLed(color) {
    console.log(`Calling Led with ${JSON.stringify(color.rgb)}`)
  }

  handleChangeComplete(color) {
    this.setState({ background: color.hex });
    this.callLed(color);
  };

  render() {
    return (
        <SketchPicker
            color={ this.state.background }
            onChangeComplete={ (color) => this.handleChangeComplete(color) }
        />
    );
  }
}

