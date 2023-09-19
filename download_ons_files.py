import urllib
from datetime import timedelta, date


def main():
    initial_date = date(2023,1,1)
    final_date = date(2023,9,18)

    while initial_date != final_date:
        print('Data: ', initial_date)

        ons_page = ('http://sdro.ons.org.br/SDRO/DIARIO/%02d_%02d_%02d/Html/DIARIO_%02d-%02d-%02d.xlsx') % (initial_date.year, initial_date.month, initial_date.day, initial_date.day, initial_date.month, initial_date.year)
        save_name = ("./output/download_ons/DIARIO_%02d-%02d-%02d.xlsx") % (initial_date.day, initial_date.month, initial_date.year)
        
        urllib.request.urlretrieve(ons_page, save_name)
        initial_date += timedelta(days=1)
 
if __name__ == '__main__':
    main()