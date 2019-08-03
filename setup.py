from setuptools import setup, find_packages

setup(name='seismology',
      version='0.0.1',
      keywords=["seismology", "eathquake", "python"],
      description='A package for seismic source inversion',
      long_description='I write some python scripts to process and test the work of seismology',

#      url="http://baiqp.info",
      url="",
      author='Qipeng Bai',
      author_email="bqpseismology@gmail.com",

      packages=find_packages('src'),
      package_dir={'':'src'}, # 告诉distutils包都在src下
#      include_package_data=True,
      package_data={
          # 任何包中含有.txt文件，都包含它
          '': ['*.txt'],
          # 包含seismology包data文件夹中的*.data文件
          'seismology': ['data/*.dat'],
      },
      install_requires=[],

      classifiers=[
          "Programming Language :: Python",
          "Development Status :: 0.0.1",
          "Intended Audience :: Science/Research",
          "Operating System :: Unix"],

)
