import polars as pl
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime

pl.Config.set_fmt_float("full") # Tira a notação científica do terminal

ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo .parquet')
    inicio = datetime.now()

    # Leitura preguiçosa:

    # with pl.StringCache(): # depreciado, não é mais usado

    df_plano_execucao = (
        pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') #dados
            # Delimitar séries
            .select(['NOME MUNICÍPIO', 'VALOR PARCELA'])
            # --- técnica
            .with_columns([
                # Cria uma tabela de números, substituindo os nomes das cidades
                pl.col('NOME MUNICÍPIO').cast(pl.Categorical)
            ])
            # Agrupar
            .group_by('NOME MUNICÍPIO') #Agrupar
            # Soma
            .agg(pl.col('VALOR PARCELA').sum()) # soma
            # Ordenar
            .sort('VALOR PARCELA', descending=True) 
        )
    
    df_bolsa_familia = df_plano_execucao.collect() # Os dados são carregados aqui

    print(df_bolsa_familia.head(10))
    print(df_bolsa_familia.columns) # Mostrar os nomes das séries

    final = datetime.now()
    
    print(f'Tempo de execução {final - inicio}')
    
except Exception as e:
    print(f"Erro ao ler arquivo .parquet {e}")