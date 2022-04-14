# coding=utf-8

import xml.dom.minidom
from PIL import Image, ImageDraw, ImageFont

def create_image(svg_data, out_file_name):
  doc = xml.dom.minidom.parseString(svg_data)
  doc.normalize()
  svg = doc.getElementsByTagName('svg')[0]
  # width = int(svg.getAttribute('width'))
  # height = int(svg.getAttribute('height'))
  viewBox = svg.getAttribute('viewBox').split()
  viewBox_x = int(viewBox[0])
  viewBox_y = int(viewBox[1])
  viewBox_width = int(viewBox[2])
  viewBox_height = int(viewBox[3])

  img = Image.new('RGB', (viewBox_width, viewBox_height), 'white')
  idraw = ImageDraw.Draw(img)

  rects = svg.getElementsByTagName("rect")
  for rect in rects:
    x = int(rect.getAttribute('x'))
    y = int(rect.getAttribute('y'))
    width = int(rect.getAttribute('width'))
    height = int(rect.getAttribute('height'))
    style = rect.getAttribute('style')
    i = style.find(':')
    style = style[i + 1:]
    idraw.rectangle((x - viewBox_x, y - viewBox_y, x + width - viewBox_x, y + height - viewBox_y),  fill=style)

  texts = svg.getElementsByTagName("text")
  for text in texts:
    x = int(text.getAttribute('x'))
    y = int(text.getAttribute('y'))
    style = text.getAttribute('style')
    data = text.childNodes[0].data

    i = style.find('fill') + len('fill')
    fill = style[i + 1:]
    i = fill.find(';')
    fill = fill[:i]

    i = style.find('font-size') + len('font-size')
    font_size = style[i + 1:]
    i = font_size.find(';')
    font_size = font_size[:i]
    i = font_size.find('pt')
    font_size = int(font_size[:i])

    i = style.find('text-anchor') + len('text-anchor')
    text_anchor = style[i + 1:]
    if text_anchor == 'start':
      text_anchor = 'left'
    if text_anchor == 'end':
      text_anchor = 'right'

    font_size = font_size + 10
    font = ImageFont.truetype("arial.ttf", size=font_size)
    size = idraw.textsize(data, font=font)
    if text_anchor == 'left':
      idraw.multiline_text((int(x) - viewBox_x, int(y) - size[1] - viewBox_y), data, font=font)
    else:
      idraw.multiline_text((int(x) - size[0] - viewBox_x, int(y) - size[1] - viewBox_y), data, font=font)
    # Масштабирование
    # img.thumbnail((60,40))

  img.save(out_file_name)


