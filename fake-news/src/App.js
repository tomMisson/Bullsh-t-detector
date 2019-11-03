import React from 'react';
import Result from './Result';
import Donald from './donald-trumpkin.png';

class App extends React.Component{

  state = {
    url:"",
    fake: false,

    reliablity:{
      text:"",
      negitive:0.0,
      neutral:0.0,
      positive:0.0
    }
  }

  collectURL = (event) => {
    if(!this.state.fake){
      this.setState({url:document.getElementById("textBox").value});
    }
    else{
      this.setState({url:"Its fake news man"});
    }
    document.getElementById("textBox").value = "";
    
    if(this.state.url!=="")
    {
      var url = "/url/"+this.state.url;
      console.log(url)
      fetch(url, {
        mode:"no-cors"
      })
      .then(res => 
        res.json()
      )
      .then(data => this.setState({reliablity:data}))
      .then(console.log(this.state.reliablity))
      .catch(err => console.log(err))
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
            <input type="submit" onClick={ this.collectURL}/>
        </main>
        <Result url={this.state.url} reliablity={this.state.reliablity}/>
      </div>
    );
  }
}
export default App;
