import re

def transform(text, transform_type):
    if transform_type == 'uppercase':
        return text.upper()
    elif transform_type == 'lowercase':
        return text.lower()
    elif transform_type == 'reverse':
        return text[::-1]
    elif transform_type == 'capitalize':
        return text.title()
    else:
        raise ValueError(f'Invalid transformation type: {transform_type}')