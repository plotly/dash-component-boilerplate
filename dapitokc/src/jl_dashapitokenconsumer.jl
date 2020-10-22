# AUTO GENERATED FILE - DO NOT EDIT

export jl_dashapitokenconsumer

"""
    jl_dashapitokenconsumer(;kwargs...)

A dashapitokenconsumer component.

Keyword arguments:
- `originEndpoint` (String; required): Origins that may pass the authentication token are limited to IoTBox frontend only, for now
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
"""
function jl_dashapitokenconsumer(; kwargs...)
        available_props = Symbol[:originEndpoint, :id]
        wild_props = Symbol[]
        return Component("jl_dashapitokenconsumer", "dashapitokenconsumer", "dapitokc", available_props, wild_props; kwargs...)
end

