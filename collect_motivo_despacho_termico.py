import pandas as pd
from motivo_despacho_termico import MotivoDespachoDf


def collect_despacho(files_list):
    despacho_df = MotivoDespachoDf().collect_data(files_list)
    despacho_df = pd.concat(despacho_df)
    despacho_df.to_csv('./output/motivo_despacho_termico.csv', index=False)