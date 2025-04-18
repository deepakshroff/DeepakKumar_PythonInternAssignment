from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apps.db'
db = SQLAlchemy(app)

class AppModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'app_name': self.app_name,
            'version': self.version,
            'description': self.description
        }

@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.get_json()
    new_app = AppModel(app_name=data['app_name'], version=data['version'], description=data['description'])
    db.session.add(new_app)
    db.session.commit()
    return jsonify({'message': 'App added successfully!'}), 201

@app.route('/get-app/<int:app_id>', methods=['GET'])
def get_app(app_id):
    app_obj = AppModel.query.get(app_id)
    if app_obj:
        return jsonify(app_obj.to_dict())
    return jsonify({'error': 'App not found'}), 404

@app.route('/delete-app/<int:app_id>', methods=['DELETE'])
def delete_app(app_id):
    app_obj = AppModel.query.get(app_id)
    if app_obj:
        db.session.delete(app_obj)
        db.session.commit()
        return jsonify({'message': 'App deleted successfully'})
    return jsonify({'error': 'App not found'}), 404

if __name__ == '__main__':
    if not os.path.exists('apps.db'):
        db.create_all()
    app.run(debug=True)