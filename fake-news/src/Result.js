import React, { Component } from 'react'

export default class Result extends Component {

    render() {

        if(this.props.url !==""){
            return (
                <section>
                    <h2><a href={this.props.url} alt="link to site" target= "_blank" rel="noopener noreferrer">{this.props.url}</a></h2>
                    
                </section>
            )
        }
        if(this.props.url === "Its fake news man")
        {
            return (
                <section>
                    <h1>{this.props.url}</h1>
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
