import csv
import detect_color
import cv2
import urllib.request

def adjust_link(link,vp_id):
  if int(vp_id) < 35200:
    try:
      urllib.request.urlopen('http://arc.media.showroomprive.com'+link[28:])
      return 'http://arc.media.showroomprive.com'+link[28:]
    except urllib.error.HTTPError:
        return '404 Error'
  else:
    try:
      urllib.request.urlopen('http://'+link[2:])
      return 'http://'+link[2:]
    except urllib.error.HTTPError:
      try:
        urllib.request.urlopen('http://media.showroomprive.com'+link[28:])
        return 'http://media.showroomprive.com'+link[28:]
      except urllib.error.HTTPError:
        return '404 Error'


c = csv.writer(open('compare_colors.csv','w'))
cr = csv.reader(open('data_showroom.csv','r'))
c.writerow(['DESCRIPTION','SHOWROOM COLOR', 'ALGO HEXA1', 'ALGO CONFUSED1', 'ALGO PRECISE1', 'ALGO HEXA2', 'ALGO CONFUSED2', 'ALGO PRECISE2','ALGO HEXA3', 'ALGO CONFUSED3', 'ALGO PRECISE3','ALGO HEXA4', 'ALGO CONFUSED4', 'ALGO PRECISE4','ALGO HEXA5', 'ALGO CONFUSED5', 'ALGO PRECISE5'])

for row in cr :
  new_line = []
  description = [row[7]]
  new_line+= description
  coloris = row[9]
  if '<b>Coloris</b> :' in coloris :
    indent = coloris.index('<b>Coloris</b> :')+16
    color = ''
    while indent<len(coloris) and row[9][indent] != '<':
      color += str(row[9][indent])
      indent +=1
    new_line+=[color]
  else :
    new_line += [None]

  indent = 17
  while row[indent][-6:]!= 'um.jpg' and indent<30:
    indent+=1
  link_basic = row[indent]
  for i in range(1,6):
    link = adjust_link(link_basic[:-12]+str(i)+link_basic[-11:],row[0])
    if link == '404 Error':
      new_line+= [None,None,None]
      next
    else:
      print(link)
      urllib.request.urlretrieve(link, 'image.jpg')
      img = cv2.imread('image.jpg')
      color_algo = detect_color.image_color(img)
      [hexa, globale, detailled]= [color_algo['hexa color'],color_algo['global name'],color_algo['detailled name']]
      new_line+=[hexa,globale,detailled]
  c.writerow(new_line)
  print('new_line')





