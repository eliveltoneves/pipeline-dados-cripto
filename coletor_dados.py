import requests
import pandas as pd
from datetime import datetime
import time
import os

def obter_cotacoes_api(moedas, moedas_base):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': ','.join(moedas),
        'vs_currencies': ','.join(moedas_base)
    }

    try:
        resposta = requests.get(url, params=params, timeout=10)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.Timeout:
        print(f"[{datetime.now()}] [TIMEOUT] A API demorou demais para responder.")
        return None
    except requests.RequestException as erro:
        print(f"[{datetime.now()}] [ERRO] Requisição falhou: {erro}")
        return None

def transformar_dados(dados_api, moedas_base_comparacao):
    timestamp = datetime.now()
    lista_registros = []

    for cripto_id, valores in dados_api.items():
        for moeda_base in moedas_base_comparacao:
            preco = valores.get(moeda_base)
            if preco is not None:
                registro = {
                    'timestamp': timestamp,
                    'cripto': cripto_id,
                    'moeda_base': moeda_base,
                    'preco': preco
                }
                lista_registros.append(registro)

    return lista_registros

def salvar_dados_csv(df, nome_arquivo):
    arquivo_existe = os.path.exists(nome_arquivo)
    df.to_csv(
        nome_arquivo,
        mode='a',
        header=not arquivo_existe,
        index=False,
        encoding='utf-8'
    )

def executar_pipeline(criptos, moedas_base, nome_arquivo_csv):
    print(f"[{datetime.now()}] Iniciando coleta...")

    dados_api = obter_cotacoes_api(criptos, moedas_base)

    if dados_api:
        dados_transformados = transformar_dados(dados_api, moedas_base)
        if dados_transformados:
            df_cotacoes = pd.DataFrame(dados_transformados)
            df_cotacoes = df_cotacoes[['timestamp', 'cripto', 'moeda_base', 'preco']]

            print(df_cotacoes)  # Exibe os dados coletados
            salvar_dados_csv(df_cotacoes, nome_arquivo_csv)
            print(f"[{datetime.now()}] ✅ Dados salvos com sucesso.\n")
        else:
            print(f"[{datetime.now()}] [AVISO] Nenhum dado transformado.")
    else:
        print(f"[{datetime.now()}] [ERRO] Nenhum dado retornado da API.\n")

if __name__ == "__main__":
    criptos = ['bitcoin', 'ethereum', 'solana']
    moedas_base = ['brl', 'usd', 'eur']
    nome_arquivo_csv = 'cotacoes_cripto.csv'
    intervalo_segundos = 60  # ajuste para 10 ou 20 segundos para testes

    print(f"Iniciando monitoramento a cada {intervalo_segundos} segundos...\n")
    try:
        while True:
            executar_pipeline(criptos, moedas_base, nome_arquivo_csv)
            time.sleep(intervalo_segundos)
    except KeyboardInterrupt:
        print("\n⏹️ Execução interrompida manualmente. Encerrando monitoramento.")
