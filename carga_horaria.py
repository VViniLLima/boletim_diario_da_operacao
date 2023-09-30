import pandas as pd
from constants import SHEET_CARGA_HORARIA
from common import Commons


class CargaHorariaDf:
    def collect_data(self, files_list):
        lista_carga_horaria = []
        for file in files_list:
            print(file, SHEET_CARGA_HORARIA)
            try:
               carga_df = Commons().find_sheet(file, SHEET_CARGA_HORARIA)
            except ValueError:
                print(f'{file} - Não possui a Aba: ', SHEET_CARGA_HORARIA)
                continue
            
            start_row = self.find_row(carga_df)
            previsto_verificado_list = self.get_previsto_verificado_name(carga_df, start_row)
            subsistema_list = self.get_subsistema_name(carga_df, start_row)
            col_names = self.column_names(previsto_verificado_list, subsistema_list)
            lista_carga_horaria.append(self.create_df(carga_df,start_row,col_names,file))
        return lista_carga_horaria

    def get_previsto_verificado_name(self, df, start_row):
        previsto_verificado_list = []
        for i in df.iloc[start_row, 1:]:
            previsto_verificado_list.append(i.replace('\r\n', ' '))
        return previsto_verificado_list

    def get_subsistema_name(self, df, start_row):
        subsistema_list = []
        for i in df.iloc[start_row-1, 1:].ffill():
            subsistema_list.append(i)
        return subsistema_list

    def column_names(self, previsto_verificado_list, subsistema_list):
        col_names = ['Hora']
        for item in range(len(subsistema_list)):
            col_names.append(subsistema_list[item] + ' - ' + previsto_verificado_list[item])
        return col_names
        

    def find_row(self, df):
        for df_row, cell_text in enumerate(df[df.columns[0]]):
            if type(cell_text) == str and (cell_text == 'Subsistema' or cell_text == 'Submercado'):
                start_row = df_row+1
                break
        return start_row

    def open_file(self, file, sheet):
        return pd.read_excel(f'./input/{file}', sheet_name=sheet)
    
    def get_file_date(self, file):
        day, month, year = file[7:17].split('-')
        data_diario = year+'-'+month+'-'+day
        return data_diario
    
    def create_df(self, df, start_row, columns, file):
        reserva_df = pd.DataFrame.copy(df.iloc[start_row+1:])
        reserva_df.columns = columns
        reserva_df['data_diario'] = self.get_file_date(file)
        return reserva_df