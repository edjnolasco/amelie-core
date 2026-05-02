from amelie_core.models.document import Document, Section


def parse_markdown(md: str) -> Document:
    lines = md.splitlines()

    sections = []
    current_section = None

    for line in lines:
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            title = line.strip("# ").strip()

            current_section = Section(title=title, level=level, content="")
            sections.append(current_section)
        else:
            if current_section:
                current_section.content += line + "\n"

    title = sections[0].title if sections else "Untitled"

    return Document(title=title, sections=sections, raw=md)