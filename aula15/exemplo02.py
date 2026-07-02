# pip install fastparquet (para ler arquivos .parquet)

import pandas as pd #0:00:27.919616
import polars as pl #0:00:08.055587

from datetime import datetime

ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo .parquet')
    inicio = datetime.now()

    # Leitura direta
    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    # print(df_bolsa_familia.head())
    
    df_filtrado = df_bolsa_familia.filter(pl.col('VALOR PARCELA') > 2500)

    print(df_filtrado.shape)
    
    # print(df_bolsa_familia.sort('VALOR PARCELA', descending=True).head(20))

    

    final = datetime.now()
    print(f'\nTotal de tempo utilizado: {final - inicio}')

except Exception as e:
    print(f"Erro ao ler arquivo .parquet {e}")