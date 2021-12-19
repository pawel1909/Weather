import sys, os
from setuptools import setup

dependencies = ['Pillow', 'numpy', 'qrcode', ]

if os.path.exists('/sys/bus/platform/drivers/gpiomem-bcm2835'):
    dependencies += ['RPi.GPIO', 'spidev']
else:
    dependencies += ['Jetson.GPIO']

setup(
    name='waveshare-epd',
    description='Weather Display, moduły do kontroli ekranu skopiowane z repozutorium https://github.com/waveshare/e-Paper',
    author='...',
    package_dir={'': 'lib'},
    packages=['waveshare_epd'],
    install_requires=dependencies,
)

