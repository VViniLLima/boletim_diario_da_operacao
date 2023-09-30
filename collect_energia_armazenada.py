import pandas as pd
from energia_armazenada import EnergiaArmazenadaDf

def collect_energia_armazenada(files_list):
    df_energia_armazenada = EnergiaArmazenadaDf().collect_data(files_list)
    df_energia_armazenada = pd.concat(df_energia_armazenada)
    df_energia_armazenada.to_csv('./output/energia_armazenada.csv', index=False)