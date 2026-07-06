from pathlib import Path

from json_presenter import Presenter, ThemeType, ViewType


input_path = Path("examples/data/nested.json")
output_path = Path("examples/output/tree_dark.html")

presenter = Presenter.from_file(input_path)

result = presenter.render(
    view=ViewType.TREE,
    theme=ThemeType.DARK_DEVELOPER,
)

result.save(output_path)

print(f"Generated: {output_path}")
