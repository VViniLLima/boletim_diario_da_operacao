import pandas as pd
from balanco_diario import BalancoDiarioDf
from constants import SHEET_BALANCO_DIARIO, SHEETS_BALANCO_ACUMULADO

def collect_balanco(files_list, sheet=SHEETS_BALANCO_ACUMULADO):
            
    df_diario_regiao = BalancoDiarioDf().collect_data(files_list, sheet)
    df_regiao = pd.concat(df_diario_regiao)
    df_regiao.to_csv(f'./output/balanco_energia_acumulado.csv', index=False)