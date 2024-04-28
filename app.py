import datetime
from flask import Flask, request, jsonify, make_response
import pandas as pd
import csv



app = Flask(__name__)

app.config["JSON_SORT_KEYS"] = False

@app.route('/api/v1/atendimentos', methods=['GET'])
def atendimentos():
    
    df = pd.read_csv('bd/atendimentos.csv',)
    # Exclusão da coluna unnamed
    df = df.drop('Unnamed: 0',axis=1)
    # Tratamento de datas de formatos diferentes    
    df['data_atendimento'] = pd.to_datetime(df['data_atendimento']).dt.date
    # requisito de tipo data string  
    df['data_atendimento'] = df['data_atendimento'].astype(str)    

    # Pegando argumentos de filtro
    condicao_saude = request.args.get('condicao_saude', type=str ,default=None)
    data_atendimento = request.args.get('data_atendimento',type=str ,default=None)           
    unidade = request.args.get('unidade', type=str ,default=None)   


    if condicao_saude:
        df= df.loc[(df['condicao_saude'] == condicao_saude)]
    if data_atendimento:
        df= df.loc[(df['data_atendimento'] == data_atendimento)]
    if unidade:
        df= df.loc[(df['UNIDADE']==unidade)]
    
    return jsonify(df.to_dict(orient='records'))
   




if __name__ == '__main__':
    app.run(debug=True)