#!/share/nas2/genome/biosoft/Python//3.7.3/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/19 13:31
# @Author : jmzhang
# @Email : zhangjm@biomarker.com.cn

from pathlib import Path
import spatial_tools
import pandas as pd
import logging


mouse_len = spatial_tools.SpatialTools.load_from(str(Path(__file__) / 'spatial_tools/demo_data/mouse.len'))
adata = pd.read_csv(str(Path(__file__) / 'spatial_tools/demo_data/L7_heAuto_RCTD.xls'), sep='\t')

app = spatial_tools.SpatialApp.run_dash(debug=False, return_app=True, spatial_tools_obj=mouse_len, adata=adata)
server = app.server

if __name__ == '__main__':
    app.run_server(debug=False, mode='external')
