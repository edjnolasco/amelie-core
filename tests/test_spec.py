from amelie_core.spec.interpreter import interpret_style


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