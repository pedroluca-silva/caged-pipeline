import pandas as pd

def extrair_caged(file_path, uf_codigo=26):
        print(f"Lendo arquivo: {"file_path"}")

        df = pd.read_csv(file_path,
                 sep=";",
                 encoding="UTF-8"
        
        )

        print(f"Total de registros (Brasil): {len(df)}")

        df_uf = df[df["uf"] == uf_codigo].copy()

        print(f"Registros após filtro de UF {uf_codigo}: {len(df_uf)}")

        colunas = [
                "competênciamov",
                "uf",
                "município",
                "seção",
                "saldomovimentação",
                "cbo2002ocupação",
                "graudeinstrução",
                "idade",
                "sexo",
                "salário",
                "tipomovimentação"
        ]

        df_final = df_uf[colunas].copy()

        print(f"Shape final: {df_final.shape}")
        print("\nPrimeiras linhas:")
        print(df_final.head())

        return df_final

if __name__ == "__main__":
        df = extrair_caged("data/raw/CAGEDMOV202301.txt")