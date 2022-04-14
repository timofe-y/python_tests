# coding=utf-8

"""
import sendmail
Отправка письма (smtp сервер, логин, пароль - указаны в модуле)
  sendmail.send('timofey@svprice.net', 'test', 'Проверка')
"""

"""
import svg_to_image
Парсинг+рисоваие+сохранение в файл этикуток WB
  svg_str_base64 = 'PD94bWwgdmVyc2lvbj0iMS4wIj8+CjwhLS0gR2VuZXJhdGVkIGJ5IFNWR28gLS0+Cjxzdmcgd2lkdGg9IjQwMCIgaGVpZ2h0PSIzMDAiCiAgICAgdmlld0JveD0iMjAgMjAgMzUwIDI2MCIKICAgICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgICAgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPgo8cmVjdCB4PSIwIiB5PSIwIiB3aWR0aD0iNDAwIiBoZWlnaHQ9IjMwMCIgc3R5bGU9ImZpbGw6d2hpdGUiIC8+CjxyZWN0IHg9IjQ0IiB5PSIyMCIgd2lkdGg9IjYiIGhlaWdodD0iMTcwIiBzdHlsZT0iZmlsbDpibGFjayIgLz4KPHJlY3QgeD0iNTIiIHk9IjIwIiB3aWR0aD0iMyIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSI2MCIgeT0iMjAiIHdpZHRoPSIyIiBoZWlnaHQ9IjE3MCIgc3R5bGU9ImZpbGw6YmxhY2siIC8+CjxyZWN0IHg9IjcyIiB5PSIyMCIgd2lkdGg9IjUiIGhlaWdodD0iMTcwIiBzdHlsZT0iZmlsbDpibGFjayIgLz4KPHJlY3QgeD0iODMiIHk9IjIwIiB3aWR0aD0iMiIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSI5MyIgeT0iMjAiIHdpZHRoPSIyIiBoZWlnaHQ9IjE3MCIgc3R5bGU9ImZpbGw6YmxhY2siIC8+CjxyZWN0IHg9IjEwMCIgeT0iMjAiIHdpZHRoPSI1IiBoZWlnaHQ9IjE3MCIgc3R5bGU9ImZpbGw6YmxhY2siIC8+CjxyZWN0IHg9IjEwOCIgeT0iMjAiIHdpZHRoPSI4IiBoZWlnaHQ9IjE3MCIgc3R5bGU9ImZpbGw6YmxhY2siIC8+CjxyZWN0IHg9IjExOCIgeT0iMjAiIHdpZHRoPSI4IiBoZWlnaHQ9IjE3MCIgc3R5bGU9ImZpbGw6YmxhY2siIC8+CjxyZWN0IHg9IjEyOCIgeT0iMjAiIHdpZHRoPSI4IiBoZWlnaHQ9IjE3MCIgc3R5bGU9ImZpbGw6YmxhY2siIC8+CjxyZWN0IHg9IjEzOCIgeT0iMjAiIHdpZHRoPSI1IiBoZWlnaHQ9IjE3MCIgc3R5bGU9ImZpbGw6YmxhY2siIC8+CjxyZWN0IHg9IjE1MSIgeT0iMjAiIHdpZHRoPSIzIiBoZWlnaHQ9IjE3MCIgc3R5bGU9ImZpbGw6YmxhY2siIC8+CjxyZWN0IHg9IjE1NiIgeT0iMjAiIHdpZHRoPSI4IiBoZWlnaHQ9IjE3MCIgc3R5bGU9ImZpbGw6YmxhY2siIC8+CjxyZWN0IHg9IjE2NiIgeT0iMjAiIHdpZHRoPSIzIiBoZWlnaHQ9IjE3MCIgc3R5bGU9ImZpbGw6YmxhY2siIC8+CjxyZWN0IHg9IjE3MSIgeT0iMjAiIHdpZHRoPSI1IiBoZWlnaHQ9IjE3MCIgc3R5bGU9ImZpbGw6YmxhY2siIC8+CjxyZWN0IHg9IjE4NCIgeT0iMjAiIHdpZHRoPSIzIiBoZWlnaHQ9IjE3MCIgc3R5bGU9ImZpbGw6YmxhY2siIC8+CjxyZWN0IHg9IjE5MiIgeT0iMjAiIHdpZHRoPSIxMCIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSIyMDQiIHk9IjIwIiB3aWR0aD0iMyIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSIyMTIiIHk9IjIwIiB3aWR0aD0iNSIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSIyMjIiIHk9IjIwIiB3aWR0aD0iMyIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSIyMzAiIHk9IjIwIiB3aWR0aD0iNyIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSIyNDAiIHk9IjIwIiB3aWR0aD0iMiIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSIyNDUiIHk9IjIwIiB3aWR0aD0iNSIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSIyNTUiIHk9IjIwIiB3aWR0aD0iMyIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSIyNjgiIHk9IjIwIiB3aWR0aD0iNSIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSIyNzUiIHk9IjIwIiB3aWR0aD0iOCIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSIyODUiIHk9IjIwIiB3aWR0aD0iOCIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSIyOTYiIHk9IjIwIiB3aWR0aD0iMiIgaGVpZ2h0PSIxNzAiIHN0eWxlPSJmaWxsOmJsYWNrIiAvPgo8cmVjdCB4PSIzMDEiIHk9IjIwIiB3aWR0aD0iMTAiIGhlaWdodD0iMTcwIiBzdHlsZT0iZmlsbDpibGFjayIgLz4KPHJlY3QgeD0iMzEzIiB5PSIyMCIgd2lkdGg9IjgiIGhlaWdodD0iMTcwIiBzdHlsZT0iZmlsbDpibGFjayIgLz4KPHJlY3QgeD0iMzI0IiB5PSIyMCIgd2lkdGg9IjUiIGhlaWdodD0iMTcwIiBzdHlsZT0iZmlsbDpibGFjayIgLz4KPHJlY3QgeD0iMzM2IiB5PSIyMCIgd2lkdGg9IjgiIGhlaWdodD0iMTcwIiBzdHlsZT0iZmlsbDpibGFjayIgLz4KPHJlY3QgeD0iMzQ2IiB5PSIyMCIgd2lkdGg9IjMiIGhlaWdodD0iMTcwIiBzdHlsZT0iZmlsbDpibGFjayIgLz4KPHJlY3QgeD0iMzUxIiB5PSIyMCIgd2lkdGg9IjUiIGhlaWdodD0iMTcwIiBzdHlsZT0iZmlsbDpibGFjayIgLz4KPHJlY3QgeD0iMjAiIHk9IjIwMCIgd2lkdGg9IjM1MCIgaGVpZ2h0PSI5MCIgc3R5bGU9ImZpbGw6YmxhY2siIC8+Cjx0ZXh0IHg9IjMwIiB5PSIyNDAiIHN0eWxlPSJmaWxsOndoaXRlO2ZvbnQtc2l6ZTozMHB0O3RleHQtYW5jaG9yOnN0YXJ0IiA+NTQ3NDk4PC90ZXh0Pgo8dGV4dCB4PSIzNTAiIHk9IjI3MCIgc3R5bGU9ImZpbGw6d2hpdGU7Zm9udC1zaXplOjUwcHQ7dGV4dC1hbmNob3I6ZW5kIiA+OTk1OTwvdGV4dD4KPC9zdmc+Cg=='
  svg_str = base64.b64decode(svg_str_base64)
  print(svg_str)
  svg_to_image.create_image(svg_str, 'test.jpg') 
"""

import base64
import simple_test
import requests_test
import simple_test




if __name__ == '__main__':
 simple_test.test()

