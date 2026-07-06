from pathlib import Path

from json_presenter import Presenter, ThemeType, ViewType


input_path = Path("examples/data/people.json")
output_path = Path("examples/output/table_minimal.html")

presenter = Presenter.from_file(input_path)

result = presenter.render(
    view=ViewType.TABLE,
    theme=ThemeType.SPRING,
)

result.save(output_path)

print(f"Generated: {output_path}")
