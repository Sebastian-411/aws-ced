import unittest
from backend.chatbot.backend.bayesian_network import IssuesBayesianNetwork, enumerated_symptoms

class TestIssuesBayesianNetwork(unittest.TestCase):

    def setUp(self):
        self.network = IssuesBayesianNetwork()

    def test_no_symptoms(self):
        symptoms = []
        result = self.network.determine_issues(symptoms)
        self.assertAlmostEqual(result["Cooling_Issue"], 0.5, places=2)
        self.assertAlmostEqual(result["Transmission_Issue"], 0.2, places=2)
        self.assertAlmostEqual(result["Steering_Issue"], 0.3, places=2)
        self.assertAlmostEqual(result["Braking_Issue"], 0.1, places=2)
        self.assertEqual(result["facts"], [])
        self.assertEqual(result["symptoms"], [])

    def test_single_symptom(self):
        symptoms = [1]  # Symptom_Engine_Overheating
        result = self.network.determine_issues(symptoms)
        self.assertGreater(result["Cooling_Issue"], 0.5)
        self.assertEqual(result["facts"], ["Cooling_Issue"])
        self.assertEqual(result["symptoms"], ["Symptom_Engine_Overheating"])

    def test_multiple_symptoms(self):
        symptoms = [1, 2, 3]  # Symptom_Engine_Overheating, Symptom_Weak_Air_Conditioning, Symptom_Fan_Clutch_Failure
        result = self.network.determine_issues(symptoms)
        self.assertGreater(result["Cooling_Issue"], 0.5)
        self.assertEqual(result["facts"], ["Cooling_Issue"])
        self.assertEqual(result["symptoms"], [
            "Symptom_Engine_Overheating",
            "Symptom_Weak_Air_Conditioning",
            "Symptom_Fan_Clutch_Failure"
        ])

    def test_mixed_symptoms(self):
        symptoms = [1, 10, 26, 38]  # Symptoms from different issues
        result = self.network.determine_issues(symptoms)
        self.assertGreater(result["Cooling_Issue"], 0.5)
        self.assertGreater(result["Transmission_Issue"], 0.5)
        self.assertGreater(result["Steering_Issue"], 0.5)
        self.assertGreater(result["Braking_Issue"], 0.5)
        self.assertEqual(set(result["facts"]), {"Cooling_Issue", "Transmission_Issue", "Steering_Issue", "Braking_Issue"})
        self.assertEqual(set(result["symptoms"]), {
            "Symptom_Engine_Overheating",
            "Symptom_Irregular_Gear_Shifting",
            "Symptom_Stiff_Steering_Wheel",
            "Symptom_Worn_Brake_Pads"
        })

if __name__ == '__main__':
    unittest.main()