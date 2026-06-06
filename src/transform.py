import pandas as pd

def transformar_caged (df):
    print("Iniciando transformações...")

    df = df.rename(columns={
        "competênciamov": "competencia",
        "uf": "uf",
        "município": "municipio",
        "seção": "secao_cnae",
        "saldomovimentação": "saldo_movimentacao",
        "cbo2002ocupação": "cbo_ocupacao",
        "graudeinstrução": "grau_instrucao",
        "idade": "idade",
        "sexo": "sexo",
        "salário": "salario",
        "tipomovimentação": "tipo_movimentacao"
    })
    
    df["data_referencia"] = pd.to_datetime(
        df["competencia"].astype(str), format="%Y%m"
    )

    df["salario"] = df["salario"].fillna(0)
    df["salario"] = df["salario"].astype(str).str.replace(",",".").astype(float)
    df["idade"] = pd.to_numeric(df["idade"], errors="coerce").fillna(0)

    df["municipio"] = df["municipio"].astype(str)
    df["cbo_ocupacao"] = df["cbo_ocupacao"].astype(str)

    print(f"Shape após transformação: {df.shape}")
    print("\nColunas finais: ", df.columns.tolist())
    print("\nTipos:\n", df.dtypes)

    return df

if __name__ == "__main__":
    from extract import extrair_caged

    df_bruto = extrair_caged("data/raw/CAGEDMOV202301.txt")
    df_transformado = transformar_caged(df_bruto)
    print("\nPrimeiras linhas transformadas:")
    print(df_transformado.head())