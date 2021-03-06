
class Error(Exception):
    """Generic error class for invalid wordnet operations."""

    # reset the module so the user sees the public name
    __module__ = 'wn'


class Warning(Warning):
    """Generic warning class for dubious worndet operations."""

    # reset the module so the user sees the public name
    __module__ = 'wn'
