import os
from spire.xls import *
from spire.common import *
from constants import BDO_DOWNLOAD_PATH, CONVERTED_FILES_PATH
from common import Commons


class XLSXFiles:
    def convert_xlsx_to_xls(self, input_path=BDO_DOWNLOAD_PATH, output_path=CONVERTED_FILES_PATH):
        convert_logger = Commons().logger('conversao')
        downloaded_files_list = self.get_files_list(input_path, 'xlsx')
        
        for file in downloaded_files_list:
            try:
                self.check_if_file_already_exists(file, convert_logger)
            except FileExistsError:
                continue

            loaded_file = self.load_xlsx_file(file, input_path)
            self.save_xls_file(file, loaded_file, output_path, convert_logger)


    def get_files_list(self, input_path, extension):
        files_list = []
        for file in os.listdir(input_path):
            if file.endswith(extension):
                files_list.append(file)
        return files_list
    

    def check_if_file_already_exists(self, file, convert_logger):
        converted_files_list = self.get_files_list(CONVERTED_FILES_PATH, 'xls')

        if file.replace('xlsx', 'xls') in converted_files_list:
            convert_logger.info(f'Arquivo {file} já existe, conversão não realizada.')
            raise FileExistsError

    def load_xlsx_file(self, file, input_path):
        workbook = Workbook()
        workbook.LoadFromFile(f'{input_path}{file}')
        return workbook
    

    def save_xls_file(self, file, workbook, output_path, convert_logger):
        file_name = file.replace('xlsx', 'xls')
        workbook.SaveToFile(f'{output_path}{file_name}', ExcelVersion.Version97to2003)
        workbook.Dispose()
        convert_logger.info(f'Arquivo {file} convertido.')
XLSXFiles().convert_xlsx_to_xls()