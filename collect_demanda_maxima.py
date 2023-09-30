import pandas as pd
from demanda_maxima import DemandaMaximaDf


def collect_demanda_maxima(files_list):
    df_demanda_maxima = DemandaMaximaDf().collect_data(files_list)
    df_demanda_maxima = pd.concat(df_demanda_maxima)
    df_demanda_maxima.to_csv('./output/demanda_maxima.csv', index=False)