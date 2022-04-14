# coding=utf-8


import os
import xlwt
import base64

import global_vars
import svg_to_image

# Экспорт закза
def export_supplie(A_supplie_lise):
    global_vars.main_logger.info('Start')
    # Проверка, есть ли каталог выгрузки
    if os.path.exists(global_vars.Export_catalog)==False:
        os.makedirs(global_vars.Export_catalog)
    order_file_name = global_vars.Export_catalog + 'order.xls'
    wb = xlwt.Workbook()
    ws = wb.add_sheet('WB Order')
    index = 0
    for item in A_supplie_lise:
        ws.write(index, 0, item['orderId'])
        ws.write(index, 1, item['name'])
        ws.write(index, 2, item['article'])
        sticker_image_file_name = global_vars.Export_catalog + item['article'] + '_' + str(item['orderId']) + '.jpeg'
        svg_to_image.create_image(base64.b64decode(item['wbStickerSvgBase64']), sticker_image_file_name)
        index = index + 1
    wb.save(order_file_name)
    global_vars.main_logger.info('{} orders exported'.format(index))
