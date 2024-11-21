from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

enumerated_symptoms = {
    1: "Symptom_Engine_Overheating",
    2: "Symptom_Weak_Air_Conditioning",
    3: "Symptom_Fan_Clutch_Failure",
    4: "Symptom_Refrigerant_Leak",
    5: "Symptom_Damaged_Radiator_Fins",
    6: "Symptom_Heater_Core_Issues",
    7: "Symptom_Coolant_Smoke",
    8: "Symptom_Engine_Shutdown_Heat",
    9: "Symptom_High_Cabin_Air_Temperature",
    10: "Symptom_Irregular_Gear_Shifting",
    11: "Symptom_Clutch_Slipping",
    12: "Symptom_Engine_Acceleration",
    13: "Symptom_Harsh_Shifting",
    14: "Symptom_Grinding_Transmission_Noise",
    15: "Symptom_Poor_Acceleration",
    16: "Symptom_Stuck_Manual_Gear_Shift",
    17: "Symptom_Difficulty_Engaging_Gears",
    18: "Symptom_Transmission_Fluid_Leak",
    19: "Symptom_Delayed_Transmission_Response",
    20: "Symptom_Gears_Not_Engaging",
    21: "Symptom_Shifting_Delay",
    22: "Symptom_Transmission_Overheating",
    23: "Symptom_Transmission_Slipping_Acceleration",
    24: "Symptom_Loss_of_Power_Gear_Shifting",
    25: "Symptom_Unusual_Smell_Acceleration",
    26: "Symptom_Stiff_Steering_Wheel",
    27: "Symptom_Steering_Wheel_Vibration",
    28: "Symptom_Steering_Wheel_Pulling",
    29: "Symptom_Steering_Column_Noise",
    30: "Symptom_Excessive_Steering_Play",
    31: "Symptom_Heavy_Steering_Wheel",
    32: "Symptom_Misaligned_Steering_Wheel",
    33: "Symptom_Steering_Fluid_Leak",
    34: "Symptom_Difficulty_Turning_Steering_Wheel",
    35: "Symptom_Steering_Wheel_Vibration_Acceleration",
    36: "Symptom_Less_Responsive_Steering",
    37: "Symptom_Squealing_Noise_Turning",
    38: "Symptom_Worn_Brake_Pads",
    39: "Symptom_Stuck_Brake_Pedal",
    40: "Symptom_Flashing_Brake_Light",
    41: "Symptom_Lack_of_Brake_Response",
    42: "Symptom_Vibration_When_Stopping",
    43: "Symptom_Soft_Brake_Pedal",
    44: "Symptom_Contaminated_Brake_Fluid",
    45: "Symptom_ABS_Light_On",
    46: "Symptom_Brake_Fading_With_Heavy_Use",
    47: "Symptom_Squealing_Brakes_When_Cold",
    48: "Symptom_Grinding_Feel_Brakes",
    49: "Symptom_Failure_to_Stop_Quickly",
    50: "Symptom_Brake_Line_Leak",
    51: "Symptom_Whistling_Noise_When_Pressing_Brake",
    52: "Symptom_Excessive_Brake_Pedal_Travel",
    53: "Symptom_Hard_Brake_Pedal",
    54: "Symptom_ABS_Failure"
}


