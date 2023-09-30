import pandas as pd
from constants import SHEET_RESERVA_GIRANTE
from common import Commons


class ReservaGiranteDf:
    def collect_data(self, files_list):
        lista_reserva_girante_df = []
        for file in files_list:
            print(file)
            try:
                reserva_girante_df = Commons().find_sheet(file, SHEET_RESERVA_GIRANTE)
            except ValueError:
                print(f'{file} - Não possui a Aba: ', SHEET_RESERVA_GIRANTE)
                continue
            start_row = self.find_row_reserva_girante(reserva_girante_df)
            column_names = self.get_column_name(reserva_girante_df, start_row)
            hour = self.get_hour(reserva_girante_df, start_row)

            lista_reserva_girante_df.append(self.create_df(reserva_girante_df, start_row, column_names, hour, file))
        return lista_reserva_girante_df

    def find_row_reserva_girante(self, df):
        for df_row, cell_text in enumerate(df[df.columns[0]]):
            if type(cell_text) == str and cell_text == 'Área de Operação':
                start_row = df_row+1
                break
        return start_row

    def get_column_name(self, df, start_row):
            cols = []
            for i in df.iloc[start_row-1].values:
                cols.append(i.replace('\r\n', ' '))
            return cols

    def get_hour(self, df, start_row):
        return df.iloc[start_row,-1]
    
    def open_file(self, file, sheet):
        return pd.read_excel(f'./input/{file}', sheet_name=sheet)

    def get_file_date(self, file):
        day, month, year = file[7:17].split('-')
        data_diario = year+'-'+month+'-'+day
        return data_diario
    
    def create_df(self, df, start_row, columns, hour, file):
        reserva_df = pd.DataFrame.copy(df.iloc[start_row:start_row+5])
        reserva_df.columns = columns
        reserva_df['Hora'] = hour
        reserva_df['data_diario'] = self.get_file_date(file)
        return reserva_df