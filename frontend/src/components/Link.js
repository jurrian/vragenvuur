import React, { Component } from 'react'

class Link extends Component {
    render() {
        return (
            <div>
                <div>
                    {this.props.link} ({this.props.link})
                </div>
            </div>
        )
    }
}

export default Link
