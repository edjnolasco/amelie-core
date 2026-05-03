from dataclasses import dataclass, field
from typing import List


@dataclass
class Section:
    title: str
    level: int
    content: str


@dataclass
class Document:
    title: str
    sections: List[Section] = field(default_factory=list)
    raw: str = ""