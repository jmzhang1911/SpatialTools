![Stars](https://static.pepy.tech/personalized-badge/SpatialTools?period=total&units=international_system&left_color=grey&right_color=orange&left_text=Downloads)
![Stars](https://img.shields.io/pypi/v/SpatialTools.svg)
## SpatialTools - spatial tools for S1000
Seurat，scanpy等分析工具为空间转录的分析和可视化提供了强大的API，但仅支持主流的10x Visium，Slide-seq v2等平台，无法适用于自研的空间转转录组测序平台。在这里推出spatial_tools，应用于自研空间转录组平台(如：S1000)的可视化及交互。主要功能和特点：

- 离散型/连续性变量的绘图，分面，仅展示某些cluster等
- 输入支持AnnData对象或pd.DataFrame对象
- 局部放大功能
- 自定义展示(可自定义展示高清He，低清He，或不展示He)
- 交互功能(如：可使用dash的选框或套索工具获取选择的barcode列表等)
- 自定义强(支持自定义配色，透明度，标题，图例调整等)
- 可迅速迭代，将逐步完善功能

安装：使用pip直接安装:
```
pip install SpatialTools
```

通过网页访问：https://spatialtoolsvision.onrender.com/
