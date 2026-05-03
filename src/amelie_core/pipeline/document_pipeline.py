from amelie_core.parsing.markdown_parser import parse_markdown
from amelie_core.normalization.markdown import normalize_markdown
from amelie_core.validation.document_rules import validate_document
from amelie_core.spec.interpreter import interpret_style


def process_document(raw_md: str, style_text: str | None = None):
    doc = parse_markdown(raw_md)
    doc = normalize_markdown(doc)

    validation_report = validate_document(doc)

    style_result = None
    if style_text:
        style_result = interpret_style(style_text)

    return {
        "document": doc,
        "validation": validation_report,
        "style": style_result,
    }