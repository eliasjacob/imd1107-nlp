import re
import unicodedata

def remove_numbers_punctuation_from_text(input_text: str) -> str:
    """
    Remove all numbers and punctuation from the input text.

    Args:
        input_text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    # Use regex to replace all non-alphabet characters with a space
    return re.sub(r'[^a-zA-Z ]', ' ', input_text)

def remove_excessive_spaces(input_text: str) -> str:
    """
    Remove excessive spaces in the given text.

    Args:
        input_text (str): The text to be processed.

    Returns:
        str: The processed text with excessive spaces removed.
    """
    # \s+ matches one or more whitespace characters
    # ' ' replaces the matched string with a single space
    # strip() removes leading and trailing spaces
    return re.sub(r'\s+', ' ', input_text).strip() 

def remove_short_words(input_text: str) -> str:
    """
    Remove all words of length 2 or less from the input text.

    Args:
        input_text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    # Split the text into words, filter out short words, and join back into a string
    return ' '.join([word for word in input_text.split() if len(word) > 2])

def remove_accented_characters(input_text: str) -> str:
    """
    Remove all accented characters from the input text.

    Args:
        input_text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    # Normalize the unicode form, encode to ASCII, ignore errors, and decode back to string
    normalized_text = unicodedata.normalize('NFKD', input_text)
    ascii_text = normalized_text.encode('ASCII', 'ignore')
    return ascii_text.decode()

def remove_repeated_non_word_characters(text: str) -> str:
    """
    Remove repeated non-word characters in the given text.

    Args:
        text (str): The text to be processed.

    Returns:
        str: The processed text with repeated non-word characters removed.
    """
    # \W matches any non-word character (equivalent to [^a-zA-Z0-9_ ])
    # \1+ matches one or more occurrences of the same character
    # r'\1' replaces the matched string with a single occurrence of the character
    # strip() removes leading and trailing spaces
    return re.sub(r'(\W)\1+', r'\1', text).strip()

def remove_repeated_letters(text: str, n_repeat: int = 4) -> str:
    """
    Remove repeated letters in the given text.

    Args:
        text (str): The text to be processed.
        n_repeat (int, optional): The number of times a letter must be repeated to be removed. Defaults to 4.

    Returns:
        str: The processed text with repeated letters removed.
    """
    # ([a-z]) matches a lowercase letter
    # \1{'+str(n_repeat)+',}' matches n_repeat or more occurrences of the same letter
    # r'\1' replaces the matched string with a single occurrence of the letter
    # strip() removes leading and trailing spaces
    # Example: 'hellooooo' -> 'hello'
    return re.sub(r'([a-z])\1{'+str(n_repeat)+',}', r'\1', text).strip()

