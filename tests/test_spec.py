from amelie_core.spec.interpreter import interpret_style
from amelie_core.pipeline.document_pipeline import process_document


def test_interpret_style_single_font():
    text = "Arial 12, interlineado sencillo, carta, márgenes 1 pulgada"

    result = interpret_style(text)

    assert result.is_resolved()
    assert result.spec.font_family == "Arial"
    assert result.spec.font_size == 12
    assert result.spec.spacing == "single"
    assert result.spec.page_size == "letter"
    assert result.spec.margin_top == "1in"


def test_interpret_style_ambiguous_fonts():
    text = (
        "Tipo de letra Arial, Calibri o Times New Roman. "
        "Tamaño 12. Espacio sencillo. Carta. Márgenes 1 pulgada."
    )

    result = interpret_style(text)

    assert not result.is_resolved()
    assert len(result.ambiguities) == 1

    ambiguity = result.ambiguities[0]

    assert ambiguity.field == "font_family"
    assert ambiguity.options == ["Arial", "Calibri", "Times New Roman"]
    assert result.spec.font_family is None
    assert result.spec.font_size == 12
    assert result.spec.spacing == "single"
    assert result.spec.page_size == "letter"
    
def test_pipeline_with_style():
    md = """# Title

## Section
Content
"""

    style_text = "Arial 12, interlineado sencillo, carta, márgenes 1 pulgada"

    result = process_document(md, style_text)

    assert result["document"].title == "Title"
    assert result["validation"].is_valid()

    style = result["style"]
    assert style is not None
    assert style.is_resolved()
    assert style.spec.font_family == "Arial"    