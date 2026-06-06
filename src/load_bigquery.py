from google.cloud import bigquery
import pandas as pd
from extract import extrair_caged
from transform import transformar_caged

def carregar_bigquery(df, project_id, dataset_id, table_id):
    client = bigquery.Client(project=project_id)
    
    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig (
        write_disposition="WRITE_TRUNCATE"
    )

    print(f"Carregando {len(df)} registros em {table_ref}...")

    job = client.load_table_from_dataframe(
        df, table_ref, job_config=job_config
    )
    job.result()

    print(f"Carga concluída com sucesso!")
    print(f"Tabela: {table_ref}")

if __name__ == "__main__":
    df_bruto = extrair_caged("data/raw/CAGEDMOV202301.txt")
    df_transformado = transformar_caged(df_bruto)

    carregar_bigquery(
        df=df_transformado,
        project_id="caged-pipeline",
        dataset_id="mercado_trabalho",
        table_id="caged_pe_2023"
    )