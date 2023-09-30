import pandas as pd
from energia_natural_afluente import EnergiaNaturalAfluenteDf


def collect_energia_natural_afluente(files_list):
    df_energia_natural = EnergiaNaturalAfluenteDf().collect_data(files_list)
    df_energia_natural = pd.concat(df_energia_natural)
    df_energia_natural.to_csv('./output/energia_natural_afluente.csv', index=False)