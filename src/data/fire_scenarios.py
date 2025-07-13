"""
Fire scenario data for the Gabrielino assessment system.
"""

# Default fire scenario for demonstrations
FIRE_SCENARIO = {
    "incident_id": "CA-LAC-000124",
    "name": "Eaton Fire Complex",
    "location": "Altadena, CA",
    "severity": "EXTREME",
    "containment": 15,
    "evacuation": "MANDATORY",
    "structures_threatened": 8000,
    "acres_burned": 13500,
    "wind_speed": 70,
    "humidity": 6,
    "temperature": 86,
}

# Collection of different fire scenarios for testing
FIRE_SCENARIOS = {
    "eaton_fire": FIRE_SCENARIO,
    
    "moderate_fire": {
        "incident_id": "CA-LAC-000125",
        "name": "Mountain View Fire",
        "location": "Pasadena, CA",
        "severity": "HIGH",
        "containment": 45,
        "evacuation": "ADVISORY",
        "structures_threatened": 2000,
        "acres_burned": 3500,
        "wind_speed": 25,
        "humidity": 15,
        "temperature": 78,
    },
    
    "controlled_fire": {
        "incident_id": "CA-LAC-000126",
        "name": "Oak Grove Fire",
        "location": "La Cañada Flintridge, CA",
        "severity": "MODERATE",
        "containment": 75,
        "evacuation": "NONE",
        "structures_threatened": 500,
        "acres_burned": 800,
        "wind_speed": 10,
        "humidity": 25,
        "temperature": 72,
    },
    
    "historic_fire": {
        "incident_id": "CA-LAC-000127",
        "name": "Thomas Fire Simulation",
        "location": "Ventura County, CA",
        "severity": "EXTREME",
        "containment": 5,
        "evacuation": "MANDATORY",
        "structures_threatened": 15000,
        "acres_burned": 281893,
        "wind_speed": 85,
        "humidity": 3,
        "temperature": 92,
    }
}


def get_fire_scenario(scenario_name: str = "eaton_fire"):
    """
    Get a fire scenario by name.
    
    Args:
        scenario_name: Name of the scenario to retrieve
        
    Returns:
        Fire scenario dictionary
        
    Raises:
        KeyError: If scenario name not found
    """
    if scenario_name not in FIRE_SCENARIOS:
        raise KeyError(f"Fire scenario '{scenario_name}' not found. Available: {list(FIRE_SCENARIOS.keys())}")
    
    return FIRE_SCENARIOS[scenario_name]


def create_custom_scenario(**kwargs):
    """
    Create a custom fire scenario with default values.
    
    Args:
        **kwargs: Fire scenario parameters
        
    Returns:
        Fire scenario dictionary with custom values
    """
    default_scenario = {
        "incident_id": "CA-CUSTOM-001",
        "name": "Custom Fire",
        "location": "California",
        "severity": "MODERATE",
        "containment": 50,
        "evacuation": "ADVISORY",
        "structures_threatened": 1000,
        "acres_burned": 1000,
        "wind_speed": 20,
        "humidity": 15,
        "temperature": 75,
    }
    
    default_scenario.update(kwargs)
    return default_scenario
