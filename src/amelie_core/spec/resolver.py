from amelie_core.models.style import AmbiguousStyleOption, StyleResolutionResult, StyleSpec


SUPPORTED_FONTS = ["Arial", "Calibri", "Times New Roman"]


def resolve_font_ambiguity(text: str, spec: StyleSpec) -> StyleResolutionResult:
    text_lower = text.lower()

    found_fonts = [
        font for font in SUPPORTED_FONTS
        if font.lower() in text_lower
    ]

    ambiguities = []

    if len(found_fonts) == 1:
        spec.font_family = found_fonts[0]

    elif len(found_fonts) > 1:
        ambiguities.append(
            AmbiguousStyleOption(
                field="font_family",
                options=found_fonts,
                message="Multiple allowed fonts were detected. Select one font family.",
            )
        )

    return StyleResolutionResult(spec=spec, ambiguities=ambiguities)