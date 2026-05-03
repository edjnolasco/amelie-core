import re

from amelie_core.models.style import StyleResolutionResult, StyleSpec
from amelie_core.spec.resolver import resolve_font_ambiguity


def interpret_style(text: str) -> StyleResolutionResult:
    normalized = text.lower()
    spec = StyleSpec()

    # Font ambiguity / selection
    result = resolve_font_ambiguity(text, spec)

    # Font size
    size_match = re.search(r"\b(\d{1,2})\b", normalized)
    if size_match:
        result.spec.font_size = int(size_match.group(1))

    # Spacing
    if "doble" in normalized or "double" in normalized:
        result.spec.spacing = "double"
    elif "sencillo" in normalized or "single" in normalized:
        result.spec.spacing = "single"

    # Page size
    if "carta" in normalized or "letter" in normalized:
        result.spec.page_size = "letter"

    # Margins
    if "margen" in normalized or "márgenes" in normalized:
        if "1" in normalized or '1"' in normalized or "1 pulgada" in normalized:
            result.spec.margin_top = "1in"
            result.spec.margin_bottom = "1in"
            result.spec.margin_left = "1in"
            result.spec.margin_right = "1in"

    return result