import streamlit as st
import pandas as pd
import geopandas as gpd
import pydeck as pdk

from src import get_data
from src import plots

## Importando dados
shp = get_data.get_shp()
mcmv = get_data.get_mcmv()


## HOME
st.title('Painel municipal')
# mapa
map_style_dict = {
    'Apenas municípios': 'blank',
    'Padrão': 'road',
    'Mapa claro':'light',
    'Mapa escuro':'dark'
}
map_style = st.selectbox("Estilo do mapa",list(map_style_dict))
st.pydeck_chart(plots.create_map(shp['mun'],shp['ufs'],map_style_dict, map_style))


shp['mun']

# minha casa minha vida
mcmv['subsidiado']