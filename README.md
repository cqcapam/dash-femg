# 📊 dash-femg

Dashboard interativo feito em **Python** com **Streamlit** para visualização de dados de ferro e manganes.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red?logo=streamlit)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)

---

## 🚀 Como executar

Para rodar localmente:

```bash
git clone https://github.com/cqcapam/dash-femg.git
cd dash-femg
pip install -r requirements.txt
streamlit run app.py
```


## 🔄 Atualização dos dados

Os dados estão localizados no arquivo:

datas/newdf.parquet

Para atualizar as análises do dashboard, basta substituir esse arquivo por uma nova versão com o mesmo nome e estrutura.

## 📁 Estrutura do projeto

📦 dash-femg
├── app.py               # Arquivo principal do Streamlit
├── datas/
│   └── newdf.parquet    # Dados em formato parquet
├── pages/
│   └── dashboard.py     # Página com os gráficos principais
├── requirements.txt     # Dependências do projeto
└── README.md            # Você está aqui :)


## 🛠️ Tecnologias utilizadas

* [Python 3.10+](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Pandas]()
* [Plotly]()


## 👩‍💻 Desenvolvido por Jade Pereira
