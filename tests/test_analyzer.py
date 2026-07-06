from json_presenter import Presenter
from json_presenter.analyzer import StructureAnalyzer
from json_presenter.models import AnalysisResult


def test_analyzer_returns_analysis_result():
    analyzer = StructureAnalyzer()

    result = analyzer.analyze({"name": "Alice"})

    assert isinstance(result, AnalysisResult)


def test_analyzer_detects_root_type():
    analyzer = StructureAnalyzer()

    result = analyzer.analyze({"name": "Alice"})

    assert result.root_type == "dict"


def test_analyzer_calculates_depth():
    analyzer = StructureAnalyzer()
    data = {"user": {"name": "Alice", "address": {"city": "Tokyo"}}}

    result = analyzer.analyze(data)

    assert result.depth == 3


def test_analyzer_counts_keys():
    analyzer = StructureAnalyzer()
    data = {"user": {"name": "Alice", "age": 25}}

    result = analyzer.analyze(data)

    assert result.total_keys == 3


def test_analyzer_detects_list_of_dicts():
    analyzer = StructureAnalyzer()
    data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
    ]

    result = analyzer.analyze(data)

    assert result.is_list_of_dicts is True


def test_presenter_analyze():
    presenter = Presenter.from_object({"name": "Alice"})

    result = presenter.analyze()

    assert result.root_type == "dict"
