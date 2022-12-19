#!/share/nas2/genome/biosoft/Python//3.7.3/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/19 13:31
# @Author : jmzhang
# @Email : zhangjm@biomarker.com.cn

import spatial_tools

app = spatial_tools.SpatialApp.run_dash(debug=False, return_app=True)
server = app.server
app.run_server(debug=False, mode='external')
