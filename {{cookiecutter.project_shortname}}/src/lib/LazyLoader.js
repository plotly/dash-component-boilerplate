import React from 'react';

export const {{cookiecutter.component_name}} = React.lazy(() => import(/* webpackChunkName: "{{cookiecutter.component_name}}" */ './fragments/{{cookiecutter.component_name}}.react'));
