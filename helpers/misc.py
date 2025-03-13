import random

def get_random_colors(num_colors: int) -> list[str]:
    """
    Returns a list of random colors from a predefined set of color codes.

    Args:
        num_colors (int): The number of random colors to return. Must be less than or equal to the number of available colors.

    Returns:
        list[str]: A list of random color codes in hexadecimal format.

    Raises:
        AssertionError: If num_colors is greater than the number of available colors.

    Example:
        >>> get_random_colors(5)
        ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF']
    """
    # Predefined list of color codes
    color_codes = [
        '#FF0000',  # Red
        '#00FF00',  # Lime
        '#0000FF',  # Blue
        '#FFFF00',  # Yellow
        '#00FFFF',  # Aqua
        '#FF00FF',  # Fuchsia
        '#C0C0C0',  # Silver
        '#808080',  # Gray
        '#800000',  # Maroon
        '#808000',  # Olive
        '#008000',  # Green
        '#800080',  # Purple
        '#008080',  # Teal
        '#000080',  # Navy
        '#FFA500',  # Orange
        '#A52A2A',  # Brown
        '#8B4513',  # SaddleBrown
        '#5F9EA0',  # CadetBlue
        '#7FFF00',  # Chartreuse
        '#D2691E',  # Chocolate
        '#FF7F50',  # Coral
        '#6495ED',  # CornflowerBlue
        '#DC143C',  # Crimson
        '#00FFFF',  # Cyan
        '#00008B',  # DarkBlue
        '#008B8B',  # DarkCyan
        '#B8860B',  # DarkGoldenRod
        '#A9A9A9'   # DarkGray
    ]

    # Ensure the requested number of colors does not exceed the available colors
    assert num_colors <= len(color_codes), f'You can only get up to {len(color_codes)} colors'

    # Return a random sample of the requested number of colors
    return random.sample(color_codes, num_colors)