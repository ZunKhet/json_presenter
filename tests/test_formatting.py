from json_presenter.formatting import format_value
from json_presenter.formatting import humanize_label


def test_humanize_label_converts_snake_case():
    assert humanize_label("first_name") == "First Name"


def test_humanize_label_converts_kebab_case():
    assert humanize_label("created-at") == "Created At"


def test_humanize_label_preserves_common_acronyms():
    assert humanize_label("user_id") == "User ID"
    assert humanize_label("api_key") == "API Key"
    assert humanize_label("json_url") == "JSON URL"


def test_humanize_label_handles_empty_string():
    assert humanize_label("") == ""


def test_format_value_formats_none():
    result = format_value(None)

    assert "Not available" in result.html


def test_format_value_formats_boolean():
    true_result = format_value(True)
    false_result = format_value(False)

    assert "✓ Yes" in true_result.html
    assert "✕ No" in false_result.html


def test_format_value_formats_url_as_link():
    result = format_value("https://example.com")

    assert "<a" in result.html
    assert "href=" in result.html
    assert "https://example.com" in result.html


def test_format_value_formats_email_as_link():
    result = format_value("alice@example.com")

    assert "mailto:alice@example.com" in result.html


def test_format_value_escapes_plain_text():
    result = format_value("<script>alert('x')</script>")

    assert "&lt;script&gt;" in result.html
    assert "<script>" not in result.html
