

class Dataframe_per_regiao:

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

    

