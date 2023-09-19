import pandas as pd
from dataframe_per_region import Dataframe_per_regiao
from find_region import GetRowAndColumn
from constants import IMPUT_PATH, SHEETS, REGIOES


class CollectBalancoDiario:
    def collect_data(self, file_list, sheet):
        dataframe_list = []
        for file in file_list:
            try:
                initial_df = self.open_xls_file(file, sheet)
            except ValueError:
                print(f'O arquivo: {file} não contém a aba: {sheet}. especificada.')

            for regiao in REGIOES:
                if regiao == 'Sistema Interligado':
                    start_row, end_row, start_column, end_column = GetRowAndColumn().sin_start_end_columns(regiao, initial_df)
                    df_regiao = Dataframe_per_regiao().balanco_energia_sin(regiao,start_row, end_row, start_column, end_column, initial_df)

                else:
                    start_row, end_row, start_column, end_column = GetRowAndColumn().regioes_start_end_columns(regiao, initial_df)
                    df_regiao = Dataframe_per_regiao().balanco_energia_regioes(regiao,start_row, end_row, start_column, end_column, initial_df)

                    if sheet == SHEETS[1]:
                        df_regiao = GetRowAndColumn().clear_text_from_programado_acumulado(df_regiao)

                df_regiao['data_diario'] = self.get_file_date(file)
                dataframe_list.append(df_regiao)     
        return dataframe_list 
        
  
    def get_file_date(self, file):
        return file[7:17].replace('-', '/')
    
    def open_xls_file(self, file, sheet):
        df = pd.read_excel(IMPUT_PATH+file, sheet_name=sheet)
        return df
        
