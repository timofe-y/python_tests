# coding=utf-8

import smtplib                                      # Импортируем библиотеку по работе с SMTP

# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.text import MIMEText                # Текст/HTML


addr_from = 'automail@biosort.ru'                 # Адрес отправителя
smtp_password  = '1qaz2WsX'                                  # Пароль
smtp_server = 'smtp.yandex.ru'
smtp_port = 465


def send(addr_to, subject, body):
    # addr_to - Получатель
    # subject - Тема
    # body    - Тело
    msg = MIMEMultipart()  # Создаем сообщение
    msg['From'] = addr_from  # Адресат
    msg['To'] = addr_to  # Получатель
    msg['Subject'] = subject  # Тема сообщения
    msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст

    server = smtplib.SMTP_SSL(smtp_server, smtp_port)  # Создаем объект SMTP
    # server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)  # Создаем объект SMTP для smtp.yandex.ru
    server.set_debuglevel(True)  # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
    #server.starttls()  # Начинаем шифрованный обмен по TLS
    server.login(addr_from, smtp_password)  # Получаем доступ
    server.send_message(msg)  # Отправляем сообщение
    server.quit()  # Выходим
