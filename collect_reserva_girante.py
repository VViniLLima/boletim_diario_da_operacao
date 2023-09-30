import pandas as pd
from reserva_girante import ReservaGiranteDf


def collect_reserva_girante(files_list):
    df_reserva_girante = ReservaGiranteDf().collect_data(files_list)
    df_reserva_girante = pd.concat(df_reserva_girante)
    df_reserva_girante.to_csv('./output/reserva_girante.csv', index=False)