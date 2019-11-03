import React from 'react';
import Result from './Result';
import Donald from './donald-trumpkin.png';

class App extends React.Component{

  state = {
    url:"",
    fake: false,

    text:"",
    negitive:0.0,
    neutral:0.0,
    positive:0.0
  }

  collectURL = (event) => {
    if(!this.state.fake){
      this.setState({url:document.getElementById("textBox").value});


      var url = "http://localhost:5000/url/"+this.state.url;
      fetch(url)
      .then(response => response.json())
      .then( console.log(response)
      )
    }
    else{
      this.setState({url:"Its fake news man"});
    }
    document.getElementById("textBox").value = "";
    
    if(this.state.url!=="")
    {
      console.log(this.state.url);
    }
  }
 
  toggleFakeNews = (event) => {
    this.state.fake = !this.state.fake
    
  }

  render() {
    return (
      <div className="App">
        <header>
          <button onClick={this.toggleFakeNews}><img alt="donald trump head" src={Donald}/></button>
        </header>
        
        <main>
          <h1>Are you getting the full story?</h1>
        
            <input type="text" id="textBox" placeholder="Text to judge"/>
            <br/>
            <input type="submit" onClick={this.collectURL}/>
        </main>
        <Result url={this.state.url}/>
      </div>
    );
  }
}
export default App;
