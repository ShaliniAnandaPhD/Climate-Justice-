
"""
MultiFactorRiskOrchestrator: Synthesizes all agent outputs for a final decision.
"""

import asyncio
from typing import Dict, Any

from .base_agent import BaseAgent


class MultiFactorRiskOrchestrator(BaseAgent):
    """Agent 4: Synthesizes all agent outputs for a final decision."""

    def __init__(self):
        super().__init__("MultiFactorRiskOrchestrator", "magenta")
        # Define weights for the decision matrix
        self.weights = {
            "fire": 0.5,
            "bias": 0.4,
            "historical": 0.1
        }

    async def synthesize(self, agent_results: Dict[str, Any], claim_damage: int) -> Dict[str, Any]:
        """
        Synthesizes all inputs into a final priority score and recommendation.
        
        Args:
            agent_results: A dictionary containing results from other agents.
            claim_damage: The damage amount of the claim.
            
        Returns:
            A dictionary with the final decision.
        """
        self.start_processing()
        self.log_step("🎯 STARTING Decision Synthesis Protocol")
        await asyncio.sleep(0.1)
        
        fire_res = agent_results.get("fire", {})
        bias_res = agent_results.get("bias", {})
        memory_res = agent_results.get("memory", {})

        # Calculate weighted score
        fire_comp = fire_res.get("fire_risk_score", 0.0) * self.weights["fire"]
        bias_comp = bias_res.get("bias_score", 0.0) * self.weights["bias"]
        hist_comp = memory_res.get("pattern_confidence", 0.0) * 100 * self.weights["historical"]
        
        priority_score = min(100, fire_comp + bias_comp + hist_comp)
        
        self.log_step("⚖️ Calculating final priority score", f"Score: {priority_score:.1f}/100")
        
        final_recommendation = self._generate_recommendation(priority_score, fire_res, bias_res)
        
        processing_time = self.get_processing_time_ms()
        self.log_completion()

        return {
            "agent_name": self.agent_name,
            "priority_score": priority_score,
            "final_recommendation": final_recommendation,
            "processing_time_ms": processing_time,
            "cost": 0.0, # Orchestration has no direct cost
        }
        
    def _generate_recommendation(self, score: float, fire_res, bias_res) -> Dict:
        """Generates title, summary, and actions based on the priority score."""
        if score >= 80:
            priority = "CRITICAL"
            title = "Immediate Escalation to Senior Adjuster"
            summary = "Extreme fire peril combined with high bias risk requires immediate expert review and intervention to ensure fair handling."
            actions = ["Assign Tier-3 Adjuster (0-1 hr)", "Activate Bias Mitigation Protocol", "Flag for Executive Oversight"]
        elif score >= 65:
            priority = "HIGH"
            title = "Priority Review by Specialized Team"
            summary = "Significant risk factors detected. Claim requires careful review by a team trained in handling high-risk and potentially biased cases."
            actions = ["Assign to High-Risk Queue", "Mandatory Supervisor Review", "Verify all documentation with extra scrutiny"]
        else:
            priority = "STANDARD"
            title = "Proceed with Standard Automated Processing"
            summary = "Risk factors are within acceptable parameters. Claim is cleared for standard, automated processing track."
            actions = ["Assign to Standard Queue", "Process via Automated Rules Engine", "Spot-check for QA"]
            
        return {"priority": priority, "title": title, "summary": summary, "actions": actions}
