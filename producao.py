import pandas as pd
from constants import SHEETS_PRODUCAO
from common import Commons


class ProducaoDf:
    def collect_data(self, file_list):
        producao_df_list = []

        for file in file_list:
            print(file)
            for sheet in SHEETS_PRODUCAO:
                try:
                    df = Commons().find_sheet(file, sheet)
                except ValueError:
                    print(f'{file} - Não possui a Aba: ', sheet)
                    continue
                
                start_row = self.find_usina_producao(df)
                df = self.create_producao_df(df, start_row)
                df['producao'] = sheet.split(' ')[-1]
                df['data_diario'] = self.get_file_date(file)
                producao_df_list.append(df)

        return producao_df_list


    def find_usina_producao(self, df):
        for df_row, cell_text in enumerate(df[df.columns[0]]):
            if type(cell_text) == str and cell_text == 'Usina':
                start_row = df_row+1
                break
        return start_row

    def create_producao_df(self, df, start_row):
        df = df.iloc[start_row:, 0:5]
        df.columns = ['Usina', 'Código ONS', 'Programado (MWmed)', 'Verificado (MWmed)', 'Desvio %']
        return df
    
    def open_file(self, file, sheet):
        return pd.read_excel(f'./input/{file}', sheet_name=sheet)

    def get_file_date(self, file):
        day, month, year = file[7:17].split('-')
        data_diario = year+'-'+month+'-'+day
        return data_diario