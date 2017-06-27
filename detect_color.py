from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import webcolors
import math


# def get_colour_name(rgb_triplet):
#   min_colours = {}
#   for key, name in webcolors.css21_hex_to_names.items():
#       r_c, g_c, b_c = webcolors.hex_to_rgb(key)
#       #distance quadratique
#       rd = (r_c - rgb_triplet[2]) ** 2
#       gd = (g_c - rgb_triplet[1]) ** 2
#       bd = (b_c - rgb_triplet[0]) ** 2
#       min_colours[math.sqrt(rd + gd + bd)] = name
#   return min_colours[min(min_colours.keys())]

SimpleColorMap={}
SimpleColorMap['Aqua']="#00FFFF"
SimpleColorMap['Black']="#000000"
SimpleColorMap['Blue']="#0000FF"
SimpleColorMap['Fuschia']="#FF00FF"
SimpleColorMap['Green']="#008000"
SimpleColorMap['Gray']="#808080"
SimpleColorMap['Orange'] = "#FFA500"
SimpleColorMap['Silver']="#C0C0C0"
SimpleColorMap['Teal'] = "#008080"
SimpleColorMap['White'] = "#FFFFFF"
SimpleColorMap['Yellow'] = "#FFFF00"


# -----------------------------------------------------------

WebColorMap = {}
# WebColorMap["AliceBlue"] = "#F0F8FF"
# WebColorMap["AntiqueWhite"] = "#FAEBD7"
WebColorMap["Aqua"] = "#00FFFF"
WebColorMap["Aquamarine"] = "#7FFFD4"
WebColorMap["Azure"] = "#F0FFFF"
WebColorMap["Beige"] = "#F5F5DC"
# WebColorMap["Bisque"] = "#FFE4C4"
WebColorMap["Black"] = "#000000"
# WebColorMap["BlanchedAlmond"] = "#FFEBCD"
WebColorMap["Blue"] = "#0000FF"
WebColorMap["BlueViolet"] = "#8A2BE2"
WebColorMap["Brown"] = "#A52A2A"
# WebColorMap["BurlyWood"] = "#DEB887"
# WebColorMap["CadetBlue"] = "#5F9EA0"
WebColorMap["Chartreuse"] = "#7FFF00"
WebColorMap["Chocolate"] = "#D2691E"
WebColorMap["Coral"] = "#FF7F50"
# WebColorMap["CornflowerBlue"] = "#6495ED"
# WebColorMap["Cornsilk"] = "#FFF8DC"
WebColorMap["Cream"] ="#FCFBE3"
WebColorMap["Crimson"] = "#DC143C"
WebColorMap["Cyan"] = "#00FFFF"
WebColorMap["DarkBlue"] = "#00008B"
WebColorMap["DarkCyan"] = "#008B8B"
# WebColorMap["DarkGoldenRod"] = "#B8860B"
WebColorMap["DarkGrey"] = "#A9A9A9"
WebColorMap["DarkGreen"] = "#006400"
WebColorMap["DarkKhaki"] = "#BDB76B"
WebColorMap["DarkMagenta"] = "#8B008B"
# WebColorMap["DarkOliveGreen"] = "#556B2F"
WebColorMap["DarkOrange"] = "#FF8C00"
# WebColorMap["DarkOrchid"] = "#9932CC"
WebColorMap["DarkRed"] = "#8B0000"
# WebColorMap["DarkSalmon"] = "#E9967A"
# WebColorMap["DarkSeaGreen"] = "#8FBC8F"
# WebColorMap["DarkSlateBlue"] = "#483D8B"
# WebColorMap["DarkSlateGrey"] = "#2F4F4F"
WebColorMap["DarkTurquoise"] = "#00CED1"
WebColorMap["DarkViolet"] = "#9400D3"
WebColorMap["DeepPink"] = "#FF1493"
# WebColorMap["DeepSkyBlue"] = "#00BFFF"
WebColorMap["DimGrey"] = "#696969"
# WebColorMap["DodgerBlue"] = "#1E90FF"
# WebColorMap["FireBrick"] = "#B22222"
# WebColorMap["FloralWhite"] = "#FFFAF0"
# WebColorMap["ForestGreen"] = "#228B22"
WebColorMap["Fuchsia"] = "#FF00FF"
# WebColorMap["Gainsboro"] = "#DCDCDC"
# WebColorMap["GhostWhite"] = "#F8F8FF"
WebColorMap["Gold"] = "#FFD700"
# WebColorMap["GoldenRod"] = "#DAA520"
WebColorMap["Grey"] = "#808080"
WebColorMap["Green"] = "#008000"
WebColorMap["GreenYellow"] = "#ADFF2F"
# WebColorMap["HoneyDew"] = "#F0FFF0"
# WebColorMap["HotPink"] = "#FF69B4"
# WebColorMap["IndianRed"] = "#CD5C5C"
WebColorMap["Indigo"] = "#4B0082"
WebColorMap["Ivory"] = "#FFFFF0"
WebColorMap["Khaki"] = "#F0E68C"
WebColorMap["Lavender"] = "#E6E6FA"
# WebColorMap["LavenderBlush"] = "#FFF0F5"
# WebColorMap["LawnGreen"] = "#7CFC00"
# WebColorMap["LemonChiffon"] = "#FFFACD"
WebColorMap["LightBlue"] = "#ADD8E6"
# WebColorMap["LightCoral"] = "#F08080"
WebColorMap["LightCyan"] = "#E0FFFF"
# WebColorMap["LightGoldenRodYellow"] = "#FAFAD2"
WebColorMap["LightGrey"] = "#D3D3D3"
WebColorMap["LightGreen"] = "#90EE90"
WebColorMap["LightPink"] = "#FFB6C1"
# WebColorMap["LightSalmon"] = "#FFA07A"
# WebColorMap["LightSeaGreen"] = "#20B2AA"
# WebColorMap["LightSkyBlue"] = "#87CEFA"
# WebColorMap["LightSlateGrey"] = "#778899"
# WebColorMap["LightSteelBlue"] = "#B0C4DE"
WebColorMap["LightYellow"] = "#FFFFE0"
WebColorMap["Lime"] = "#00FF00"
# WebColorMap["LimeGreen"] = "#32CD32"
# WebColorMap["Linen"] = "#FAF0E6"
WebColorMap["Magenta"] = "#FF00FF"
WebColorMap["Maroon"] = "#800000"
# WebColorMap["MediumAquaMarine"] = "#66CDAA"
WebColorMap["MediumBlue"] = "#0000CD"
# WebColorMap["MediumOrchid"] = "#BA55D3"
WebColorMap["MediumPurple"] = "#9370D8"
# WebColorMap["MediumSeaGreen"] = "#3CB371"
# WebColorMap["MediumSlateBlue"] = "#7B68EE"
# WebColorMap["MediumSpringGreen"] = "#00FA9A"
WebColorMap["MediumTurquoise"] = "#48D1CC"
# WebColorMap["MediumVioletRed"] = "#C71585"
WebColorMap["MidnightBlue"] = "#191970"
# WebColorMap["MintCream"] = "#F5FFFA"
# WebColorMap["MistyRose"] = "#FFE4E1"
WebColorMap["Moccasin"] = "#FFE4B5"
# WebColorMap["NavajoWhite"] = "#FFDEAD"
WebColorMap["Navy"] = "#000080"
# WebColorMap["OldLace"] = "#FDF5E6"
WebColorMap["Olive"] = "#808000"
# WebColorMap["OliveDrab"] = "#6B8E23"
WebColorMap["Orange"] = "#FFA500"
WebColorMap["OrangeRed"] = "#FF4500"
# WebColorMap["Orchid"] = "#DA70D6"
# WebColorMap["PaleGoldenRod"] = "#EEE8AA"
WebColorMap["PaleGreen"] = "#98FB98"
WebColorMap["PaleTurquoise"] = "#AFEEEE"
# WebColorMap["PaleVioletRed"] = "#D87093"
# WebColorMap["PapayaWhip"] = "#FFEFD5"
# WebColorMap["PeachPuff"] = "#FFDAB9"
# WebColorMap["Peru"] = "#CD853F"
WebColorMap["Pink"] = "#FFC0CB"
# WebColorMap["Plum"] = "#DDA0DD"
# WebColorMap["PowderBlue"] = "#B0E0E6"
WebColorMap["Purple"] = "#800080"
WebColorMap["Red"] = "#FF0000"
WebColorMap["RosyBrown"] = "#BC8F8F"
WebColorMap["RoyalBlue"] = "#4169E1"
# WebColorMap["SaddleBrown"] = "#8B4513"
WebColorMap["Salmon"] = "#FA8072"
# WebColorMap["SandyBrown"] = "#F4A460"
WebColorMap["SeaGreen"] = "#2E8B57"
# WebColorMap["SeaShell"] = "#FFF5EE"
# WebColorMap["Sienna"] = "#A0522D"
WebColorMap["Silver"] = "#C0C0C0"
WebColorMap["SkyBlue"] = "#87CEEB"
# WebColorMap["SlateBlue"] = "#6A5ACD"
# WebColorMap["SlateGrey"] = "#708090"
WebColorMap["Snow"] = "#FFFAFA"
# WebColorMap["SpringGreen"] = "#00FF7F"
# WebColorMap["SteelBlue"] = "#4682B4"
WebColorMap["Tan"] = "#D2B48C"
WebColorMap["Teal"] = "#008080"
# WebColorMap["Thistle"] = "#D8BFD8"
WebColorMap["Tomato"] = "#FF6347"
WebColorMap["Turquoise"] = "#40E0D0"
WebColorMap["Violet"] = "#EE82EE"
# WebColorMap["Wheat"] = "#F5DEB3"
WebColorMap["White"] = "#FFFFFF"
# WebColorMap["WhiteSmoke"] = "#F5F5F5"
WebColorMap["Yellow"] = "#FFFF00"
WebColorMap["YellowGreen"] = "#9ACD32"

