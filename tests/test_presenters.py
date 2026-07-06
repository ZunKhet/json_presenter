from json_presenter import ViewType
from json_presenter.presentation import (
    CardNode,
    NestedField,
    PrimitiveField,
    TableNode,
    TreeNode,
)
from json_presenter.presenters import CardPresenter, TablePresenter, TreePresenter
from json_presenter.presentation import CollectionField


def test_tree_presenter_builds_tree_document():
    document = TreePresenter().build_document({"name": "Alice"})

    assert document.view == ViewType.TREE
    assert isinstance(document.nodes[0], TreeNode)
    assert document.nodes[0].label == "root"


def test_table_presenter_builds_table_document():
    document = TablePresenter().build_document([{"name": "Alice"}])

    assert document.view == ViewType.TABLE
    assert isinstance(document.nodes[0], TableNode)
    assert document.nodes[0].headers == ["name"]


def test_card_presenter_builds_card_document():
    document = CardPresenter().build_document(
        {
            "name": "Alice",
            "age": 25,
        }
    )

    assert document.view == ViewType.CARDS
    assert document.title == "JSON Object"
    assert document.subtitle == "2 properties"
    assert document.description == "Object presented as semantic cards."

    card = document.nodes[0]

    assert isinstance(card, CardNode)
    assert card.title == "Properties"

    assert isinstance(card.fields[0], PrimitiveField)
    assert card.fields[0].label == "Name"
    assert card.fields[0].content == "Alice"

    assert isinstance(card.fields[1], PrimitiveField)
    assert card.fields[1].label == "Age"
    assert card.fields[1].content == 25


def test_card_presenter_builds_value_document():
    document = CardPresenter().build_document(42)

    card = document.nodes[0]

    assert document.title == "JSON Value"
    assert document.subtitle == "int"
    assert isinstance(card, CardNode)
    assert isinstance(card.fields[0], PrimitiveField)
    assert card.fields[0].label == "Value"
    assert card.fields[0].content == 42


def test_card_presenter_builds_nested_card_from_dict():
    document = CardPresenter().build_document(
        {
            "name": "Alice",
            "profile": {
                "country": "Japan",
                "role": "Engineer",
            },
        }
    )

    card = document.nodes[0]

    assert isinstance(card, CardNode)
    assert isinstance(card.fields[0], PrimitiveField)
    assert card.fields[0].label == "Name"

    assert isinstance(card.fields[1], NestedField)
    assert card.fields[1].label == "Profile"
    assert card.fields[1].card.title == "Profile"

    nested_card = card.fields[1].card

    assert isinstance(nested_card.fields[0], PrimitiveField)
    assert nested_card.fields[0].label == "Country"
    assert nested_card.fields[0].content == "Japan"


def test_card_presenter_builds_collection_field_from_primitive_list():
    document = CardPresenter().build_document(
        {
            "skills": ["Python", "AI", "Computer Vision"],
        }
    )

    card = document.nodes[0]
    field = card.fields[0]

    assert isinstance(field, CollectionField)
    assert field.label == "Skills"
    assert len(field.items) == 3
    assert isinstance(field.items[0], PrimitiveField)
    assert field.items[0].content == "Python"


def test_card_presenter_builds_collection_field_from_list_of_dicts():
    document = CardPresenter().build_document(
        {
            "employees": [
                {"name": "Alice", "role": "Engineer"},
                {"name": "Bob", "role": "Designer"},
            ]
        }
    )

    card = document.nodes[0]
    field = card.fields[0]

    assert isinstance(field, CollectionField)
    assert field.label == "Employees"
    assert len(field.items) == 2
    assert isinstance(field.items[0], CardNode)
    assert field.items[0].title == "Alice"
    assert field.items[1].title == "Bob"


def test_card_presenter_builds_multiple_cards_from_root_list_of_dicts():
    document = CardPresenter().build_document(
        [
            {"name": "Alice", "role": "Engineer"},
            {"name": "Bob", "role": "Designer"},
        ]
    )

    assert document.title == "JSON Collection"
    assert document.subtitle == "2 items"
    assert len(document.nodes) == 2
    assert document.nodes[0].title == "Alice"
    assert document.nodes[1].title == "Bob"
