import os
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from pi_network import PiNetwork
from ai_engine import AIEngine

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

pi_network = PiNetwork()
ai_engine = AIEngine()

@app.route('/', methods=['GET'])
def index():
    return 'Welcome to Nexaura!'

@app.route('/api/assistant', methods=['POST'])
def assistant():
    user_input = request.get_json()['input']
    response = ai_engine.process_input(user_input)
    return jsonify({'response': response})

@app.route('/api/pi_network', methods=['GET'])
def pi_network_info():
    info = pi_network.get_info()
    return jsonify(info)

@app.route('/api/pi_network/transactions', methods=['GET'])
def pi_network_transactions():
    transactions = pi_network.get_transactions()
    return jsonify(transactions)

@app.route('/api/pi_network/balance', methods=['GET'])
def pi_network_balance():
    balance = pi_network.get_balance()
    return jsonify({'balance': balance})

if __name__ == '__main__':
    app.run(debug=True)
