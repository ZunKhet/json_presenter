from json_presenter.models import RenderedPresentation


def test_rendered_presentation_can_save_html(tmp_path):
    rendered = RenderedPresentation(html="<html>Hello</html>")
    output_path = tmp_path / "output.html"

    saved_path = rendered.save(output_path)

    assert saved_path == output_path
    assert output_path.read_text(encoding="utf-8") == "<html>Hello</html>"


def test_rendered_presentation_casts_to_string():
    rendered = RenderedPresentation(html="<html>Hello</html>")

    assert str(rendered) == "<html>Hello</html>"
