import pandas as pd
import polars as pl  # 0:00:37.178481

from datetime import datetime

import os

ENDERECO_DADOS = r'./../dados/'

try:
    print('Obtendo dados...')
    inicio = datetime.now()

    # Lisa para guardar cada arquivo que termina em .csv
    # Esta lista que utilizaremos 
    lista_arquivos = []

    df_bolsa_familia = None

    # listar nomes dos arquivos da pasta dados
    lista_dir_arquivos = os.listdir(ENDERECO_DADOS)
    # print(lista_dir_arquivos)

    # Verifica se todos os arquivos são csv
    for arquivo in lista_dir_arquivos:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)

    # Leitura dos arquivos
    for arquivo in lista_arquivos:
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')
        print(df.head())

        # Concatenar (juntar os dataframes)

        if df_bolsa_familia is None:
            df_bolsa_familia = df

        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

        del df

        print(f'\nArquivo {arquivo} processado com sucesso!')
        print(df_bolsa_familia.shape)


    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA')
        .str.replace(',', '.')
        .cast(pl.Float64)
    )

    # Salvando em arquivo Parquet

    print('\nIniciando a gravação do arquivo Parquet...')

    df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    print('\narquivo salvo com sucesso!')        

    final = datetime.now()
    print(f'\nTotal de tempo utilizado: {final - inicio}')

except Exception as e:
    print(f'Erro ao obter dados {e}')