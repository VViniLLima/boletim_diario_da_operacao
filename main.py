from convert_xlsx_files import XLSXFiles
from collect_balanco_diario import collect_balanco
from collect_producao import collect_producao
from collect_motivo_despacho_termico import collect_despacho
from collect_reserva_girante import collect_reserva_girante
from collect_energia_armazenada import collect_energia_armazenada
from collect_energia_natural_afluente import collect_energia_natural_afluente
from collect_carga_horaria import collect_carga_horaria
from collect_demanda_maxima import collect_demanda_maxima
from collect_reservatorios_hidraulicos import collect_reservatorios


def main():
    files_list = XLSXFiles().get_files_list(input_path='', extension='')
    XLSXFiles().convert_xlsx_to_xls(files_list='', input_path='', output_path='')
    

    collect_balanco(files_list)
    #collect_producao(files_list)
    #collect_despacho(files_list)
    #collect_reserva_girante(files_list)
    #collect_energia_armazenada(files_list)
    #collect_energia_natural_afluente(files_list)   
    #collect_carga_horaria(files_list)              
    #collect_demanda_maxima(files_list)             

    #collect_reservatorios(files_list)
if __name__ == '__main__':
    main()
