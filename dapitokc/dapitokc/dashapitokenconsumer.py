# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class dashapitokenconsumer(Component):
    """A dashapitokenconsumer component.


Keyword arguments:
- originEndpoint (string; required): Origins that may pass the authentication token are limited to IoTBox frontend only, for now
- id (string; optional): The ID used to identify this component in Dash callbacks."""
    @_explicitize_args
    def __init__(self, originEndpoint=Component.REQUIRED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['originEndpoint', 'id']
        self._type = 'dashapitokenconsumer'
        self._namespace = 'dapitokc'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['originEndpoint', 'id']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['originEndpoint']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(dashapitokenconsumer, self).__init__(**args)
