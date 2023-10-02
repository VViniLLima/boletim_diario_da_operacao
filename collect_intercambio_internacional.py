import pandas as pd
from intercambio_internacional import IntercambioInternacionalDf
from constants import SHEET_BALANCO_DIARIO, SHEETS_BALANCO_ACUMULADO

def collect_intercambio(files_list, sheet=SHEETS_BALANCO_ACUMULADO):
            
    df_intercambio_internacional = IntercambioInternacionalDf().collect_data(files_list, sheet)
    df_intercambio = pd.concat(df_intercambio_internacional)
    df_intercambio.to_csv(f'./output/intercambio_internacional_acumulado.csv', index=False)