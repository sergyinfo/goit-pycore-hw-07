"""
This module contains decorators for the bot commands.
"""

from functools import wraps

def input_error(func: callable) -> callable:
    """
    Decorator to handle input errors across bot commands.

    Args:
        func (function): The function to decorate.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error: {str(e)}"
    return inner
