from dataclasses import dataclass
from typing import List


@dataclass
class ValidationIssue:
    message: str
    severity: str  # "error" | "warning"


@dataclass
class ValidationReport:
    issues: List[ValidationIssue]

    def is_valid(self) -> bool:
        return not any(i.severity == "error" for i in self.issues)