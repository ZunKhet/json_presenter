from dataclasses import dataclass


@dataclass(frozen=True)
class AnalysisResult:
    root_type: str
    depth: int
    total_keys: int
    total_items: int
    is_list_of_dicts: bool
