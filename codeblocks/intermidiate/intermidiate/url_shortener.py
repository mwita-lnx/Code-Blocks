from django.utils.crypto import get_random_string

def shortener():
    unique_chars = get_random_string(length=6, allowed_chars='ABCDEF123')
    return unique_chars
