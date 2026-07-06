COMMON_ACRONYMS = {
    "id": "ID",
    "api": "API",
    "url": "URL",
    "uri": "URI",
    "html": "HTML",
    "css": "CSS",
    "json": "JSON",
    "xml": "XML",
    "ip": "IP",
}


def humanize_label(key: str) -> str:
    """Convert a JSON key into a human-friendly label."""
    normalized = key.replace("_", " ").replace("-", " ").strip()

    if not normalized:
        return key

    words = normalized.split()

    return " ".join(_humanize_word(word) for word in words)


def _humanize_word(word: str) -> str:
    lower_word = word.lower()

    if lower_word in COMMON_ACRONYMS:
        return COMMON_ACRONYMS[lower_word]

    return lower_word.capitalize()
