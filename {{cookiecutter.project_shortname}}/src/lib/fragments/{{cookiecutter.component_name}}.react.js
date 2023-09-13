import React from 'react';
import PropTypes from 'prop-types';
import {defaultProps, propTypes} from '../components/{{cookiecutter.component_name}}.react';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
const {{cookiecutter.component_name}} = (props) => {
    const {id, label, setProps, value} = props;

    return (
        <div id={id}>
            ExampleComponent: {label}&nbsp;
            <input
                value={value}
                onChange={
                    /*
                        * Send the new value to the parent component.
                        * setProps is a prop that is automatically supplied
                        * by dash's front-end ("dash-renderer").
                        * In a Dash app, this will update the component's
                        * props and send the data back to the Python Dash
                        * app server if a callback uses the modified prop as
                        * Input or State.
                        */
                    e => setProps({ value: e.target.value })
                }
            />
        </div>
    );
}


{{cookiecutter.component_name}}.defaultProps = defaultProps;
{{cookiecutter.component_name}}.propTypes = propTypes;

export default {{cookiecutter.component_name}};
