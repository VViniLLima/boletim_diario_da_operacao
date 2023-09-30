import pandas as pd
from producao import ProducaoDf


def collect_producao(files_list):
    df_producao = ProducaoDf().collect_data(files_list)
    df_producao = pd.concat(df_producao)
    df_producao.to_csv('./output/producao.csv', index=False)

    