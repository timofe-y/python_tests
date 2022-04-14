# coding=utf-8

import requests
import json
from datetime import datetime
from datetime import timedelta
import urllib.parse

import global_vars


def get_product(Abarcode):
    global_vars.main_logger.info('Start')
    global_vars.main_logger.info('Abarcode:{}'.format(Abarcode))

    URL = '/api/v2/stocks'
    header = {'Accept': 'application/json',
              'Authorization': global_vars.WB_token}

    param = {'search':Abarcode,
             'skip': 0,
             'take': 1
            }
    try:
        response = requests.get(global_vars.WB_server + URL, headers=header, params=param)
    except:
        global_vars.main_logger.error('Ошибка выполнения метода [requests.get()]')
        return None

    if response.status_code == 200:
        response_json = json.loads(response.text)
        # print(response_json)

        total = response_json.get('total')
        if total <= 0:
            return None
        else:
            stocks_json = response_json.get('stocks')
        product = {}
        product['name'] =       stocks_json[0].get('name')
        product['barcode'] =    stocks_json[0].get('barcode')
        product['article'] = stocks_json[0].get('article')
        return product
    else:
        global_vars.main_logger.error('Status_code: ' + str(response.status_code))
        try:
            response_json = json.loads(response.text)
            global_vars.main_logger.error(response_json.get('errorText'))
        except:
            global_vars.main_logger.error(response.text.encode('utf-8'))
        return None



# список товаров поставщика с их остатками
def get_product_list():
    # return [] / None
    #   name	(string) Наименование
    #   barcode	(string) Баркод
    #   article	(string) Артикул поставщика

    global_vars.main_logger.info('Start')

    URL = '/api/v2/stocks'
    header = {'Accept': 'application/json',
              'Authorization': global_vars.WB_token}
    product_list = []
    # return product_list
    total = 999999
    skip = 0
    take = 1000
    while skip < total:
        param = {'skip': str(skip),
                 'take': str(take)
                 }
        try:
            response = requests.get(global_vars.WB_server + URL, headers=header, params=param)
        except:
            global_vars.main_logger.error('Ошибка выполнения метода [requests.get()]')
            return None

        if response.status_code == 200:
            response_json = json.loads(response.text)
            total = response_json.get('total')
            if skip == 0:
                global_vars.main_logger.info('Products count: ' + str(total))
            stocks_json = response_json.get('stocks')
            for item_json in stocks_json:
                product = {}
                product['name'] =       item_json.get('name')
                product['barcode'] =    item_json.get('barcode')
                product['article'] =    item_json.get('article')
                product_list.append(product)
        else:
            global_vars.main_logger.error('Status_code: ' + str(response.status_code))
            try:
                response_json = json.loads(response.text)
                global_vars.main_logger.error(response_json.get('errorText'))
            except:
                global_vars.main_logger.error(response.text.encode('utf-8'))
            return None
        skip = skip + take
    return product_list


# список сборочных заданий
def get_order_list():
    # return [] / None
    #       orderId (string) Идентификатор заказа
    #       barcode	(string) Штрихкод товара
    global_vars.main_logger.info('Start')

    date_end =   datetime.now() + timedelta(days=1)
    date_start = datetime.now() - timedelta(days=30)

    str_date_start =    datetime.strftime(date_start, "%Y-%m-%dT23:59:59+04:00")
    str_date_end =      datetime.strftime(date_end, "%Y-%m-%dT00:00:00+04:00")

    global_vars.main_logger.info('date_start: ' + str_date_start)
    global_vars.main_logger.info('date_end: ' + str_date_end)

    take =          1000
    skip =          0
    total =         999999
    order_list = []

    URL = '/api/v2/orders'
    header = {'Accept': 'application/json',
              'Authorization': global_vars.WB_token}

    # status = 0-новые заказы, 1-заказы переданые на сборку

    while (skip < total):
        param = {'date_start': str_date_start,
                    'date_end':str_date_end,
                    'status': 1,
                    'take': str(take),
                    'skip': str(skip)}

        param = urllib.parse.urlencode(param)
        try:
            response = requests.get(global_vars.WB_server + URL, headers=header, params=param)
        except:
            global_vars.main_logger.error('Ошибка выполнения метода [requests.get()]')
            return None

        if response.status_code == 200:
            response_json = json.loads(response.text)
            total = response_json.get('total')
            if skip == 0:
                global_vars.main_logger.info('Orders count: ' + str(total))
            orders_json = response_json.get('orders')
            for item_json in orders_json:
                orderId = int(item_json.get('orderId'))
                # Если barcode == "" тогда идентифицировать товар не получится, пропускаем его
                barcode = item_json.get('barcode')
                barcode = barcode.strip()
                if len(barcode) == 0:
                    global_vars.main_logger.error('В заказе ({}) не указан barcode товара'.format(orderId))
                    continue
                # userStatus	integer
                # 1 - Отмена клиента 2 - Доставлен 3 - Возврат 4 - Ожидает 5 - Брак
                userStatus = int(item_json.get('userStatus'))
                if userStatus != 4:
                    continue
                order = {}
                order['orderId'] =  orderId
                order['barcode'] =  barcode
                order_list.append(order)
        else:
            global_vars.main_logger.error('Status_code: ' + str(response.status_code))
            try:
                response_json = json.loads(response.text)
                global_vars.main_logger.error(response_json.get('errorText'))
            except:
                global_vars.main_logger.error('Неизвестная ошибка')
            return None
        skip = skip + take
    return order_list



