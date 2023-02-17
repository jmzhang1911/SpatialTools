from setuptools import setup
from setuptools import find_packages

VERSION = '2.1.15'

setup(
    name='SpatialTools',  # package name
    version='2.1.15',  # package version
    description='spatial tools for S1000',  # package description
    python_requires='>=3.9',
    packages=find_packages(),
    install_requires=['numpy>=1.23.0',
                      'pandas>=1.4.3',
                      'Pillow>=9.2.0',
                      'anndata>=0.8.0',
                      'kiwisolver>=1.4.4',
                      'pyzmq>=23.2.1',
                      'scipy>=1.9.1',
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
                      'packaging==21.3.0',
                      'louvain>=0.8.0',
                      'leidenalg>=0.9.0',
                      'igraph>=0.10.1'],
    zip_safe=False,
    scripts=['spatial_tools/run_spatial_tools', 'spatial_tools/run_app.py']
)
