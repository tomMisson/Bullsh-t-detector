import React, { Component } from 'react'
const axios = require('axios');
const cheerio = require('cheerio');

export default class Result extends Component {
    
    componentDidMount(){
       if(this.props.url!==""){
            axios(this.props.url)
            .then(response => {
            const html = response.data;
            const $ = cheerio.load(html);
            const statsTable = $('.statsTableContainer > tr');
            console.log(statsTable.length);
            })
            .catch(console.error);
        
        }
    }
     
    
    render() {

        if(this.props.url !==""){
            return (
                <section>
                    <h2><a href={this.props.url} alt="link to site" target= "_blank" rel="noopener noreferrer">{this.props.url}</a></h2>
                    <h3></h3>
                </section>
            )
        }
        else{
            return (
                <div>
                
                </div>
            )
        }
    }
}
