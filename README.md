# json_presenter

> Transform JSON into meaningful, beautiful, downloadable presentation views.

`json_presenter` is an open-source Python package that converts JSON data into presentation-ready visual layouts.

Unlike traditional JSON viewers or formatters, `json_presenter` focuses on helping people understand data through attractive, human-friendly presentations.

---

## Features

* Load JSON from:

  * Python dictionaries and lists
  * JSON strings
  * JSON files

* Analyze JSON structure

* Recommend suitable presentation views

* Render JSON as:

  * Card View
  * Table View
  * Tree View

* Built-in themes

  * Minimal
  * Digital
  * Spring
  * Summer
  * Autumn
  * Winter
  * Dark Developer

* Human-friendly presentation

  * Nested cards
  * Expandable collections
  * Humanized labels
  * Value formatting
  * Beautiful HTML output

---

## Installation

```bash
pip install json_presenter
```

---

## Quick Start

```python
from json_presenter import Presenter
from json_presenter import ViewType
from json_presenter import ThemeType

result = (
    Presenter
    .from_file("company.json")
    .render(
        view=ViewType.CARDS,
        theme=ThemeType.WINTER,
    )
)

result.save("company.html")
```

---

## Loading JSON

### Python object

```python
Presenter.from_object(data)
```

### JSON string

```python
Presenter.from_json(json_string)
```

### JSON file

```python
Presenter.from_file("data.json")
```

---

## View Recommendation

```python
presenter = Presenter.from_file("data.json")

recommendations = presenter.recommend_views()

for recommendation in recommendations:
    print(
        recommendation.view,
        recommendation.confidence,
        recommendation.reason,
    )
```

---

## Supported Views

| View  | Status |
| ----- | ------ |
| Cards | ✅      |
| Table | ✅      |
| Tree  | ✅      |

---

## Themes

* Minimal
* Digital
* Spring
* Summer
* Autumn
* Winter
* Dark Developer

---

## Project Structure

```text
src/
└── json_presenter/
    ├── analyzer/
    ├── formatting/
    ├── models/
    ├── presenters/
    ├── presentation/
    ├── recommendations/
    ├── rendering/
    ├── themes/
    └── utils/
```

---

## Examples

Example datasets are available in:

```text
examples/data/
```

Generate showcase pages:

```bash
python examples/render_showcase.py
```

Generated HTML files are written to:

```text
examples/output/
```

---

## Roadmap

### Version 0.1

* HTML rendering
* Card view
* Table view
* Tree view
* Themes
* View recommendation

### Future

* SVG renderer
* PDF export
* Interactive presentation layouts
* Plugin system
* Additional presentation views

---

## Contributing

Contributions, feature requests, bug reports, and discussions are welcome.

Please see `CONTRIBUTING.md` for development guidelines.

---

## License

MIT License.
