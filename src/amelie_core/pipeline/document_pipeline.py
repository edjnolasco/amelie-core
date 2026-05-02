from amelie_core.parsing.markdown_parser import parse_markdown
from amelie_core.normalization.markdown import normalize_markdown
from amelie_core.validation.document_rules import validate_document


def process_document(raw_md: str):
    doc = parse_markdown(raw_md)
    doc = normalize_markdown(doc)
    report = validate_document(doc)
    return doc, report