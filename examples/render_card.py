from pathlib import Path

from json_presenter import Presenter, ThemeType, ViewType

input_path = Path("examples/data/person.json")
output_path = Path("examples/output/card_winter.html")

presenter = Presenter.from_file(input_path)

result = presenter.render(
    view=ViewType.CARDS,
    theme=ThemeType.WINTER,
)

result.save(output_path)

print(f"Generated: {output_path}")
