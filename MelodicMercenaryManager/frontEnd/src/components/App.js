import React, { Component } from 'react';
import ReactDOM from 'react-dom';

// front end react app

class App extends Component {
    render() {
        return <h1>React App</h1>
    }
};

// makes the app into an html element
ReactDOM.render(<App />, document.getElementById('app'))