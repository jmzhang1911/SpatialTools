from setuptools import setup
from setuptools import find_packages

VERSION = '2.1.3'

setup(
    name='SpatialTools',  # package name
    version='2.1.3',  # package version
    description='spatial tools for S1000',  # package description
    packages=find_packages(),
    install_requires=['anndata>=0.8.0',
                      'scanpy>=1.9.1',
                      'dash>=2.6.0',
                      'dash-bootstrap-components>=1.2.0',
                      'dash-core-components>=2.0.0',
                      'dash-daq>=0.5.0',
                      'dash-html-components>=2.0.0',
                      'dash-table>=5.0.0',
                      'jupyter-dash>=0.4.2',
                      'matplotlib>=3.6.0',
                      'matplotlib-inline>=0.1.6',
                      'plotly>=5.10.0',
                      # 'scikit-learn==1.1.2',
                      'jsonpickle>=3.0.0',
                      'pickleshare>=0.7.5',
                      'seaborn>=0.12.0',
                      'dash-uploader==0.7.0a1',
                      'packaging==21.3.0'],
    zip_safe=False,
    scripts=['spatial_tools/spatial_tools.py', 'spatial_tools/run_app.py']
)
