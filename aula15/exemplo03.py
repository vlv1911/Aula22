# pip install fastparquet (para ler arquivos .parquet)

# import pandas as pd
import polars as pl
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime

ENDERECO_DADOS = r'./../dados/'

try:
    print('Lendo arquivo .parquet')
    inicio = datetime.now()

    # Leitura preguiçosa:
    df_plano_execucao = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    df_bolsa_familia = df_plano_execucao.collect()

    print(df_bolsa_familia.head(10))
    
   
    
except Exception as e:
    print(f"Erro ao ler arquivo .parquet {e}")

try:
    # Array
    array_valor_parcela = np.array(df_bolsa_familia['VALOR PARCELA'])

except Exception as e:
    print(f"Erro ao obter o array {e}")

try:
    plt.boxplot(array_valor_parcela, vert=False)    
    plt.title('Distribuição bolsa família')
    
    final = datetime.now()
    print(f'\nTotal de tempo utilizado: {final - inicio}')
    
    plt.show()


except Exception as e:
    print(f"Erro ao gerar gráfico {e}")