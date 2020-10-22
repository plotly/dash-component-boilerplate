# AUTO GENERATED FILE - DO NOT EDIT

rdashapitokenconsumer <- function(originEndpoint=NULL, id=NULL) {
    
    props <- list(originEndpoint=originEndpoint, id=id)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'dashapitokenconsumer',
        namespace = 'dapitokc',
        propNames = c('originEndpoint', 'id'),
        package = 'dapitokc'
        )

    structure(component, class = c('dash_component', 'list'))
}
