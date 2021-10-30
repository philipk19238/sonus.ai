import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      message: null,
    };
  }

  componentDidMount() {
    fetch("http://localhost:5000/api/hello-world")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            message: result.message,
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error,
          });
        }
      )
  }

  render() {
    const {error, isLoaded, message} = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <ul>
          {message}
        </ul>
      );
    }
  }
}


ReactDOM.render(
  <App/>,
  document.getElementById('root')
);