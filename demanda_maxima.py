import pandas as pd
from constants import SHEET_DEMANDA_MAXIMA
from common import Commons

class DemandaMaximaDf:
    def collect_data(self, files_list):
        lista_demanda_maxima = []
        for file in files_list:
            print(file, SHEET_DEMANDA_MAXIMA)
            try:
               demanda_maxima_df =  Commons().find_sheet(file, SHEET_DEMANDA_MAXIMA)
            except ValueError:
                print(f'{file} - Não possui a Aba: ', SHEET_DEMANDA_MAXIMA)
                continue

            start_row = self.find_row(demanda_maxima_df)
            col_names = self.column_names(demanda_maxima_df, start_row)
            lista_demanda_maxima.append(self.create_df(demanda_maxima_df,start_row,col_names,file))
        return lista_demanda_maxima

    def find_row(self, df):
        for df_row, cell_text in enumerate(df[df.columns[0]]):
            if type(cell_text) == str and (cell_text == 'Subsistema' or cell_text == 'Submercado'):
                start_row = df_row+1
                break
        return start_row

    def column_names(self, df, start_row):
        cols = []
        for item in df.iloc[start_row-1]:
            cols.append(item)
            if 'Submercado' in cols:
                cols[0] = 'Subsistema'
        return cols
    
    def create_df(self, df, start_row, columns, file):
        demanda_max_df = pd.DataFrame.copy(df.iloc[start_row:].dropna())
        demanda_max_df.columns = columns
        demanda_max_df.pop('Referência')
        demanda_max_df.pop('Data')
        demanda_max_df['data_diario'] = self.get_file_date(file)
        return demanda_max_df
    
    def open_file(self, file, sheet):
        return pd.read_excel(f'./input/{file}', sheet_name=sheet)
    
    def get_file_date(self, file):
        day, month, year = file[7:17].split('-')
        data_diario = year+'-'+month+'-'+day
        return data_diario