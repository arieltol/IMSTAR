import matplotlib.pyplot as plt
import math
import pandas as pd
from pma_python import core
core.connect()    #Connection à PMA.start

#Definition des éléments
nomfich = "C:/usr/pma_python-master/pma_python/H07-16592-1.02.ndpi"
infos = core.get_slide_info(nomfich)
img_tile = [core.get_tile(nomfich, x =x, zoomlevel = x) for x in range (7)] #liste des images selon le zoom 

#Affiche la tuile avec le zoom
for i in range(1, 7): #parcourt les elements de la liste à ploter 
    plt.subplot(1,7,i)
    plt.imshow(img_tile[i-1])  
num_lev = len(core.get_zoomlevels_dict(nomfich))
plt.show()


#Fonction qui print tous les noms des elements de dict
def print_dict (dict):
    for nom in dict.keys():  
        print(nom, "=", dict[nom])

#Fonction pour définir la liste et afficher les MetaData sous forme matricielle contenant name et value
def print_list(li):
    for nom in li:
        print(nom)  
print("Voici la liste des MetaData")
print_list(infos["MetaData"])


print("\nVoici la fiche") 
print_dict(infos)


#Plot le barcode
#barcode = core.get_barcode_image(nomfich)
#barcode.show()

print("\nVoici mon truc", infos["MetaData"][2]) #print seulement SlideInfo
print(type(infos["MetaData"][0])) 

#Print sous forme de ligne les valeurs de SlideInfo en decoupant par value et key
slideInfoDict = {}
for i in range(len(infos["MetaData"])):
     if infos["MetaData"][i]['Name'] == "SlideInfo":
       slideInfoDict = infos["MetaData"][i]
       break
a = slideInfoDict['Value'].split("\r\n") #print sous forme de ligne avec separateur
print(a)




#df_levels = pd.DataFrame(level_infos, columns=["res_x", "res_y", "tiles_x", "tiles_y", "approx_mag", "exact_mag", "micropp"])
#print(nomfich)
#print(df_levels)

#tile_sz = core.get_number_of_tiles(nomfich, zoomlevel = 1) # zoomlevel 1
#for xTile in range(0, tile_sz[0]): #parcourt une liste d'element 
#    for yTile in range(0, tile_sz[1]):
#        tile = core.get_tile(nomfich, x = xTile, y = yTile, zoomlevel = 1)
#        tile.show()
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