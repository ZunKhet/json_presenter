from pathlib import Path

from json_presenter import Presenter, ThemeType, ViewType

DATASETS = [
    ("person", ThemeType.WINTER),
    ("company", ThemeType.SPRING),
    ("country", ThemeType.MINIMAL),
    ("book", ThemeType.AUTUMN),
    ("github_repo", ThemeType.DARK_DEVELOPER),
    ("weather", ThemeType.SUMMER),
    ("api_response", ThemeType.DIGITAL),
]


def main() -> None:
    output_dir = Path("examples/output")
    output_dir.mkdir(exist_ok=True)

    for dataset_name, theme in DATASETS:
        input_path = Path(f"examples/data/{dataset_name}.json")
        output_path = output_dir / f"{dataset_name}_cards.html"

        presenter = Presenter.from_file(input_path)

        result = presenter.render(
            view=ViewType.CARDS,
            theme=theme,
        )

        result.save(output_path)

        print(f"Generated: {output_path}")


if __name__ == "__main__":
    main()
