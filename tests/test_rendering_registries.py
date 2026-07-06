from json_presenter import ThemeType, ViewType
from json_presenter.presenters import CardPresenter, TablePresenter, TreePresenter
from json_presenter.rendering import PresenterRegistry, ThemeRegistry
from json_presenter.themes import MinimalTheme, WinterTheme
from json_presenter.themes import AutumnTheme, SummerTheme


def test_presenter_registry_returns_tree_presenter_class():
    registry = PresenterRegistry()

    presenter_class = registry.get(ViewType.TREE)

    assert presenter_class is TreePresenter


def test_presenter_registry_returns_table_presenter_class():
    registry = PresenterRegistry()

    presenter_class = registry.get(ViewType.TABLE)

    assert presenter_class is TablePresenter


def test_presenter_registry_returns_card_presenter_class():
    registry = PresenterRegistry()

    presenter_class = registry.get(ViewType.CARDS)

    assert presenter_class is CardPresenter


def test_theme_registry_returns_minimal_theme_class():
    registry = ThemeRegistry()

    theme_class = registry.get(ThemeType.MINIMAL)

    assert theme_class is MinimalTheme


def test_theme_registry_returns_winter_theme_class():
    registry = ThemeRegistry()

    theme_class = registry.get(ThemeType.WINTER)

    assert theme_class is WinterTheme


def test_theme_registry_returns_summer_theme_class():
    registry = ThemeRegistry()

    theme_class = registry.get(ThemeType.SUMMER)

    assert theme_class is SummerTheme


def test_theme_registry_returns_autumn_theme_class():
    registry = ThemeRegistry()

    theme_class = registry.get(ThemeType.AUTUMN)

    assert theme_class is AutumnTheme
