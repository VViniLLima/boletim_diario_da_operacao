import pandas as pd
from carga_horaria import CargaHorariaDf


def collect_carga_horaria(files_list):
    df_carga_horaria = CargaHorariaDf().collect_data(files_list)
    df_carga_horaria = pd.concat(df_carga_horaria)
    df_carga_horaria.to_csv('./output/carga_horaria.csv', index=False)