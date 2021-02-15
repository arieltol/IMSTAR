import matplotlib.pyplot as plt
import math
import urllib, json
import pandas as pd
from pma_python import core
core.connect()    #Connection à PMA.start

#Definition des éléments
nomfich = "C:/usr/pma_python-master/pma_python/H07-16592-1.02.ndpi"
infos = core.get_slide_info(nomfich)


print(infos)