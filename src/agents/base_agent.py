"""
Base agent class for all Gabrielino agents.
"""

import uuid
import time
from datetime import datetime
from typing import Optional

from ..utils.console_utils import console
from config.settings import PROCESSING_DELAY_MS


class BaseAgent:
    """A base class for all agents, providing common functionality."""
    
    def __init__(self, agent_name: str, color: str):
        """
        Initialize the base agent.
        
        Args:
            agent_name: The name of the agent
            color: The color to use for console output
        """
        self.agent_name = agent_name
        self.agent_id = str(uuid.uuid4())[:8]
        self.color = color
        self._start_time: Optional[float] = None

    def log_step(self, step: str, detail: str = ""):
        """
        Log a single step of the agent's process.
        
        Args:
            step: The step description
            detail: Optional additional detail
        """
        timestamp = datetime.now().strftime('%H:%M:%S.%f')[:-3]
        console.print(f"[dim]{timestamp}[/] [{self.color}][{self.agent_name}][/] {step}")
        if detail:
            console.print(f"[dim]  └─ {detail}[/]")
        time.sleep(PROCESSING_DELAY_MS / 1000)  # Convert ms to seconds

    def start_processing(self):
        """Mark the start of processing for timing."""
        self._start_time = time.time()

    def get_processing_time_ms(self) -> float:
        """Get the processing time in milliseconds."""
        if self._start_time is None:
            return 0.0
        return (time.time() - self._start_time) * 1000

    def log_completion(self, additional_info: str = ""):
        """Log the completion of the agent's processing."""
        processing_time = self.get_processing_time_ms()
        completion_msg = f"✅ PROTOCOL COMPLETE - Elapsed time: {processing_time:.0f}ms"
        if additional_info:
            completion_msg += f" - {additional_info}"
        self.log_step(completion_msg)
