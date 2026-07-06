from abc import ABC, abstractmethod
from typing import Any

from json_presenter.presentation import PresentationDocument


class BasePresenter(ABC):
    """Base interface for presentation document builders."""

    @abstractmethod
    def build_document(self, data: Any) -> PresentationDocument:
        """Build a presentation document from JSON-compatible data."""
        raise NotImplementedError
