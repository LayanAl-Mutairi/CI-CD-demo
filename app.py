from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def is_valid_email(email):
   # Simple validation: starts with a letter, ends with gmail.com only
    pattern = r"^[a-zA-Z][a-zA-Z0-9_.]*@gmail\.com$"
    return re.match(pattern, email) is not None

def is_valid_national_id(national_id):
    # Must start with digit 1 and be exactly 10 digits long
    pattern = r"^[1]\d{9}$"
    return re.match(pattern, national_id) is not None

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json(force=True, silent=True)
    errors = {}

    if not data:
        errors['email'] = "Email is required."
        errors['national_id'] = "National ID is required."
        return jsonify({"valid": False, "errors": errors}), 400

    email = data.get('email')
    national_id = data.get('national_id')

    if not email:
        errors['email'] = "Email is required."
    elif not is_valid_email(email):
        errors['email'] = "Invalid email format."

    if not national_id:
        errors['national_id'] = "National ID is required."
    elif not is_valid_national_id(national_id):
        errors['national_id'] = "Invalid national ID format."

    if errors:
        return jsonify({"valid": False, "errors": errors}), 400

    return jsonify({"valid": True, "message": "Email and National ID are valid."}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
