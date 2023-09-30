import pandas as pd
from constants import SHEET_ENERGIA_ARMAZENADA
from common import Commons


class EnergiaArmazenadaDf:
    def collect_data(self, files_list):
        lista_energia_armazenada_df = []
        for file in files_list:
            print(file, SHEET_ENERGIA_ARMAZENADA)
            try:
                energia_armazenada_df =  Commons().find_sheet(file, SHEET_ENERGIA_ARMAZENADA)
            except ValueError:
                print(f'{file} - Não possui a Aba: ', SHEET_ENERGIA_ARMAZENADA)
                continue

            start_row = self.find_row_energia_armazenada(energia_armazenada_df)
            column_names = self.get_column_name(energia_armazenada_df, start_row)
            lista_energia_armazenada_df.append(self.create_df(energia_armazenada_df, start_row, column_names, file))

        return lista_energia_armazenada_df



    def find_row_energia_armazenada(self, df):
        for df_row, cell_text in enumerate(df[df.columns[0]]):
            if type(cell_text) == str and cell_text == 'Energia Armazenada':
                start_row = df_row+1
                break
        return start_row

    def get_column_name(self, df, start_row):
            cols = []
            for i in df.iloc[start_row-1].values:
                cols.append(i.replace('\r\n', ' '))
            return cols

    def open_file(self, file, sheet):
        return pd.read_excel(f'./input/{file}', sheet_name=sheet)
    
    def get_file_date(self, file):
        day, month, year = file[7:17].split('-')
        data_diario = year+'-'+month+'-'+day
        return data_diario
    
    def create_df(self, df, start_row, columns, file):
        reserva_df = pd.DataFrame.copy(df.iloc[start_row:])
        reserva_df.columns = columns
        reserva_df['data_diario'] = self.get_file_date(file)
        return reserva_df