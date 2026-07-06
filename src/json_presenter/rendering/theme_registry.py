from json_presenter.enums import ThemeType
from json_presenter.exceptions import UnknownThemeError
from json_presenter.themes import (
    AutumnTheme,
    BaseTheme,
    DarkDeveloperTheme,
    DigitalTheme,
    MinimalTheme,
    SpringTheme,
    SummerTheme,
    WinterTheme,
)


class ThemeRegistry:
    """Registry that maps theme types to theme classes."""

    def __init__(self):
        self._registry: dict[ThemeType, type[BaseTheme]] = {}
        self._register_defaults()

    def _register_defaults(self) -> None:
        self.register(ThemeType.MINIMAL, MinimalTheme)
        self.register(ThemeType.DIGITAL, DigitalTheme)
        self.register(ThemeType.SPRING, SpringTheme)
        self.register(ThemeType.SUMMER, SummerTheme)
        self.register(ThemeType.AUTUMN, AutumnTheme)
        self.register(ThemeType.WINTER, WinterTheme)
        self.register(ThemeType.DARK_DEVELOPER, DarkDeveloperTheme)

    def register(
        self,
        theme_type: ThemeType,
        theme_class: type[BaseTheme],
    ) -> None:
        self._registry[theme_type] = theme_class

    def get(self, theme_type: ThemeType) -> type[BaseTheme]:
        try:
            return self._registry[theme_type]
        except KeyError as exc:
            raise UnknownThemeError(f"Unknown theme type: {theme_type}") from exc
