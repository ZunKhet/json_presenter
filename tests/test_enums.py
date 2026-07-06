from json_presenter import ThemeType, ViewType


def test_view_type_values():
    assert ViewType.TREE.value == "tree"
    assert ViewType.TABLE.value == "table"
    assert ViewType.CARDS.value == "cards"


def test_theme_type_values():
    assert ThemeType.MINIMAL.value == "minimal"
    assert ThemeType.DIGITAL.value == "digital"
    assert ThemeType.SPRING.value == "spring"
    assert ThemeType.SUMMER.value == "summer"
    assert ThemeType.AUTUMN.value == "autumn"
    assert ThemeType.WINTER.value == "winter"
    assert ThemeType.DARK_DEVELOPER.value == "dark_developer"
