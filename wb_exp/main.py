# coding=utf-8

import global_vars
import wb
import export
from datetime import datetime

if __name__ == '__main__':
    global_vars.mail_text = 'Загрузка заказов WB ({})'.format(datetime.now())+'\n'
    # Инициализация глобального модуля
    global_vars.init()
    # Получить текущий список заказов
    supplie_lise = wb.get_curr_supplie()
    if supplie_lise == None:
        global_vars.main_logger.info('supplie_list is empry')
    else:
        if len(supplie_lise) == 0:
            global_vars.main_logger.info('supplie_list is empry')
        else:
            # Выгрузка поставки в файл экспорта 1С
            export.export_supplie(supplie_lise)

