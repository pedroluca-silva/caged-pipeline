# Pipeline CAGED-PE 2023

Pipeline de dados públicos do mercado de trabalho formal de Pernambuco, construído com Python, Google BigQuery e Looker Studio.

## Problema de Negócio

O mercado de trabalho formal brasileiro gera milhões de registros mensais via CAGED (Cadastro Geral de Empregados e Desempregados). Este projeto constrói um pipeline de ingestão desses dados para Pernambuco em janeiro/2023, permitindo análise do saldo de empregos por setor, município e perfil do trabalhador.

## Arquitetura

```
CAGED (MTE) → extract.py → transform.py → load_bigquery.py → Google BigQuery → Looker Studio
```

## Stack

- Python 3.13
- pandas
- google-cloud-bigquery
- pandas-gbq
- pyarrow
- Google BigQuery (free tier — 10 GB storage + 1 TB queries/mês)
- Looker Studio (gratuito, integrado ao BigQuery)

## Estrutura do Repositório

```
caged-pipeline/
├── src/
│   ├── explore.py        # Exploração inicial dos dados brutos
│   ├── extract.py        # Leitura e filtro por UF
│   ├── transform.py      # Limpeza, renomeação e tipagem
│   └── load_bigquery.py  # Carga no Google BigQuery
├── data/
│   └── sample/
├── docs/
├── .gitignore
├── requirements.txt
└── README.md
```

## Como Executar

```bash
# 1. Clonar o repositório
git clone https://github.com/pedroluca-silva/caged-pipeline.git
cd caged-pipeline

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar credenciais do Google Cloud
# Salve sua chave JSON fora do repositório e defina a variável de ambiente:
# Windows (PowerShell):
$env:GOOGLE_APPLICATION_CREDENTIALS = "C:\Users\seu-usuario\.gcp\caged-pipeline-key.json"

# 4. Baixar o arquivo do CAGED
# Acesse http://pdet.mte.gov.br/caged e baixe CAGEDMOV202301.7z
# Extraia o .txt para data/raw/

# 5. Executar o pipeline completo
python src/load_bigquery.py
```

## Dashboard

Acesse o dashboard interativo com os dados de Pernambuco — janeiro/2023:

🔗 https://datastudio.google.com/reporting/932138cc-c6f8-444d-b6e1-91b68525e75f

**Visualizações disponíveis:**
- Saldo líquido de empregos (admissões − demissões)
- Saldo por setor econômico (CNAE)
- Distribuição por grau de instrução
- Top municípios por saldo de emprego

## Decisões Técnicas

**Filtro por UF antes da carga**
O arquivo mensal do CAGED contém dados de todo o Brasil (~3,6 milhões de registros). O filtro por Pernambuco (UF = 26) é aplicado antes da carga, reduzindo o volume para ~91 mil registros e respeitando os limites do free tier do BigQuery.

**WRITE_TRUNCATE na carga**
A configuração `write_disposition=WRITE_TRUNCATE` apaga e reescreve a tabela a cada execução, garantindo idempotência — o pipeline pode ser reprocessado sem duplicar dados.

**Encoding UTF-8**
O Novo CAGED (pós-2020) utiliza encoding UTF-8. Arquivos anteriores a 2020 usam latin-1. Essa distinção é relevante para qualquer pipeline que processe séries históricas do CAGED.

**Credenciais fora do repositório**
A chave da Service Account é armazenada em `~/.gcp/` e referenciada via variável de ambiente `GOOGLE_APPLICATION_CREDENTIALS`, nunca commitada no repositório.

## Aprendizados

- Ingestão de dados públicos do governo com Python e pandas
- Carga de DataFrames no Google BigQuery via API oficial
- Tratamento de encoding e tipos de dados em arquivos do MTE
- Criação de dashboards analíticos conectados a data warehouse real
- Boas práticas de segurança com credenciais em projetos de dados
- Versionamento de projetos de dados com Git e Conventional Commits

## Fonte dos Dados

Ministério do Trabalho e Emprego — Novo CAGED
http://pdet.mte.gov.br/caged