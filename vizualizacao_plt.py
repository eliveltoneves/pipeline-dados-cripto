import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def visualizar_evolucao_preco(csv_path, cripto='bitcoin', moeda_base='brl'):
    try:
        df = pd.read_csv(csv_path, parse_dates=['timestamp'])

        # Filtrar por cripto e moeda base
        df_filtrado = df[(df['cripto'] == cripto) & (df['moeda_base'] == moeda_base)]

        if df_filtrado.empty:
            print(f"Nenhum dado encontrado para {cripto.upper()} em {moeda_base.upper()}.")
            return

        # Ordenar por tempo para o gráfico ficar correto
        df_filtrado = df_filtrado.sort_values(by='timestamp')

        # Plot
        plt.figure(figsize=(10, 5))
        plt.plot(df_filtrado['timestamp'], df_filtrado['preco'], marker='o', linestyle='-')
        plt.title(f"Evolução do Preço - {cripto.capitalize()} ({moeda_base.upper()})")
        plt.xlabel('Data e Hora')
        plt.ylabel(f'Preço ({moeda_base.upper()})')
        plt.grid(True)
        plt.xticks(rotation=45)

        # Formatar eixo X com datas amigáveis
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %H:%M'))
        plt.tight_layout()

        plt.show()

    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
if __name__ == "__main__":
    visualizar_evolucao_preco('cotacoes_cripto.csv', cripto='bitcoin', moeda_base='brl')
