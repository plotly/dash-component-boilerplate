
module Dapitokc
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl_dashapitokenconsumer.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dapitokc",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dapitokc.min.js",
    external_url = "https://unpkg.com/dapitokc@0.0.1/dapitokc/dapitokc.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dapitokc.min.js.map",
    external_url = "https://unpkg.com/dapitokc@0.0.1/dapitokc/dapitokc.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
