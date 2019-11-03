import React from 'react';
import Result from './Result';

class App extends React.Component{

  state = {
    url:""
  }

  collectURL = (event) =>{
    this.setState({url:document.getElementById("textBox").value});
    document.getElementById("textBox").value = "";
    if(this.state.url!=="")
    {
      console.log(this.state.url);
      
    }
  }

  render() {
    return (
      <div className="App">
        <main>
          <h1>Are you getting the full story?</h1>
        
            <input type="text" id="textBox" placeholder="URL to news source"/>
            <br/>
            <input type="submit" onClick={this.collectURL}/>
        </main>
        <Result url={this.state.url}/>
      </div>
    );
  }
}
export default App;
