class JsonPresenterError(Exception):
    """Base exception for json_presenter."""


class InvalidJsonError(JsonPresenterError):
    """Raised when JSON input is invalid."""


class UnknownViewError(JsonPresenterError):
    """Raised when a requested view is not registered."""


class UnknownThemeError(JsonPresenterError):
    """Raised when a requested theme is not registered."""


class RenderError(JsonPresenterError):
    """Raised when rendering fails."""
