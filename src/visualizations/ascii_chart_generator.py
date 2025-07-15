
"""
Generates ASCII art charts for console display.
"""

from typing import List, Tuple

class ASCIIChartGenerator:
    """A class to generate various ASCII art visualizations."""

    def create_horizontal_bar_chart(self, data: List[Tuple], title: str, show_values: bool = True, max_width: int = 40) -> str:
        """
        Creates a formatted horizontal ASCII bar chart.

        Args:
            data: A list of tuples, where each tuple is (label, value, icon, color).
            title: The title of the chart.
            show_values: Whether to display the value at the end of the bar.
            max_width: The maximum character width for the bars.

        Returns:
            A formatted multi-line string representing the chart.
        """
        if not data:
            return f"{title}\nNo data to display."

        max_val = max(item[1] for item in data if isinstance(item[1], (int, float))) if data else 1
        max_label_len = max(len(item[0]) for item in data) if data else 0
        
        chart_str = f"  [bold]{title}[/bold]\n"
        chart_str += "  " + "─" * (max_width + max_label_len + 15) + "\n"

        for label, value, icon, color in data:
            bar_len = int((value / max_val) * max_width) if max_val > 0 else 0
            bar = "█" * bar_len
            padding = " " * (max_label_len - len(label))
            
            value_str = f"{value:,.1f}" if isinstance(value, float) else f"{value:,}"
            display_val = f" {value_str}" if show_values else ""
            
            chart_str += f"  {icon} [white]{label}{padding}[/white] │ [{color}]{bar}[/{color}]{display_val}\n"
            
        chart_str += "  " + "─" * (max_width + max_label_len + 15)
        return chart_str

    def create_progress_bar(self, value: float, max_value: float, width: int, color: str) -> str:
        """
        Creates a single-line ASCII progress bar with rich color tags.

        Args:
            value: The current value.
            max_value: The maximum possible value.
            width: The character width of the bar.
            color: The rich color name for the bar.

        Returns:
            A formatted string for the progress bar.
        """
        if max_value <= 0:
            return "░" * width
            
        filled_len = int((value / max_value) * width)
        filled_len = max(0, min(filled_len, width))
        
        filled_chars = "█" * filled_len
        empty_chars = "░" * (width - filled_len)
        
        return f"[{color}]{filled_chars}[/{color}]{empty_chars}"
