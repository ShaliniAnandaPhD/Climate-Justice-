
"""
ContextualFairnessAuditor: Assesses claims for demographic bias using AI.
"""

import asyncio
from typing import Dict, Any

from .base_agent import BaseAgent
from ..data.demographic_data import get_demographic_data, get_bias_factors
from config.settings import COST_GEMINI_FLASH_CALL, ENABLE_GEMINI

class ContextualFairnessAuditor(BaseAgent):
    """Agent 2: Assesses claims for demographic bias using AI."""

    def __init__(self):
        super().__init__("ContextualFairnessAuditor", "yellow")

    async def assess(self, demographic: str, fire_scenario: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess bias risk using demographic data and AI context.

        Args:
            demographic: The demographic category of the claimant.
            fire_scenario: The details of the fire incident for context.

        Returns:
            Dictionary containing bias assessment results.
        """
        self.start_processing()
        self.log_step("⚖️ STARTING Fairness Audit Protocol")
        await asyncio.sleep(0.2)

        self.log_step("📊 Loading historical demographic data", f"Category: {demographic}")
        try:
            demo_data = get_demographic_data(demographic)
            bias_factors = get_bias_factors(demographic)
            # A simple statistical risk score based on historical denial rates
            base_score = demo_data["denial_rate"] * 3.0
        except KeyError as e:
            self.log_step("⚠️ ERROR: Demographic data not found", str(e))
            return {"error": str(e)}

        ai_insight = "No AI insight generated."
        final_score = base_score

        if ENABLE_GEMINI:
            self.log_step("🧠 Connecting to Google Gemini for contextual analysis...")
            prompt = self._create_gemini_prompt(demo_data, bias_factors, fire_scenario)
            await asyncio.sleep(0.6) # Simulate API call latency

            # --- In a real application, you would call the Gemini API here ---
            # response_text = call_gemini_api(prompt) 
            # ai_adjustment, ai_insight = self._parse_gemini_response(response_text)
            
            # Mocked response for this demo
            self.log_step("✅ AI analysis complete", "Parsing Gemini response")
            ai_adjustment = 15.0 if demographic == "low_income" else -5.0
            ai_insight = "AI analysis indicates heightened risk due to historical patterns of aggressive claim scrutiny in high-severity incidents."
            final_score += ai_adjustment
        
        final_score = min(100, max(0, final_score))
        
        processing_time = self.get_processing_time_ms()
        self.log_completion()

        return {
            "agent_name": self.agent_name,
            "bias_score": final_score,
            "bias_factors": bias_factors,
            "ai_insight": ai_insight,
            "processing_time_ms": processing_time,
            "cost": COST_GEMINI_FLASH_CALL if ENABLE_GEMINI else 0.0
        }

    def _create_gemini_prompt(self, demo_data: Dict, bias_factors: list, fire_scenario: Dict) -> str:
        """Creates a detailed prompt for the Gemini API."""
        return (
            f"Analyze potential bias for an insurance claim with the following context.\n"
            f"Fire Scenario: {fire_scenario['name']}, Severity: {fire_scenario['severity']}.\n"
            f"Claimant Demographic Profile: Historical denial rate of {demo_data['denial_rate']}%, "
            f"historically identified bias factors include: {', '.join(bias_factors)}.\n"
            f"Based on this, provide a risk adjustment score between -20 and +20 and a one-sentence summary of the key contextual risk."
        )
