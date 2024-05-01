from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
  long_desc = readme.read()

setup(
  name='isontheedge_sc_downloader',  # Replace with your module name
  version='0.1.26',  # Replace with your version number
  description='A tool to download tracks from soundcloud.com',
  long_description=long_desc,
  long_description_content_type='text/markdown',
  packages=find_packages(where='isontheedge_sc_downloader'),
  author='Suyash Behera',
  author_email='sne9x@outlook.com',
  url='https://github.com/Suyash458/soundcloud-dl',
  download_url='https://github.com/Suyash458/soundcloud-dl/archive/master.zip',
  keywords=['Downloader', 'Python', 'soundcloud'],
  install_requires=[
      'soundcloud~=2.0',  # Example with version range
      'requests>=2.27.1',
      'mutagen',
      'six',
      'halo',
      'tqdm',
  ],
  entry_points={
      'console_scripts': ['isontheedge_sc_downloader=isontheedge_sc_downloader.main:main',
                          'isontheedge-sc-dl=isontheedge_sc_downloader.main:main'],
  },
  classifiers=[
      'Development Status :: 5 - Production/Stable',
  ],
)
