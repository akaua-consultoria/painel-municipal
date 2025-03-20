import pydeck as pdk


# Função para atualizar o mapa corretamente
def create_map(mun,ufs,map_style_dict, map_style):
    return pdk.Deck(
        map_style=map_style_dict[map_style], 
        initial_view_state=pdk.ViewState(
            latitude=-15.7801, longitude=-47.9292, zoom=3, pitch=0
        ),
        layers=[
            # municipios
            pdk.Layer(
                "GeoJsonLayer",
                data=mun,
                get_fill_color=[200, 30, 0, 120],  # Vermelho semi-transparente
                get_line_color=[255, 255, 255],  # Bordas brancas
                pickable=True
            ),
            # estados (somente contorno)
            pdk.Layer(
                "GeoJsonLayer",
                data=ufs,
                get_fill_color=[0, 0, 0, 0],  # Transparente
                get_line_color=[150, 150, 150, 255], 
                line_width_min_pixels=1,
                pickable=False
            )
        ],
        tooltip={
            "html": "<b>Nome:</b> {NM_MUN}<br>"
                    "<b>UF:</b> {NM_UF}<br>"
                    "<b>Área:</b> {AREA_KM2} km²",
            "style": {
                "backgroundColor": "steelblue",
                "color": "white"
            }
        }
    )