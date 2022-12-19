#!/share/nas2/genome/biosoft/Python//3.7.3/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/19 13:31
# @Author : jmzhang
# @Email : zhangjm@biomarker.com.cn
import logging

import spatial_tools

logging.info('xxxxxx')
app = spatial_tools.SpatialApp.run_dash(debug=False, return_app=True)
server = app.server

if __name__ == '__main__':

    app.run_server(debug=False, mode='external')