class IssuesBayesianNetwork():
    def __init__(self):

        self.model = BayesianNetwork()

        edges = []
        
        symptoms_problem = {
            # symptom | issue
            # f is the probability of having the symptom without having a cooling problem
            # t is the probability of having the symptom with a cooling problem
            "Symptom_Engine_Overheating": {"Cooling_Issue": {"f": 0.05, "t": 0.85}},
            "Symptom_Weak_Air_Conditioning": {"Cooling_Issue": {"f": 0.10, "t": 0.75}},
            "Symptom_Fan_Clutch_Failure": {"Cooling_Issue": {"f": 0.12, "t": 0.78}},
            "Symptom_Refrigerant_Leak": {"Cooling_Issue": {"f": 0.08, "t": 0.80}},
            "Symptom_Damaged_Radiator_Fins": {"Cooling_Issue": {"f": 0.18, "t": 0.70}},
            "Symptom_Heater_Core_Issues": {"Cooling_Issue": {"f": 0.20, "t": 0.72}},
            "Symptom_Coolant_Smoke": {"Cooling_Issue": {"f": 0.05, "t": 0.90}},
            "Symptom_Engine_Shutdown_Heat": {"Cooling_Issue": {"f": 0.10, "t": 0.85}},
            "Symptom_High_Cabin_Air_Temperature": {"Cooling_Issue": {"f": 0.15, "t": 0.80}},

            "Symptom_Irregular_Gear_Shifting": {"Transmission_Issue": {"f": 0.25, "t": 0.78}},
            "Symptom_Clutch_Slipping": {"Transmission_Issue": {"f": 0.20, "t": 0.85}},
            "Symptom_Engine_Acceleration": {"Transmission_Issue": {"f": 0.30, "t": 0.80}},
            "Symptom_Harsh_Shifting": {"Transmission_Issue": {"f": 0.18, "t": 0.82}},
            "Symptom_Grinding_Transmission_Noise": {"Transmission_Issue": {"f": 0.10, "t": 0.88}},
            "Symptom_Poor_Acceleration": {"Transmission_Issue": {"f": 0.20, "t": 0.80}},
            "Symptom_Stuck_Manual_Gear_Shift": {"Transmission_Issue": {"f": 0.15, "t": 0.85}},
            "Symptom_Difficulty_Engaging_Gears": {"Transmission_Issue": {"f": 0.12, "t": 0.88}},
            "Symptom_Transmission_Fluid_Leak": {"Transmission_Issue": {"f": 0.07, "t": 0.85}},
            "Symptom_Delayed_Transmission_Response": {"Transmission_Issue": {"f": 0.15, "t": 0.82}},
            "Symptom_Gears_Not_Engaging": {"Transmission_Issue": {"f": 0.10, "t": 0.90}},
            "Symptom_Shifting_Delay": {"Transmission_Issue": {"f": 0.18, "t": 0.80}},
            "Symptom_Transmission_Overheating": {"Transmission_Issue": {"f": 0.08, "t": 0.85}},
            "Symptom_Transmission_Slipping_Acceleration": {"Transmission_Issue": {"f": 0.20, "t": 0.78}},
            "Symptom_Loss_of_Power_Gear_Shifting": {"Transmission_Issue": {"f": 0.22, "t": 0.80}},
            "Symptom_Unusual_Smell_Acceleration": {"Transmission_Issue": {"f": 0.25, "t": 0.75}},

            "Symptom_Stiff_Steering_Wheel": {"Steering_Issue": {"f": 0.15, "t": 0.80}},
            "Symptom_Steering_Wheel_Vibration": {"Steering_Issue": {"f": 0.20, "t": 0.75}},
            "Symptom_Steering_Wheel_Pulling": {"Steering_Issue": {"f": 0.18, "t": 0.78}},
            "Symptom_Steering_Column_Noise": {"Steering_Issue": {"f": 0.25, "t": 0.70}},
            "Symptom_Excessive_Steering_Play": {"Steering_Issue": {"f": 0.22, "t": 0.76}},
            "Symptom_Heavy_Steering_Wheel": {"Steering_Issue": {"f": 0.15, "t": 0.82}},
            "Symptom_Misaligned_Steering_Wheel": {"Steering_Issue": {"f": 0.10, "t": 0.88}},
            "Symptom_Steering_Fluid_Leak": {"Steering_Issue": {"f": 0.08, "t": 0.90}},
            "Symptom_Difficulty_Turning_Steering_Wheel": {"Steering_Issue": {"f": 0.12, "t": 0.85}},
            "Symptom_Steering_Wheel_Vibration_Acceleration": {"Steering_Issue": {"f": 0.18, "t": 0.80}},
            "Symptom_Less_Responsive_Steering": {"Steering_Issue": {"f": 0.25, "t": 0.75}},
            "Symptom_Squealing_Noise_Turning": {"Steering_Issue": {"f": 0.20, "t": 0.80}},

            "Symptom_Worn_Brake_Pads": {"Braking_Issue": {"f": 0.10, "t": 0.88}},
            "Symptom_Stuck_Brake_Pedal": {"Braking_Issue": {"f": 0.05, "t": 0.90}},
            "Symptom_Flashing_Brake_Light": {"Braking_Issue": {"f": 0.12, "t": 0.85}},
            "Symptom_Lack_of_Brake_Response": {"Braking_Issue": {"f": 0.18, "t": 0.82}},
            "Symptom_Vibration_When_Stopping": {"Braking_Issue": {"f": 0.20, "t": 0.78}},
            "Symptom_Soft_Brake_Pedal": {"Braking_Issue": {"f": 0.15, "t": 0.80}},
            "Symptom_Contaminated_Brake_Fluid": {"Braking_Issue": {"f": 0.10, "t": 0.85}},
            "Symptom_ABS_Light_On": {"Braking_Issue": {"f": 0.12, "t": 0.85}},
            "Symptom_Brake_Fading_With_Heavy_Use": {"Braking_Issue": {"f": 0.18, "t": 0.80}},
            "Symptom_Squealing_Brakes_When_Cold": {"Braking_Issue": {"f": 0.22, "t": 0.75}},
            "Symptom_Grinding_Feel_Brakes": {"Braking_Issue": {"f": 0.12, "t": 0.88}},
            "Symptom_Failure_to_Stop_Quickly": {"Braking_Issue": {"f": 0.08, "t": 0.90}},
            "Symptom_Brake_Line_Leak": {"Braking_Issue": {"f": 0.05, "t": 0.90}},
            "Symptom_Whistling_Noise_When_Pressing_Brake": {"Braking_Issue": {"f": 0.10, "t": 0.85}},
            "Symptom_Excessive_Brake_Pedal_Travel": {"Braking_Issue": {"f": 0.18, "t": 0.80}},
            "Symptom_Hard_Brake_Pedal": {"Braking_Issue": {"f": 0.20, "t": 0.75}},
            "Symptom_ABS_Failure": {"Braking_Issue": {"f": 0.10, "t": 0.90}}
            }

        for symptom, issues in symptoms_problem.items():
            for issue, _ in issues.items():        
                edges.append((issue, symptom))

        self.model.add_edges_from(edges)

        self.model.add_nodes_from([issue for issue in issues.keys()])

        cpds = []
        
        issues = {
            'Cooling_Issue': 0.5, 
            'Transmission_Issue': 0.2, 
            'Steering_Issue': 0.3, 
            'Braking_Issue': 0.1
        }

        for issue, prob in issues.items():
            cpd = TabularCPD(variable=issue, variable_card=2, values=[[1 - prob], [prob]])
            cpds.append(cpd)
    

        for symptom, issues in symptoms_problem.items():
            for issue, probabilities in issues.items():
                
                probF = probabilities.get("f")
                probT = probabilities.get("t")
                
                cpd = TabularCPD(
                    variable=symptom,
                    variable_card=2,
                    values=[[1 - probF, 1 - probT],
                            [probF, probT]],     
                    evidence=[issue],
                    evidence_card=[2]
                )
    
            cpds.append(cpd)
    
        self.model.add_cpds(*cpds)

        self.model.check_model()
        
    def determine_issues(self, symptoms):
        inference = VariableElimination(self.model)
        
        evidence = {
            enumerated_symptoms[symptom]:1 for symptom in symptoms 
        }

        probability_cooling_issue = inference.query(
            variables=["Cooling_Issue"],
            evidence=evidence
        ).values[1]
        
        probability_transmission_issue = inference.query(
            variables=["Transmission_Issue"],
            evidence=evidence
        ).values[1]
        
        probability_steering_issue = inference.query(
            variables=["Steering_Issue"],
            evidence=evidence
        ).values[1]
        
        probability_braking_issue = inference.query(
            variables=["Braking_Issue"],
            evidence=evidence
        ).values[1]
        
        return {
            "Cooling_Issue": probability_cooling_issue,
            "Transmission_Issue": probability_transmission_issue,
            "Steering_Issue": probability_steering_issue,
            "Braking_Issue": probability_braking_issue,
            "facts": [
                fact
                for fact in [
                    "Cooling_Issue" if probability_cooling_issue > 0.5 else "",
                    "Transmission_Issue" if probability_transmission_issue > 0.5 else "",
                    "Steering_Issue" if probability_steering_issue > 0.5 else "",
                    "Braking_Issue" if probability_braking_issue > 0.5 else ""
                ]
                if fact != ""
                ],
            "symptoms": [
                enumerated_symptoms[symptom] for symptom in symptoms 
            ]
        }