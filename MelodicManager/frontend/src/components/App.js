import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";

import Header from "./layout/Header";
import Home from "./mercenary/Home";
class App extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <div className="container">
                    <Home />
                </div>
            </Fragment>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));