from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def is_valid_email(email):
    if not email or not email.endswith("@gmail.com"):
        return False
    username = email[:-10]
    if len(username) == 0 or username[0].isdigit():
        return False
    if not re.match(r'^[a-zA-Z0-9]+$', username):
        return False
    return True

def is_valid_national_id(national_id):
    return bool(re.match(r'^[1|2]\d{9}$', national_id))

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()

    email = data.get('email') if data else None
    national_id = data.get('national_id') if data else None

    errors = {}

    if not email:
        errors['email'] = "Email is required."
    elif not is_valid_email(email):
        errors['email'] = "Invalid email format."

    if not national_id:
        errors['national_id'] = "National ID is required."
    elif not is_valid_national_id(national_id):
        errors['national_id'] = "Invalid national ID format."

    if errors:
        return jsonify({
            "status": "fail",
            "valid": False,
            "errors": errors
        }), 400

    return jsonify({
        "status": "success",
        "valid": True,
        "message": "Email and National ID are valid."
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
