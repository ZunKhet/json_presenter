from json_presenter.enums import ViewType
from json_presenter.exceptions import UnknownViewError
from json_presenter.presenters import (
    BasePresenter,
    CardPresenter,
    TablePresenter,
    TreePresenter,
)


class PresenterRegistry:
    """Registry that maps view types to presenter classes."""

    def __init__(self):
        self._registry: dict[ViewType, type[BasePresenter]] = {}
        self._register_defaults()

    def _register_defaults(self) -> None:
        self.register(ViewType.TREE, TreePresenter)
        self.register(ViewType.TABLE, TablePresenter)
        self.register(ViewType.CARDS, CardPresenter)

    def register(
        self,
        view_type: ViewType,
        presenter_class: type[BasePresenter],
    ) -> None:
        self._registry[view_type] = presenter_class

    def get(self, view_type: ViewType) -> type[BasePresenter]:
        try:
            return self._registry[view_type]
        except KeyError as exc:
            raise UnknownViewError(f"Unknown view type: {view_type}") from exc