def rgbFromStr(facecolor):
  # s starts with a #.
  # turns hexa number into rgb
  r, g, b = int(facecolor[1:3],16), int(facecolor[3:5], 16),int(facecolor[5:7], 16)
  return r, g, b

def findNearestColorName(three_colored_array,Map=WebColorMap):
  R,G,B = three_colored_array[2],three_colored_array[1],three_colored_array[0]
  mindiff = None
  for d in Map:
      r, g, b = rgbFromStr(Map[d])
      diff = (abs(R -r)*256)**2 + (abs(G-g)* 256)**2 + (abs(B- b)* 256)**2
      if mindiff is None or diff < mindiff:
          mindiff = diff
          mincolorname = d
  return mincolorname

def chop_image(img):
  #img doit être un objet cv2

  H, W, dim = img.shape
  # découpage en 9
  # I1 = img[0:H//3,0:W//3]
  # I2 = img[0:H//3,W//3:2*W//3]
  # I3 = img[0:H//3,2*W//3:W]

  # I4 = img[H//3:2*H//3,2*W//3:W]
  # I5 = img[2*H//3:H,2*W//3:W]

  # I6 = img[2*H//3:H,W//3:2*W//3]
  # I7 = img[2*H//3:H,0:W//3]

  # I8 = img[H//3:2*H//3,0:W//3]

  # I9 = img[H//3:2*H//3,W//3:2*W//3]
  # table = [I2,I9,I8,I4,I1,I3,I5,I7,I6]

  # img = img[(int(2*H/6)):(int(4*H/6)), (int(2*W/6)):(int(4*W/6)), :]


  I1 = img[0:H//5,0:W//5]
  I2 = img[0:H//5,W//5:2*W//5]
  I3 = img[0:H//5,2*W//5:3*W//5]
  I4 = img[0:H//5,3*W//5:4*W//5]
  I5 = img[0:H//5,4*W//5:W]

  I6 = img[H//5:2*H//5,4*W//5:W]
  I7 = img[2*H//5:3*H//5,4*W//5:W]
  I8 = img[3*H//5:4*H//5,4*W//5:W]
  I9 = img[4*H//5:H,4*W//5:W]

  I10 = img[4*H//5:H,3*W//5:4*W//5]
  I11 = img[4*H//5:H,2*W//5:3*W//5]
  I12 = img[4*H//5:H,W//5:2*W//5]
  I13 = img[4*H//5:H,0:W//5]

  I14 = img[3*H//5:4*H//5,0:W//5]
  I15 = img[2*H//5:3*H//5,0:W//5]
  I16 = img[H//5:2*H//5,0:W//5]

  I17 = img[H//5:2*H//5,W//5:2*W//5]
  I18 = img[H//5:2*H//5,2*W//5:3*W//5]
  I19 = img[H//5:2*H//5,3*W//5:4*W//5]

  I20 = img[2*H//5:3*H//5,3*W//5:4*W//5]
  I21 = img[3*H//5:4*H//5,3*W//5:4*W//5]

  I22 = img[3*H//5:4*H//5,2*W//5:3*W//5]
  I23 = img[3*H//5:4*H//5,W//5:2*W//5]

  I24 = img[2*H//5:3*H//5,W//5:2*W//5]

  I25 = img[2*H//5:3*H//5,2*W//5:3*W//5]
  table = [I25,I22,I18,I23,I12,I24,I20,I11,I3,I17,I2,I19,I4,I1,I10,I21,I9]
  return table


def image_color(image):
  # img doit etre un objet cv2

  white = True
  indent = 0

  while white :
    if indent == len(chop_image(image))-1:
      img = chop_image(image)[0]
      height, width, dim = img.shape

      img_vec = np.reshape(img, [height * width, dim] )

      kmeans = KMeans(n_clusters=3)
      kmeans.fit( img_vec )


      unique_l, counts_l = np.unique(kmeans.labels_, return_counts=True)
      sort_ix = np.argsort(counts_l)
      sort_ix = sort_ix[::-1]

      three_colored_array = kmeans.cluster_centers_[sort_ix][0]
      color = {}
      facecolor = '#%02x%02x%02x' % (int(three_colored_array[2]), int(three_colored_array[1]), int(three_colored_array[0]) )
      color['hexa color']=facecolor
      # color['global name']=get_colour_name(three_colored_array)
      color['global name']=findNearestColorName(three_colored_array,SimpleColorMap)
      color['detailled name']=findNearestColorName(three_colored_array)
      return color
    else:
      img = chop_image(image)[indent]
      # img = img[(int(2*height/6)):(int(4*height/6)), (int(2*width/6)):(int(4*width/6)), :]
      height, width, dim = img.shape

      img_vec = np.reshape(img, [height * width, dim] )

      kmeans = KMeans(n_clusters=3)
      kmeans.fit( img_vec )


      unique_l, counts_l = np.unique(kmeans.labels_, return_counts=True)
      sort_ix = np.argsort(counts_l)
      sort_ix = sort_ix[::-1]

      fig = plt.figure()
      ax = fig.add_subplot(111)
      x_from = 0.05
      # print(indent)

      # for cluster_center in kmeans.cluster_centers_[sort_ix]:
      #     ax.add_patch(patches.Rectangle( (x_from, 0.05), 0.29, 0.9, alpha=None,
      #                                     facecolor='#%02x%02x%02x' % (int(cluster_center[2]), int(cluster_center[1]), int(cluster_center[0]) ) ) )
      #     x_from = x_from + 0.31

      # plt.show()

      three_colored_array = kmeans.cluster_centers_[sort_ix][0]
      color = {}
      facecolor = '#%02x%02x%02x' % (int(three_colored_array[2]), int(three_colored_array[1]), int(three_colored_array[0]) )
      color['hexa color']=facecolor
      # color['global name']=get_colour_name(three_colored_array)
      color['global name']=findNearestColorName(three_colored_array,SimpleColorMap)
      color['detailled name']=findNearestColorName(three_colored_array)
      if color['global name']!='White':
        white = False
        return color
      if indent<5:
        try:
          three_colored_array = kmeans.cluster_centers_[sort_ix][1]
          color = {}
          facecolor = '#%02x%02x%02x' % (int(three_colored_array[2]), int(three_colored_array[1]), int(three_colored_array[0]) )
          color['hexa color']=facecolor
          # color['global name']=get_colour_name(three_colored_array)
          color['global name']=findNearestColorName(three_colored_array,SimpleColorMap)
          color['detailled name']=findNearestColorName(three_colored_array)
          if color['global name']!='White':
            white = False
            return color
        except IndexError:
          'Out of bound'
      indent +=1




img = cv2.imread('oreille.jpg')
print(image_color(img))





