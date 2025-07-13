"""
Demographic data for bias analysis in the Gabrielino assessment system.
"""

# Historical demographic data for bias analysis
DEMOGRAPHIC_DATA = {
    "low_income": {
        "denial_rate": 18.5,
        "payout_ratio": 0.68,
        "processing_days": 28.7,
        "appeal_rate": 35.2,
        "satisfaction_score": 6.1,
        "description": "Lower income demographic historically facing higher denial rates"
    },
    "high_income": {
        "denial_rate": 3.2,
        "payout_ratio": 0.94,
        "processing_days": 8.5,
        "appeal_rate": 8.1,
        "satisfaction_score": 8.7,
        "description": "Higher income demographic with more favorable outcomes"
    },
    "middle_income": {
        "denial_rate": 9.8,
        "payout_ratio": 0.82,
        "processing_days": 16.3,
        "appeal_rate": 18.5,
        "satisfaction_score": 7.2,
        "description": "Middle income demographic with moderate outcomes"
    },
    "elderly": {
        "denial_rate": 12.1,
        "payout_ratio": 0.79,
        "processing_days": 22.1,
        "appeal_rate": 24.8,
        "satisfaction_score": 6.8,
        "description": "Elderly demographic often needing additional support"
    },
    "minority": {
        "denial_rate": 16.3,
        "payout_ratio": 0.71,
        "processing_days": 25.4,
        "appeal_rate": 31.7,
        "satisfaction_score": 6.3,
        "description": "Minority demographic showing concerning bias patterns"
    }
}


def get_demographic_data(demographic: str):
    """
    Get demographic data by category.
    
    Args:
        demographic: Demographic category name
        
    Returns:
        Demographic data dictionary
        
    Raises:
        KeyError: If demographic category not found
    """
    if demographic not in DEMOGRAPHIC_DATA:
        raise KeyError(f"Demographic '{demographic}' not found. Available: {list(DEMOGRAPHIC_DATA.keys())}")
    
    return DEMOGRAPHIC_DATA[demographic]


def calculate_bias_risk(demographic: str, emergency_factor: float = 1.0) -> float:
    """
    Calculate bias risk score for a demographic.
    
    Args:
        demographic: Demographic category
        emergency_factor: Emergency amplifier (1.0 = normal, >1.0 = emergency)
        
    Returns:
        Bias risk score (0-100)
    """
    demo_data = get_demographic_data(demographic)
    
    # Base bias score from denial rate
    base_score = demo_data["denial_rate"] * 3.5
    
    # Apply emergency amplifier
    final_score = min(100, base_score * emergency_factor)
    
    return final_score


def get_bias_factors(demographic: str) -> list:
    """
    Get potential bias factors for a demographic.
    
    Args:
        demographic: Demographic category
        
    Returns:
        List of potential bias factors
    """
    bias_factors = {
        "low_income": [
            "Limited access to legal representation",
            "Complex claim documentation requirements", 
            "Historical pattern of aggressive claim scrutiny"
        ],
        "high_income": [
            "Access to premium legal representation",
            "Simplified documentation processes",
            "Historical pattern of benefit of doubt"
        ],
        "elderly": [
            "Technology barriers in claim submission",
            "Complex medical documentation requirements",
            "Age-related communication challenges"
        ],
        "minority": [
            "Language barriers in claim processing",
            "Cultural misunderstandings in documentation",
            "Historical pattern of systemic bias"
        ],
        "middle_income": [
            "Moderate access to legal resources",
            "Standard documentation requirements",
            "Balanced historical treatment patterns"
        ]
    }
    
    return bias_factors.get(demographic, ["No specific bias factors identified"])
