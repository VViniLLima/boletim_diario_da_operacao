import pandas as pd
from constants import SHEET_RESERVATORIOS_HIDRAULICOS
from common import Commons

class ReservatoriosHidraulicos:
    def collect_data(self, files_list):
        lista_reservatorios = []
        for file in files_list:
            
            for sheet in SHEET_RESERVATORIOS_HIDRAULICOS:
                print(file, sheet)
                try:
                    reservatorios_df = Commons().find_sheet(file, sheet)
                except ValueError:
                    print(f'{file} - Não possui a Aba: ', sheet)
                    continue

                start_row = self.find_row(reservatorios_df)
                cols = self.column_names(reservatorios_df, start_row)
                lista_reservatorios.append(self.create_df(reservatorios_df,start_row, cols, file, sheet))
        
        return lista_reservatorios
    

    def find_row(self, df):
        for df_row, cell_text in enumerate(df[df.columns[0]]):
            if type(cell_text) == str and cell_text == 'Bacia':
                start_row = df_row+1
                break
        return start_row
    
    def column_names(self, df, start_row):
        cols = []
        for item in df.iloc[start_row-1].dropna().iloc[:-1]:
            cols.append(item)
        for item in df.iloc[start_row].dropna():
            cols.append(item)
        return cols
    
    def open_file(self, file, sheet):
        return pd.read_excel(f'./input/{file}', sheet_name=sheet)
    
    def get_file_date(self, file):
        day, month, year = file[7:17].split('-')
        data_diario = year+'-'+month+'-'+day
        return data_diario
    
    def create_df(self, df, start_row, columns, file, sheet):
        res_df = df.iloc[start_row+1:]
        res_df = res_df.drop(res_df.columns[2], axis=1)
        res_df.columns = columns
        res_df[res_df.columns[0]] = res_df[res_df.columns[0]].ffill()
        res_df['data_diario'] = self.get_file_date(file)
        res_df['regiao'] = self.identify_subsistema(sheet)
        return res_df
    
    def identify_subsistema(self, sheet):
        if sheet[-2:] == ' S':
            subsistema = 'Sul'
        if sheet[-2:] == 'SE':
            subsistema = 'Sudeste'
        if sheet[-2:] == ' N':
            subsistema = 'Norte'
        if sheet[-2:] == 'NE':
            subsistema = 'Nordeste'
        return subsistema