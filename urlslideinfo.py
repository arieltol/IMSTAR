import matplotlib.pyplot as plt
import math
import urllib, json
import pandas as pd
from pma_python import core
import pmatest

core.connect()    #Connection à PMA.start

#Definition des éléments
nomfich = "C:/usr/pma_python-master/pma_python/H07-16592-1.02.ndpi"
infos = core.get_slide_info(nomfich)
#infos1 = pmatest.print_dict()

print(json)

print("\nLa largeur de la slide est ", infos["Width"])
print("La taille de la slide est ", infos["Height"])