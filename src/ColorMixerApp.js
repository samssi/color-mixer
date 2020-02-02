import React from "react";
import "./main.css";
import Mixer from "./components/Mixer";

export default class ColorMixerApp extends React.Component {
  render() {
    return (
      <div>
        <Mixer />
      </div>
    );
  }
}
