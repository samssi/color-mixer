import React from 'react';
import axios from "axios";
import { SketchPicker } from 'react-color';

export default class Mixer extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      background: '#fff',
    };
  }

  callLed(color) {
    axios.post("http://192.168.10.43:5000/color", color.rgb)
        .then((response) => console.log('done'))
        .catch((error) => console.log(error));

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

