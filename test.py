import matplotlib.pyplot as plt
import math
import pandas as pd
from pma_python import core
core.connect()    #Connection à PMA.start

def print_dict (dict):
    for nom in dict.keys(): #print toutes les nom des dict 
        print(nom, "=", dict[nom])


nomfich = "C:/usr/pma_python-master/pma_python/H07-16592-1.02.ndpi"
#nomfich1_vsi = "D:/Data/VSISampleFilePackage.v2.6/MIA_Multilayer_24bit_RGB_JPEG.vsi"


img_tile = [core.get_tile(nomfich, x =x, zoomlevel = x) for x in range (7)] #liste des images selon le zoom  ##aranger ca avec la resoo!!!!
level_infos = []

for i in range(1, 7): #parcourt les elements de la liste à ploter 
    plt.subplot(1,7,i)
    plt.imshow(img_tile[i-1])  

num_lev = len(core.get_zoomlevels_dict(nomfich))
plt.show()
print("Voici la fiche")
barcode = core.get_barcode_image(nomfich)
barcode.show()


info = core.get_slide_info(nomfich)
print_dict(info)
#print_dict( info{"MetaData"})


#get_max_zoomlevel(nomfich, sessionID=None)





df_levels = pd.DataFrame(level_infos, columns=["res_x", "res_y", "tiles_x", "tiles_y", "approx_mag", "exact_mag", "micropp"])
print(nomfich)
print(df_levels)

tile_sz = core.get_number_of_tiles(nomfich, zoomlevel = 1) # zoomlevel 1
for xTile in range(0, tile_sz[0]): #parcourt une liste d'element 
    for yTile in range(0, tile_sz[1]):
        tile = core.get_tile(nomfich, x = xTile, y = yTile, zoomlevel = 1)
        #tile.show()
#def plot_slide_as_tiles(slide_ref, zoomlevel):
 #   dims = core.get_zoomlevels_dict(slide_ref) #liste complete pour chaque level 
#
  #  max_x = dims[0]
 #   max_y = dims[1]
  #  plt.subplots(max_y, max_x, figsize=(15,15))
   # for x in range(0,max_x):
    #    for y in range(0,max_y):
     #       plt.subplot(max_y, max_x, (x+1) + y * max_x)
      #      plt.imshow(core.get_tile(slide_ref, zoomlevel = zoomlevel, x = x, y = y))
    #plt.plot(figsize=(200,100))
    #plt.show()
#plt.show()


#def len_dims():
#    dims = core.get_zoomlevels_dict(slide_ref) #liste complete pour chaque level 
 #   print(len(dims))

    
#def __init__(
 #       self, width=None, height=None, tile_size=254, tile_overlap=1, tile_format="jpg"
  #  ):
   #     self.width = width
    #    self.height = height
     #   self.tile_size = tile_size
      #  self.tile_overlap = tile_overlap
       # self.tile_format = tile_format
        #self._num_levels = None

#def num_levels(self):
 #   """Number of levels in the pyramid."""
  #  if self._num_levels is None:
   #     max_dimension = max(self.width, self.height)
    #    self._num_levels = int(math.ceil(math.log(max_dimension, 2))) + 1
    #return self._num_levels

#def get_scale(self, level):
 #   """Scale of a pyramid level."""
  #  assert 0 <= level and level < self.num_levels, "Invalid pyramid level"
   # max_level = self.num_levels - 1
    #return math.pow(0.5, max_level - level)

#def get_dimensions(self, level):
 #   """Dimensions of level (width, height)"""
  #  assert 0 <= level and level < self.num_levels, "Invalid pyramid level"
   # scale = self.get_scale(level)
    #width = int(math.ceil(self.width * scale))
    #height = int(math.ceil(self.height * scale))
    #return (width, height)
