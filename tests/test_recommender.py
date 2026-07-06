from json_presenter import Presenter, ViewType
from json_presenter.models import AnalysisResult, ViewRecommendation
from json_presenter.recommenders import ViewRecommender
from json_presenter.recommenders.rules import TableRule


def test_table_rule_recommends_table_for_list_of_dicts():
    analysis = AnalysisResult(
        root_type="list",
        depth=2,
        total_keys=4,
        total_items=2,
        is_list_of_dicts=True,
    )

    recommendation = TableRule().recommend(analysis)

    assert recommendation is not None
    assert recommendation.view == ViewType.TABLE
    assert recommendation.confidence == 0.95


def test_recommender_returns_sorted_recommendations():
    analysis = AnalysisResult(
        root_type="list",
        depth=2,
        total_keys=4,
        total_items=2,
        is_list_of_dicts=True,
    )

    recommendations = ViewRecommender().recommend(analysis)

    assert len(recommendations) >= 1
    assert recommendations[0].confidence >= recommendations[-1].confidence


def test_presenter_recommend_views():
    presenter = Presenter.from_object(
        [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 30},
        ]
    )

    recommendations = presenter.recommend_views()

    assert isinstance(recommendations[0], ViewRecommendation)
    assert recommendations[0].view == ViewType.TABLE
