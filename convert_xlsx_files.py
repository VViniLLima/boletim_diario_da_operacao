import os
from spire.xls import *
from spire.common import *


class XLSXFiles:
    def convert_xlsx_to_xls(self, files_list, input_path, output_path):
        for file in files_list:
            workbook = Workbook()
            workbook.LoadFromFile(f'{input_path}{file}')
            
            file_name = file.replace('xlsx', 'xls')
            workbook.SaveToFile(f'{output_path}{file_name}', ExcelVersion.Version97to2003)
            workbook.Dispose()

    def get_files_list(self, input_path, extension):
        files_list = []
        for file in os.listdir(input_path):
            if file.endswith(extension):
                files_list.append(file)
        return files_list