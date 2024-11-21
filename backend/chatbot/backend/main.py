from flask import Flask, request, jsonify

from bayesian_network import IssuesBayesianNetwork
from engine import GeneralEngine
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/diagnostic', methods=['POST'])
def process_numbers():
    data = request.get_json()
    
    if 'symptoms' not in data:
        return jsonify({'error': 'symptoms not found'}), 400
    
    symptoms = data['symptoms']
    
    if not all(isinstance(num, (int, float)) for num in symptoms):
        return jsonify({'error': 'symptoms format not correct'}), 400
    
    issuesBayesianNetwork = IssuesBayesianNetwork()
    
    
    return jsonify(GeneralEngine().make_recommendations(issuesBayesianNetwork.determine_issues(symptoms))), 200

if __name__ == '__main__':
    app.run(debug=True)
