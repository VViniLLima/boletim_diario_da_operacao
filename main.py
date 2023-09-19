import pandas as pd
from convert_xlsx_files import XLSXFiles
from constants import IMPUT_PATH, SHEETS
from collect_region_data import CollectBalancoDiario

def main():
    files_list = XLSXFiles().get_files_list(IMPUT_PATH, ".xls")
    df_regiao = pd.DataFrame()
    
    df_diario_regiao = CollectBalancoDiario().collect_data(files_list, SHEETS[1])
    df_regiao = pd.concat(df_diario_regiao)
    df_regiao.to_csv(f'./output/jan_set_{SHEETS[1]}.csv', index=False)

if __name__ == '__main__':
    main()
