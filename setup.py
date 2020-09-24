# coding=utf-8
import setuptools

setuptools.setup(name='thermalbuildingmodel',
                 version='1.0.0',
                 description='Thermal building model, based on guideline VDI 6007-1',
                 url='https://github.com/ThomasSchuetz/ThermalBuildingModel',
                 license='MIT License',
                 packages=['thermal_building_model'],
                 install_requires=['numpy'],
                 classifiers=[
                         "Programming Language :: Python :: 3",
                         "License :: OSI Approved :: MIT License",
                         "Operating System :: OS Independent",
                 ],
                 )