from dataclasses import dataclass, field


@dataclass
class StyleSpec:
    font_family: str | None = None
    font_size: int = 12
    spacing: str = "single"  # single | double
    page_size: str = "letter"
    margin_top: str = "1in"
    margin_bottom: str = "1in"
    margin_left: str = "1in"
    margin_right: str = "1in"


@dataclass
class AmbiguousStyleOption:
    field: str
    options: list[str]
    message: str


@dataclass
class StyleResolutionResult:
    spec: StyleSpec
    ambiguities: list[AmbiguousStyleOption] = field(default_factory=list)

    def is_resolved(self) -> bool:
        return len(self.ambiguities) == 0