#' {{ cookiecutter.project_short_description }}
#'
#' @docType package
#' @name {{ cookiecutter.r_package_name }}
#
# Write functions only and document them with roxygen-styled comments.
# Example below taken from http://r-pkgs.had.co.nz/man.html
#

#' Add together two numbers.
#' 
#' @param x A number.
#' @param y A number.
#' @return The sum of \code{x} and \code{y}.
#' @examples
#' add(1, 1)
#' add(10, 1)
#' @export
add <- function(x, y) {
      x + y
}

