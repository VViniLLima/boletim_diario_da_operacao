import pandas as pd
PATH = '../../../../PycharmProjects/ipdo/Backup_BDO_Geral/converted_files/'

class Commons:
    def find_sheet(self, file, sheet):
        df = pd.ExcelFile(f'{PATH}{file}')
        checked_sheet = self.check_sheet(df, sheet)
        if checked_sheet != None:
            return self.open_file(file, checked_sheet)
        else:
           raise ValueError

    def open_file(self, file, sheet):
        return pd.read_excel(f'{PATH}{file}', sheet_name=sheet)
    
    def check_sheet(self, df, sheet):
     for s in df.sheet_names:
        if sheet in s:
            return s