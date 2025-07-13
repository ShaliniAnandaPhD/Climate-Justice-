"""
Console utilities for the Gabrielino Fire Assessment system.
"""

from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.align import Align

# Global console instance
console = Console()


def create_header_panel(title: str, subtitle: str = "") -> Panel:
    """
    Create a formatted header panel.
    
    Args:
        title: Main title text
        subtitle: Optional subtitle text
        
    Returns:
        Rich Panel object
    """
    header_text = Text(title, justify="center", style="bold magenta")
    
    if subtitle:
        sub_text = Text(subtitle, justify="center", style="white")
        content = Text.assemble(header_text, "\n", sub_text)
    else:
        content = header_text
    
    return Panel(content, border_style="blue")


def create_progress_bar(value: float, max_value: float = 100, width: int = 20, 
                       filled_char: str = "█", empty_char: str = "░") -> str:
    """
    Create an ASCII progress bar.
    
    Args:
        value: Current value
        max_value: Maximum value
        width: Width of the progress bar
        filled_char: Character for filled portion
        empty_char: Character for empty portion
        
    Returns:
        ASCII progress bar string
    """
    if max_value <= 0:
        return empty_char * width
        
    filled_length = int((value / max_value) * width)
    filled_length = max(0, min(filled_length, width))
    
    return filled_char * filled_length + empty_char * (width - filled_length)


def format_currency(amount: float) -> str:
    """
    Format a currency amount with proper separators.
    
    Args:
        amount: Currency amount
        
    Returns:
        Formatted currency string
    """
    return f"${amount:,.2f}"


def format_percentage(value: float, decimal_places: int = 1) -> str:
    """
    Format a percentage value.
    
    Args:
        value: Percentage value (0.0 to 1.0)
        decimal_places: Number of decimal places
        
    Returns:
        Formatted percentage string
    """
    return f"{value * 100:.{decimal_places}f}%"


def format_time_ms(time_ms: float) -> str:
    """
    Format time in milliseconds to a readable string.
    
    Args:
        time_ms: Time in milliseconds
        
    Returns:
        Formatted time string
    """
    if time_ms < 1000:
        return f"{time_ms:.0f}ms"
    elif time_ms < 60000:
        return f"{time_ms/1000:.1f}s"
    else:
        return f"{time_ms/60000:.1f}min"


def clear_screen():
    """Clear the console screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def print_separator(char: str = "=", length: int = 80, style: str = "dim"):
    """
    Print a separator line.
    
    Args:
        char: Character to use for separator
        length: Length of separator
        style: Rich style to apply
    """
    console.print(char * length, style=style)
