import polars as pl

from datetime import datetime

import os

ENDERECO_DADOS = r'./../dados2/'

# try:
#     print('Lendo dados...')
#     inicio = datetime.now()

#     listar_arquivos = []

#     df_auxilio_brasil = None

#     lista_diretorio = os.listdir(ENDERECO_DADOS)

#     for arquivo in lista_diretorio:
#         if arquivo.endswith('.csv'):
#             listar_arquivos.append(arquivo)

#     for arquivo in listar_arquivos:
#         df_aux_br = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')
#         print(df_aux_br.head())

#         if df_auxilio_brasil is None:
#             df_auxilio_brasil = df_aux_br

#         else:
#             df_auxilio_brasil = pl.concat([df_auxilio_brasil, df_aux_br])

#         del df_aux_br

#         print(f'\nProcessamento realizado com sucesso!')
#         print(df_auxilio_brasil.shape)

#     df_auxilio_brasil = df_auxilio_brasil.with_columns(
#         pl.col('VALOR PARCELA')
#         .str.replace(',', '.')
#         .cast(pl.Float64)
#     )

#     print('\nGerando arquivo .parquet...')

#     df_auxilio_brasil.write_parquet(ENDERECO_DADOS + 'auxilio_brasil.parquet')

#     print('\nArquivo gerado com sucesso!')

#     final = datetime.now()
#     print(f'\nTempo total do processo: {final - inicio}')
    
# except Exception as e:
#     print(f'Erro na leitura dos dados {e}')

pl.Config.set_fmt_float("full")

try:
    print('Lendo arquivo .parquet')
    inicio = datetime.now()

    df_auxilio_brasil_parquet = (
        pl.scan_parquet(ENDERECO_DADOS + 'auxilio_brasil.parquet')
            .select(['NOME MUNICÍPIO', 'VALOR PARCELA'])
            .with_columns([
                pl.col('NOME MUNICÍPIO').cast(pl.Categorical)
            ])
            .group_by('NOME MUNICÍPIO')
            .agg(pl.col('VALOR PARCELA').sum())
            .sort('VALOR PARCELA', descending=True)
    )

    df_auxilio_brasil = df_auxilio_brasil_parquet.collect()

    print(df_auxilio_brasil.head(10))
    print(df_auxilio_brasil.columns)

    final = datetime.now()

    print(f'\nFim do processamento: {final - inicio}')


except Exception as e:
    print(f'Erro ao ler o arquivo .parquet')