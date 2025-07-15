
"""
HistoricalDataSynthesisEngine: Analyzes patterns against historical data.
"""

import asyncio
import re
from typing import Dict, Any

import ollama

from .base_agent import BaseAgent
from config.settings import ENABLE_OLLAMA, OLLAMA_MODEL


class HistoricalDataSynthesisEngine(BaseAgent):
    """Agent 3: Analyzes claim against historical data using a local LLM."""

    def __init__(self):
        super().__init__("HistoricalDataSynthesisEngine", "blue")
        if ENABLE_OLLAMA:
            self.client = ollama.AsyncClient()
        else:
            self.client = None

    async def assess(self, claim_damage: int) -> Dict[str, Any]:
        """Synthesizes insights from historical claim data."""
        self.start_processing()
        self.log_step("📚 STARTING Historical Synthesis Protocol")
        
        # In a real system, this would come from a vector DB lookup
        similar_cases_found = 47 
        historical_context = (
            "Case 1: $580k claim, settled for $450k (77%), 88 days. HIGH fire risk zone.\n"
            "Case 2: $520k claim, settled for $410k (79%), 95 days. Similar demographic.\n"
            "Case 3: $610k claim, settled for $580k (95%), 30 days. Low fire risk, different demographic.\n"
        )

        pattern_confidence = 0.0
        pattern_insight = "Ollama analysis disabled."

        if self.client and ENABLE_OLLAMA:
            self.log_step("🧠 Querying local LLM for pattern synthesis...", f"Model: {OLLAMA_MODEL}")
            prompt = self._create_ollama_prompt(claim_damage, historical_context)
            try:
                response = await self.client.generate(model=OLLAMA_MODEL, prompt=prompt, stream=False)
                pattern_confidence, pattern_insight = self._parse_ollama_response(response['response'])
                self.log_step("✅ Pattern analysis complete", f"Confidence: {pattern_confidence:.0%}")
            except Exception as e:
                self.log_step("⚠️ OLLAMA FAILED", "Is the Ollama server running?")
                pattern_insight = "Local LLM analysis failed. Please ensure Ollama is running."
        
        processing_time = self.get_processing_time_ms()
        self.log_completion()

        return {
            "agent_name": self.agent_name,
            "similar_cases_found": similar_cases_found,
            "pattern_confidence": pattern_confidence,
            "pattern_insight": pattern_insight,
            "processing_time_ms": processing_time,
            "cost": 0.0, # Local model, no direct API cost
        }

    def _create_ollama_prompt(self, claim_damage: int, historical_context: str) -> str:
        """Creates a prompt for the local LLM."""
        return (
            "You are a claims analysis expert. Based on the provided historical cases, "
            "analyze the current claim and provide a structured response.\n"
            f"CURRENT CLAIM: Damage estimated at ${claim_damage:,.0f}.\n"
            f"HISTORICAL CONTEXT:\n{historical_context}\n"
            "REQUIRED FORMAT:\n"
            "CONFIDENCE: [A float between 0.0 and 1.0 representing confidence in a predictable pattern.]\n"
            "INSIGHT: [A one-sentence summary of the primary pattern observed.]"
        )

    def _parse_ollama_response(self, text: str) -> (float, str):
        """Parses the structured response from the Ollama model."""
        try:
            confidence_match = re.search(r"CONFIDENCE:\s*([0-9.]+)", text, re.IGNORECASE)
            insight_match = re.search(r"INSIGHT:\s*(.+)", text, re.IGNORECASE)

            confidence = float(confidence_match.group(1)) if confidence_match else 0.5
            insight = insight_match.group(1).strip() if insight_match else "No insight generated."

            return confidence, insight
        except Exception:
            return 0.5, "Failed to parse local LLM response."
