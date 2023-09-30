from urllib import request
from datetime import timedelta, date
import time

def main():
    initial_date = date(2019,2,1)
    final_date = date(2021,12,31)

    while initial_date != final_date:
        print('Data: ', initial_date)

        ons_page = ('http://sdro.ons.org.br/SDRO/DIARIO/%02d_%02d_%02d/Html/DIARIO_%02d-%02d-%02d.xlsx') % (initial_date.year, initial_date.month, initial_date.day, initial_date.day, initial_date.month, initial_date.year)
        save_name = ("./output/download_ons/DIARIO_%02d-%02d-%02d.xlsx") % (initial_date.day, initial_date.month, initial_date.year)
        
        request.urlretrieve(ons_page, save_name)
        initial_date += timedelta(days=1)
        time.sleep(2)
if __name__ == '__main__':
    main()