from amelie_core.models.document import Document


def normalize_markdown(doc: Document) -> Document:
    for section in doc.sections:
        section.content = section.content.strip()

    return doc