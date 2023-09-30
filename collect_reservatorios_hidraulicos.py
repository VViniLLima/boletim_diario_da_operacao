import pandas as pd
from reservatorios_hidraulicos import ReservatoriosHidraulicos

def collect_reservatorios(files_list):
    df_reservatorios = ReservatoriosHidraulicos().collect_data(files_list)
    df_reservatorios = pd.concat(df_reservatorios)
    df_reservatorios.to_csv('./output/reservatorios.csv', index=False)