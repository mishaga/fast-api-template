def camel_to_snake_case(letters: str) -> str:
    """Translate CamelCase string to snake_case.

    Parameters:
        letters: string to translate

    Returns:
        string in snake case
    """
    name_parts = []

    for position, letter in enumerate(letters):
        if letter.isupper() and position > 0:
            name_parts.append('_')
        name_parts.append(letter.lower())

    return ''.join(name_parts)
