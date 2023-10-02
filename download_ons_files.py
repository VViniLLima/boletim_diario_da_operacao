from urllib import request
from urllib.request import urlopen
import urllib
from datetime import timedelta, date
from convert_xlsx_files import XLSXFiles
from constants import BDO_DOWNLOAD_PATH
from common import Commons
import time


downloaded_files_list = XLSXFiles().get_files_list(BDO_DOWNLOAD_PATH, 'xlsx')
def main():
    logger_download_ons = create_logger()
    initial_date = date(2023,9,14)
    final_date = date(2023,9,30)

    while initial_date <= final_date:
        try:
            check_if_file_exists(initial_date, logger_download_ons)
        except FileExistsError:
            initial_date += timedelta(days=1)
            continue

        ons_page = ('http://sdro.ons.org.br/SDRO/DIARIO/%02d_%02d_%02d/Html/DIARIO_%02d-%02d-%02d.xlsx') % (initial_date.year, initial_date.month, initial_date.day, initial_date.day, initial_date.month, initial_date.year)
        try:
            check_if_page_exists(ons_page, logger_download_ons)
        except:
            continue
        
        save_name = (f"{BDO_DOWNLOAD_PATH}DIARIO_%02d-%02d-%02d.xlsx") % (initial_date.day, initial_date.month, initial_date.year)
        download_file(ons_page, save_name, logger_download_ons)
        initial_date += timedelta(days=1)
        time.sleep(2)

def create_logger():
    return Commons().logger(dir_name='download_ons_files')


def check_if_file_exists(initial_date, logger_download_ons):
    filename = ('DIARIO_%02d-%02d-%02d.xlsx') % (initial_date.day, initial_date.month, initial_date.year)
    
    if filename in downloaded_files_list:
        logger_download_ons.debug(f'Arquivo {filename} já existe, download não realizado')
        raise FileExistsError

def check_if_page_exists(ons_page, logger_download_ons):
    try:
        page = urllib.request.urlopen(ons_page)
    except: 
        logger_download_ons.warning(f'Arquivo ainda não disponível: {page}')

def download_file(ons_page, save_name, logger_download_ons):
    logger_download_ons.debug(f'Baixando arquivo: {save_name}')
    request.urlretrieve(ons_page, save_name)
    

if __name__ == '__main__':
    main()