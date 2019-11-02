import React, { Component } from 'react'

export default class Result extends Component {
    
    
    
    render() {

        if(this.props.url !==""){
            return (
                <section>
                    <h2><a href={this.props.url} target= "_blank">{this.props.url}</a></h2>
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
