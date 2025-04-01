from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to send requests to backend

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///queries.db'
db = SQLAlchemy(app)

class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(100), nullable=False)
    teacher_id = db.Column(db.String(100), nullable=False)
    query = db.Column(db.Text, nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/save_query', methods=['POST'])
def save_query():
    data = request.get_json()
    new_query = Query(student_id=data['Student_ID'], teacher_id=data['Teacher_ID'], query=data['Query'])
    db.session.add(new_query)
    db.session.commit()
    return jsonify({"message": "Query saved successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
