from amelie_core.pipeline.document_pipeline import process_document


def test_pipeline_basic():
    md = """# Title

## Section 1
Content here
"""

    doc, report = process_document(md)

    assert doc.title == "Title"
    assert len(doc.sections) >= 1
    assert report.is_valid()