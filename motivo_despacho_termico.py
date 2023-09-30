import pandas as pd
import numpy as np
from constants import SHEET_MOTIVO_DESPACHO
from common import Commons


class MotivoDespachoDf:
    def collect_data(self, file_list):
        despacho_df_list = []

        for file in file_list:
            print(file)
            try:
                df = Commons().find_sheet(file, SHEET_MOTIVO_DESPACHO)
            except ValueError:
                print(f'{file} - Não possui a Aba: ', SHEET_MOTIVO_DESPACHO)
                continue
            
            start_row = self.find_usina_despacho(df)
            cols = self.get_column_name(df, start_row)

            df = self.create_despacho_df(df, start_row, cols)
            df['data_diario'] = self.get_file_date(file)
            despacho_df_list.append(df)

        return despacho_df_list

    def open_file(self, file, sheet):
        return pd.read_excel(f'./input/{file}', sheet_name=sheet)
    
    def find_usina_despacho(self, df):
        for df_row, cell_text in enumerate(df[df.columns[0]]):
            if type(cell_text) == str and cell_text == 'Usina':
                start_row = df_row+1
                break
        return start_row
    
    def get_column_name(self, df, start_row):
        cols = []
        for i in df.iloc[start_row-1].values:
            cols.append(i.replace('\r\n', ' '))
        return cols
    
    def create_despacho_df(self, df, start_row, cols):
        colunas_esperadas = ['Usina','Código ONS', 'Garantia Energética', 'Restrição Elétrica','Inflex.','Energia de Reposição', 'Reserva de Potência', 'Export.','Geração Fora de Mérito']
        motdesp = df.iloc[start_row:, :]
        motdesp.columns = cols
        col_faltante = list(set(colunas_esperadas).difference(cols))
        print(col_faltante)
        
        if len(col_faltante) > 0:
            for c in col_faltante:
                motdesp[c] = np.nan
                return motdesp[colunas_esperadas]
        else:
            return motdesp[colunas_esperadas]
    
    def get_file_date(self, file):
        day, month, year = file[7:17].split('-')
        data_diario = year+'-'+month+'-'+day
        return data_diario