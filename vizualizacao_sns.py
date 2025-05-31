import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

def visualizar_evolucao_preco_seaborn(csv_path, cripto='ethereum', moeda_base='brl'):
    try:
        # Lê o CSV e interpreta a coluna 'timestamp' como datetime
        df = pd.read_csv(csv_path, parse_dates=['timestamp'])

        # Filtrar pelos parâmetros
        df_filtrado = df[(df['cripto'] == cripto) & (df['moeda_base'] == moeda_base)]

        if df_filtrado.empty:
            print(f"Nenhum dado encontrado para {cripto.upper()} em {moeda_base.upper()}.")
            return

        # Ordenar por tempo
        df_filtrado = df_filtrado.sort_values(by='timestamp')

        # Estilo do Seaborn
        sns.set(style="darkgrid", palette="deep")

        # Criar gráfico
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df_filtrado, x='timestamp', y='preco', marker='o')

        plt.title(f'Evolução do Preço - {cripto.capitalize()} ({moeda_base.upper()})', fontsize=16)
        plt.xlabel('Data e Hora', fontsize=12)
        plt.ylabel(f'Preço ({moeda_base.upper()})', fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
if __name__ == "__main__":
    visualizar_evolucao_preco_seaborn('cotacoes_cripto.csv', cripto='ethereum', moeda_base='brl')
