import React, { Component } from 'react'

export default class Result extends Component {

    render() {

        if(this.props.url !==""){
            return (
                <section>
                    <h4>{this.props.url}</h4><br/>
                    <p>Positive: {this.props.reliablity.positive}</p><br/>
                    <p>Neutral: {this.props.reliablity.neutral}</p><br/>
                    <p>Negative: {this.props.reliablity.negative}</p><br/>
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
