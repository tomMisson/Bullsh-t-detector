import React, { Component } from 'react'

export default class Result extends Component {

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