# список этикеток по переданному массиву сборочных заданий
def get_sticker_list(A_orders_list):
    # A_orders - Спитсок id заказов
    # return [] / None
    # orderId - Id заказа
    # wbStickerSvgBase64 - Полное представление этикетки в векторном формате
    global_vars.main_logger.info('Start')

    MAX_ORDERS_COUNT = 1000
    stickers_list = []

    URL = '/api/v2/orders/stickers'

    header = {'Accept': 'application/json',
              'Content-Type': 'application/json',
              'Authorization': global_vars.WB_token}

    orderIds = []
    orders_count = len(A_orders_list)
    for index in range(0, orders_count):
        order = A_orders_list[index]
        orderId = int(order['orderId'])
        orderIds.append(orderId)
        if (len(orderIds) >= MAX_ORDERS_COUNT) or (orders_count-1 == index):
            # **********************************************************************************
            global_vars.main_logger.info('len(orderIds): ' + str(len(orderIds)))
            body = {'orderIds': orderIds, "type": "code128"}
            try:
                response = requests.post(global_vars.WB_server + URL, headers=header, json=body)
            except:
                global_vars.main_logger.error('Ошибка выполнения метода [requests.get()]')
                continue
            if response.status_code == 200:
                response_json = json.loads(response.text)
                data_json = response_json.get('data')
                if data_json != None:
                    for item in data_json:
                        orderId = item.get('orderId')
                        sticker = item.get('sticker')
                        if sticker != None:
                            wbStickerIdParts = sticker.get('wbStickerIdParts')
                            if wbStickerIdParts != None:
                                obj_sticker = {}
                                obj_sticker['orderId'] = int(orderId)
                                obj_sticker['wbStickerSvgBase64'] = sticker.get('wbStickerSvgBase64')
                                stickers_list.append(obj_sticker)
            else:
                global_vars.main_logger.error('Status_code: ' + str(response.status_code))
                try:
                    response_json = json.loads(response.text)
                    global_vars.main_logger.error(response_json.get('errorText'))
                except:
                    global_vars.main_logger.error('Неизвестная ошибка: ' + response.text.encode('utf-8'))
            # **********************************************************************************
            orderIds = []

    return stickers_list

# Сопоставление списков
def match_lists(A_product_list, A_order_list, A_sticker_list):
    # order_list == sticker_list по orderId
    # order_list == product_list по barcode

    global_vars.main_logger.info('Start')
    wb_orders_list = []
    for order in A_order_list:
        item = {}
        order_orderId = order['orderId']
        order_barcode = order['barcode']
        item['orderId'] = order_orderId
        item['barcode'] = order_barcode
        for sticker in A_sticker_list:
            sticker_orderId = sticker.get('orderId')
            if order_orderId == sticker_orderId:
                item['wbStickerSvgBase64'] = sticker['wbStickerSvgBase64']
                break
        fl = False
        for product in A_product_list:
            product_barcode = product.get('barcode')
            if order_barcode == product_barcode:
                item['name'] = product['name']
                item['article'] = product['article']
                fl = True
                break
        # Если товар не найден в списке product_list, запрашиваем его на сайте WB
        if fl == False:
            product = get_product(order_barcode)
            if product != None:
                item['name'] = product['name']
                item['article'] = product['article']

        wb_orders_list.append(item)
    return wb_orders_list



# Получение текущего списка заказов
# return {}
#     item['orderId']
#     item['barcode']
#     item['totalPrice']
#     item['wbStickerId']
#     item['A']
#     item['B']
#     item['ZPL']
#         # item['wbStickerEncoded']
#         # item['wbStickerSvgBase64']
#         # item['wbStickerZplV']
#         # item['wbStickerZpl']
#     item['name']
#     item['article']
def get_curr_supplie():
    # Список товаров
    product_list = get_product_list()
    if product_list == None:
        global_vars.main_logger.info('product_list count: is empry')
        return None
    if len(product_list) == 0:
        global_vars.main_logger.error('product_list is empry')
        return None
    global_vars.main_logger.info('product_list count: ' + str(len(product_list)))
    # Список заказов
    order_list = get_order_list()
    if order_list == None:
        global_vars.main_logger.error('order_list is empry')
        return None
    if len(order_list) == 0:
        global_vars.main_logger.error('order_list is empry')
        return None
    global_vars.main_logger.info('order_list count: ' + str(len(order_list)))
    # Список этикеток
    sticker_list = get_sticker_list(order_list)
    global_vars.main_logger.info('sticker_list count: ' + str(len(sticker_list)))
    if sticker_list == None:
        global_vars.main_logger.error('sticker_list is empry')
        return None
    if len(sticker_list) == 0:
        global_vars.main_logger.error('sticker_list is empry')
        return None

    # Сопоставление списков
    supplie_list = match_lists(product_list, order_list, sticker_list)

    if len(supplie_list) != len(order_list):
        delta = len(order_list) - len(supplie_list)
        global_vars.main_logger.info('supplie_list count: ' + str(len(supplie_list)))
        global_vars.main_logger.info('order_list count: ' + str(len(order_list)))
        global_vars.main_logger.info('delta: ' + str(delta))
        global_vars.main_logger.info('failed to load')
        # return None
    if len(supplie_list) == 0:
        global_vars.main_logger.info('supplie_list is empry')
        return None
    global_vars.mail_text = global_vars.mail_text + 'Загружено {} заказов'.format(len(supplie_list)) + '\n'

    return supplie_list
