FROM continuumio/anaconda3:2022.10

LABEL maintainer="Jingmin Zhang <jmzhang1911@gmail.com>" app="SpatialToolsVision"

RUN conda create -n spatial_tools python=3.9.12 && \
    conda install gcc -c conda-forge && \
    conda activate spatial_tools && \
    pip install SpatialTools -i https://pypi.tuna.tsinghua.edu.cn/simple some-package


