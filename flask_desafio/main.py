from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/') 
def index():
    return {'message': 'Welcome to Api flask!'}

@app.route("/excel_to_json", methods=['GET', 'POST'])
def excel_to_json():
    # Lê o arquivo xlsx na mesma pasta do arquivo main.py
    df = pd.read_excel("flask_desafio/pessoas.xlsx")
    # Converte o DataFrame em dicionario
    data = df.to_dict(orient="records")
    # Retorna o json como resposta
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)