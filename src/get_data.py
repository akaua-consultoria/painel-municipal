import pandas as pd
import geopandas as gpd

from src import aux_functions as aux

## DADOS GEOGRÁFICOS
# malha municipal
def get_shp_mun(path='data/malha_municipal/BR_Municipios_2023.parquet'):
    gdf = gpd.read_parquet(path)
    # Converter o GeoDataFrame para JSON para o Pydeck
    gdf = gdf.__geo_interface__
    return gdf
# malha de UFs
def get_shp_ufs(path='data/malha_uf/BR_UF_2023.parquet'):
    gdf = gpd.read_parquet(path)
    # Converter o GeoDataFrame para JSON para o Pydeck
    gdf = gdf.__geo_interface__
    return gdf

def get_shp():
    return {
        'mun':get_shp_mun(),
        'ufs':get_shp_ufs()
    }

## MINHA CASA MINHA VIDA
def get_mcmv_subsidiado(path='data/mcmv_subsidiado_dados_abertos_ogu_2024122.csv'):
    dtype_dict = {
    'txt_cep': 'object',
    }

    df = pd.read_csv(path,
                         sep = ';',  dtype=dtype_dict,
                         parse_dates=['data_referencia','dt_assinatura'], 
                         date_format='%d/%m/%Y',
                         converters={'val_contratado_total': aux.br_to_float,
                                     'val_desembolsado':aux.br_to_float,
                                     'cod_ibge':aux.extract_dots})
    # corrigindo tipo das quantidades de unidades
    df['qtd_uh'] = df['qtd_uh'].fillna(0).astype('int32')
    df['qtd_uh_entregues'] = df['qtd_uh_entregues'].fillna(0).astype('int32')
    df['qtd_uh_vigentes'] = df['qtd_uh_vigentes'].fillna(0).astype('int32')
    df['qtd_uh_distratadas'] = df['qtd_uh_distratadas'].fillna(0).astype('int32')
    # pct de entregues
    df['pct_entregues'] = df['qtd_uh_entregues'] / df['qtd_uh']
    # valor contratado por unidade contratada
    df['val_contratado_por_uh'] = df['val_contratado_total'] / df['qtd_uh']
    # valor desembolsado por unidade contratada
    df['val_desembolsado_por_uh'] = df['val_desembolsado'] / df['qtd_uh']
    # valor contratado por unidade entregue
    df['val_contratado_por_uh_entregue'] = df['val_contratado_total'] / df['qtd_uh_entregues']
    # valor desembolsado por unidade entregue
    df['val_desembolsado_por_uh_entregue'] = df['val_desembolsado'] / df['qtd_uh_entregues']

    return df

def get_mcmv_financiado():
    return None


def get_mcmv():
    return {
        'subsidiado':get_mcmv_subsidiado(),
        'financiado':get_mcmv_financiado()
    }