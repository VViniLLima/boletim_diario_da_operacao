

class GetRowAndColumn:
   def sin_start_end_columns(self, regiao, df):
      for column in range(1,3):
         for df_row, cell_text in enumerate(df[df.columns[column]]):
            if type(cell_text) == str and regiao in cell_text:
               start_row = df_row+2
               start_column = column
               end_column = start_column+4

               for regiao_row, cell_text in enumerate(df[df.columns[start_column]][start_row:]):
                     if type(cell_text) == str and 'Carga ' in cell_text:
                        end_row = regiao_row+(df_row+3)
                        break
      
      return start_row, end_row, start_column, end_column

   def regioes_start_end_columns(self, regiao, df):
      for column in range(1,10):
         for df_row, cell_text in enumerate(df[df.columns[column]]):
            if type(cell_text) == str and regiao in cell_text:
               start_row = df_row+1
               start_column = column
               end_column = start_column+4

               for regiao_row, cell_text in enumerate(df[df.columns[start_column]][start_row:]):
                     if type(cell_text) == str and 'Carga ' in cell_text:
                           end_row = regiao_row+(df_row+3)
                           break
      return start_row, end_row, start_column, end_column

   def clear_text_from_programado_acumulado(self, df):
      for df_index in df.index:     
         if type(df['programado'][df_index]) == str:
            df.at[df_index, 'programado'] = df['programado'][df_index].strip(' MWmed')
      return df
      