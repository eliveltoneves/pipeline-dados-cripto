# 📈 Projeto: Coletor de Cotações de Criptomoedas em Tempo Real

Pipeline de dados em Python para coletar cotações de criptomoedas em tempo real usando a API da CoinGecko, armazená-las em CSV e gerar visualizações com gráficos de linha.

---

## 🚀 Descrição Rápida

Este projeto realiza a coleta periódica de preços de criptomoedas como **Bitcoin**, **Ethereum**, **Litecoin**, entre outras, converte os dados em uma estrutura tabular, armazena-os com carimbo de tempo em um arquivo CSV, e permite a visualização da evolução dos preços ao longo do tempo por meio de gráficos com **Matplotlib** e **Seaborn**.

---

## 🛠 Tecnologias Utilizadas

* Python 3.7+
* Pandas
* Requests
* Matplotlib
* Seaborn
* Time / Datetime
* CoinGecko API

---

## ✅ Funcionalidades

* 🔄 Coleta de cotações em tempo real da API CoinGecko
* 🧶 Transformação e estruturação dos dados com timestamp
* 📀 Armazenamento dos dados em `cotacoes_cripto.csv` com append automático e controle de cabeçalho
* ⏱️ Agendamento automatizado de coletas com `time.sleep()` para simular monitoramento contínuo
* 📊 Geração de gráficos:

  * Gráfico de evolução de uma cripto (Matplotlib)
  * Visualização da série temporal de preços com Seaborn (Seaborn)

---

## ⚙️ Como Configurar e Executar

### 📌 Requisitos

* Python 3.7 ou superior instalado

### 📁 Criar Ambiente Virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 📦 Instalar Dependências

```bash
pip install -r requirements.txt
```

### ▶️ Executar o Coletor Principal

```bash
python coletor_dados.py
```

> Esse script coleta os dados periodicamente e salva no CSV.

### 📉 Executar Visualização com Matplotlib

```bash
python vizualizacao_plt.py
```

### 📊 Executar Visualização com Seaborn

```bash
python vizualizacao_sns.py
```

---

## 📂 Estrutura do Projeto

```
├── coletor_dados.py           # Script principal: coleta, transforma e salva os dados
├── vizualizacao_plt.py        # Gráfico de linha com Matplotlib
├── vizualizacao_sns.py        # Gráfico comparativo com Seaborn
├── cotacoes_cripto.csv        # Arquivo onde os dados coletados são salvos
├── requirements.txt           # Lista de dependências do projeto
├── imagens/
│   ├── grafico_matplotlib.png # Imagem gerada com Matplotlib
│   ├── grafico_seaborn.png    # Imagem gerada com Seaborn
└── README.md                  # Documentação do projeto
```

---

## 📌 Exemplo de Saída

### 📾 Exemplo de linha do `cotacoes_cripto.csv`:

```csv
timestamp,cripto,moeda_base,preco
2025-05-30 14:05:02.123456,bitcoin,brl,362500.23
```

### 📊 Visualizações

#### Gráfico Seaborn

![Gráfico Seaborn](/imagens/Figure_2.png)

#### Gráfico Matplotlib

![Gráfico Matplotlib](/imagens/Figure_1.png)

---

## 💡 Possíveis Melhorias Futuras

* 📋 Substituir CSV por banco de dados (Ex: SQLite ou PostgreSQL)
* ☁️ Implantar o pipeline em uma nuvem (ex: AWS Lambda, GCP Cloud Functions)
* 📊 Criar um dashboard interativo com **Streamlit** ou **Dash**
* 🗓️ Agendamento com `APScheduler` ou `cron` para produção
* 🔔 Notificações em tempo real com alertas por e-mail ou Telegram

---

## 📬 Contato

Projeto desenvolvido por **Elivélton Neves de Alcântara**
Sinta-se à vontade para contribuir, sugerir melhorias ou usar como portfólio pessoal! 🚀
