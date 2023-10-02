import pandas as pd
from constants import IMPUT_PATH, REGIOES
from common import Commons


class BalancoDiarioDf:
    def collect_data(self, file_list, sheet):
        dataframe_list = []
        for file in file_list:
            print(file)
            try:
                initial_df = Commons().find_sheet(file, sheet)
            except ValueError:
                print(f'O arquivo: {file} não contém a aba: {sheet}. especificada.')
                continue

            for regiao in REGIOES:
                
                if regiao == 'Sistema Interligado':
                    start_row, end_row, start_column, end_column = self.sin_start_end_columns(regiao, initial_df)
                    if start_row != 0 and end_row != 0:
                        df_regiao = self.balanco_energia_sin(regiao,start_row, end_row, start_column, end_column, initial_df)
                        df_regiao['data_diario'] = self.get_file_date(file)
                        df_regiao = self.clear_text_from_programado_acumulado(df_regiao)
                        dataframe_list.append(df_regiao)
                else:
                    start_row, end_row, start_column, end_column = self.regioes_start_end_columns(regiao, initial_df)
                    df_regiao = self.balanco_energia_regioes(regiao,start_row, end_row, start_column, end_column, initial_df)
                    df_regiao['data_diario'] = self.get_file_date(file)
                    df_regiao = self.clear_text_from_programado_acumulado(df_regiao)
                    dataframe_list.append(df_regiao)
            

        return dataframe_list 
        
  
    def get_file_date(self, file):
        day, month, year = file[7:17].split('-')
        data_diario = year+'-'+month+'-'+day
        return data_diario
    
    def open_xls_file(self, file, sheet):
        df = pd.read_excel(IMPUT_PATH+file, sheet_name=sheet)
        return df
        
    def sin_start_end_columns(self, regiao, df):
        start_row = None
        for column in range(1,3):
            for df_row, cell_text in enumerate(df[df.columns[column]]):
                if type(cell_text) == str and regiao in cell_text:
                    start_row = df_row+2
                    start_column = column
                    end_column = start_column+4

            if start_row == None:
                return 0,0,0,0
            
            for regiao_row, cell_text in enumerate(df[df.columns[start_column]][start_row:]):
                    if type(cell_text) == str and 'Carga ' in cell_text:
                        end_row = (start_row+regiao_row+1)
                        return start_row, end_row, start_column, end_column
        
    def regioes_start_end_columns(self, regiao, df):
        if regiao == 'Norte':
            for column in range(1,3):
                for df_row, cell_text in enumerate(df[df.columns[column]]):
                    if type(cell_text) == str and regiao in cell_text:
                        start_row = df_row+1
                        start_column = column
                        end_column = start_column+4

            for regiao_row, cell_text in enumerate(df[df.columns[start_column]][start_row:]):
                    if type(cell_text) == str and 'Carga ' in cell_text:
                        end_row = (start_row+regiao_row+1)
                        return start_row, end_row, start_column, end_column
        else:
            for column in range(8,9):
                for df_row, cell_text in enumerate(df[df.columns[column]]):
                    if type(cell_text) == str and regiao in cell_text:
                        start_row = df_row+1
                        start_column = column
                        end_column = start_column+4

            for regiao_row, cell_text in enumerate(df[df.columns[start_column]][start_row:]):
                    if type(cell_text) == str and 'Carga ' in cell_text:
                        end_row = (start_row+regiao_row+1)
                        return start_row, end_row, start_column, end_column

    def clear_text_from_programado_acumulado(self, df):
        for df_index in df.index:     
            if type(df['programado'][df_index]) == str:
                df.at[df_index, 'programado'] = df['programado'][df_index].strip(' MWmed')
        return df
    

    def balanco_energia_sin(self, regiao, start_row, end_row, start_col, end_col, initial_df):
        reg_df = initial_df.iloc[start_row:end_row, start_col:end_col]
        reg_df.columns = ['producao', 'programado', 'verificado', 'desvio']
        reg_df['producao'] = reg_df['producao'].str.strip()
        reg_df['regiao'] = regiao

        return reg_df
    
    def balanco_energia_regioes(self, regiao, start_row, end_row, start_col, end_col, initial_df):
        reg_df = initial_df.iloc[start_row:end_row, start_col:end_col]
        reg_df.columns = ['producao', 'desvio', 'verificado', 'programado']
        reg_df['regiao'] = regiao
        
        return reg_df