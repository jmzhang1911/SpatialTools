#!/share/nas2/genome/biosoft/Python//3.7.3/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/12/6 15:41
# @Author : jmzhang
# @Email : zhangjm@biomarker.com.cn


import spatial_tools_v2

if __name__ == '__main__':
    spatial_tools_v2.SpatialApp.run_dash(port=2008, debug=True)
