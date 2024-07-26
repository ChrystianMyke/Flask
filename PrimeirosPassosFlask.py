from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/index", methods=['GET'])
def index():
  with open("planilha.json", 'r') as arquivo:
    planilha = json.load(arquivo)
    
  return jsonify(planilha)

if __name__ == '__main__':
  app.run(debug=True)
  