"""
PerilScorerEngine: Ingests real-time incident data to quantify physical risk.
"""

import asyncio
from typing import Dict

from .base_agent import BaseAgent
from config.settings import COST_CALFIRE_API_CALL


class PerilScorerEngine(BaseAgent):
    """Agent 1: Ingests real-time incident data to quantify physical risk."""
    
    def __init__(self):
        super().__init__("PerilScorerEngine", "red")

    async def assess(self, fire_scenario: Dict) -> Dict:
        """
        Assess fire peril risk based on scenario data.
        
        Args:
            fire_scenario: Dictionary containing fire incident data
            
        Returns:
            Dictionary containing risk assessment results
        """
        self.start_processing()
        self.log_step("🔥 STARTING Peril Scoring Protocol")
        await asyncio.sleep(0.3)
        
        self.log_step("📡 Establishing connection to Cal Fire data stream...")
        await asyncio.sleep(0.5)
        
        self.log_step("📊 Ingesting incident data packet", f"ID: {fire_scenario['incident_id']}")
        self.log_step("⚠️ Computing risk vector from incident parameters...")
        
        # Risk calculation based on multiple factors
        severity_score = self._calculate_severity_score(fire_scenario["severity"])
        containment_risk = self._calculate_containment_risk(fire_scenario["containment"])
        weather_score = self._calculate_weather_score(fire_scenario["wind_speed"], fire_scenario["humidity"])
        proximity_score = self._calculate_proximity_score(fire_scenario["structures_threatened"])
        
        total_risk = min(100, severity_score + containment_risk + weather_score + proximity_score)
        risk_level = self._determine_risk_level(total_risk)
        
        await asyncio.sleep(0.4)
        self.log_step("🌡️ Finalized peril score", f"Aggregated Score: {total_risk}/100 ({risk_level})")
        
        processing_time = self.get_processing_time_ms()
        self.log_completion()
        
        return {
            "agent_name": self.agent_name,
            "fire_risk_score": total_risk,
            "risk_level": risk_level,
            "processing_time_ms": processing_time,
            "cost": COST_CALFIRE_API_CALL,
            "risk_breakdown": {
                "severity_score": severity_score,
                "containment_risk": containment_risk,
                "weather_score": weather_score,
                "proximity_score": proximity_score,
            }
        }

    def _calculate_severity_score(self, severity: str) -> int:
        """Calculate risk score based on fire severity."""
        severity_map = {
            "EXTREME": 35,
            "HIGH": 25, 
            "MODERATE": 15,
            "LOW": 5
        }
        return severity_map.get(severity, 10)

    def _calculate_containment_risk(self, containment: int) -> int:
        """Calculate risk based on containment percentage."""
        return max(0, 30 - containment)

    def _calculate_weather_score(self, wind_speed: int, humidity: int) -> int:
        """Calculate weather-related risk score."""
        wind_risk = 20 if wind_speed > 50 else 10 if wind_speed > 25 else 5
        humidity_risk = 15 if humidity < 10 else 8 if humidity < 20 else 3
        return wind_risk + humidity_risk

    def _calculate_proximity_score(self, structures_threatened: int) -> int:
        """Calculate risk based on threatened structures."""
        if structures_threatened > 5000:
            return 15
        elif structures_threatened > 1000:
            return 10
        else:
            return 5

    def _determine_risk_level(self, total_risk: int) -> str:
        """Determine risk level based on total score."""
        if total_risk >= 85:
            return "EXTREME DANGER"
        elif total_risk >= 65:
            return "HIGH RISK"
        elif total_risk >= 45:
            return "MODERATE RISK"
        else:
            return "LOW RISK"
