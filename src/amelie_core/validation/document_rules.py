from amelie_core.models.validation import ValidationReport, ValidationIssue
from amelie_core.models.document import Document


def validate_document(doc: Document) -> ValidationReport:
    issues = []

    if not doc.title:
        issues.append(ValidationIssue("Document has no title", "error"))

    if not doc.sections:
        issues.append(ValidationIssue("Document has no sections", "error"))

    return ValidationReport(issues)