from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RenderedPresentation:
    html: str

    def save(self, file_path: str | Path) -> Path:
        path = Path(file_path)
        path.write_text(self.html, encoding="utf-8")
        return path

    def __str__(self) -> str:
        return self.html
