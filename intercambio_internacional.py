import pandas as pd
from common import Commons


class IntercambioInternacionalDf:
    def collect_data(self, file_list, sheet):
        dataframe_list = []
        for file in file_list:
            print(file)
            try:
                initial_df = Commons().find_sheet(file, sheet)
            except ValueError:
                print(f'O arquivo: {file} não contém a aba: {sheet}. especificada.')
                continue

            start_row, start_col = self.find_intercambio_row(initial_df)
            initial_df = initial_df.iloc[start_row:, start_col:start_col+5]

            interc_internacional_cols = ['usina', 'importacao_verificada', 'importacao_programada', 'exportacao_verificada', 'exportacao_programada']

            initial_df.dropna(subset=[initial_df.columns[-1]], inplace=True)
            initial_df.columns = interc_internacional_cols
            initial_df['usina'] = initial_df['usina'].str.strip()
            initial_df['data_diario'] = self.get_file_date(file)
            dataframe_list.append(initial_df)

        return dataframe_list 
        
  
    def get_file_date(self, file):
        day, month, year = file[7:17].split('-')
        data_diario = year+'-'+month+'-'+day
        return data_diario
    
    def find_intercambio_row(self, df):
        interc_start_row = 25
        start_col = 1
        for df_row, cell_text in enumerate(df[df.columns[start_col]][interc_start_row:]):
            if type(cell_text) == str and cell_text == 'Intercâmbio Internacional':
                start_row = df_row+interc_start_row
                break
        return start_row, start_col 