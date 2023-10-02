import pandas as pd
import logging
from datetime import datetime
from constants import CONVERTED_FILES_PATH

class Commons:
    def find_sheet(self, file, sheet):
        df = pd.ExcelFile(f'{CONVERTED_FILES_PATH}{file}')
        checked_sheet = self.check_sheet(df, sheet)
        if checked_sheet != None:
            return self.open_file(file, checked_sheet)
        else:
           raise ValueError

    def open_file(self, file, sheet):
        return pd.read_excel(f'{CONVERTED_FILES_PATH}{file}', sheet_name=sheet)
    
    def check_sheet(self, df, sheet):
        for s in df.sheet_names:
            if sheet in s:
                return s
        
    def logger(self, dir_name):
        current_date = '{:%d-%m-%Y}'.format(datetime.now())
        
        logger = logging.getLogger(name='Logger')
        logging.basicConfig(filename=f'./logs/{dir_name}/{current_date}.log', encoding='utf-8', filemode='a', level=logging.DEBUG, format='%(asctime)s: %(name)s - %(levelname)s - %(message)s')
        logger.setLevel(level=logging.DEBUG)
        return logger