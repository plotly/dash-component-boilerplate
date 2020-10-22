import React, {Component} from 'react';
import PropTypes from 'prop-types';

export default class dashapitokenconsumer extends Component {
    constructor(props) {
        super(props);
        this.state = { token: 'no token' }
    }

    componentDidMount() {
        window.addEventListener("message", (event) => {
            console.log('@R Debug event from origin: ', event);
            if (event.origin === this.props.originEndpoint && event.data.toString().includes('Token ')) {
                this.setState({ token: event.data })
            }
        }, false);
    }

    render() {
        const {id} = this.props;

        return (
            <div id={id}>
                Token: {this.state.token} <br></br>
            </div>
        );
    }
}

dashapitokenconsumer.defaultProps = {};

dashapitokenconsumer.propTypes = {
    /**
     * Origins that may pass the authentication token are limited to IoTBox frontend only, for now
     */
    originEndpoint: PropTypes.string.isRequired,
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string
};
