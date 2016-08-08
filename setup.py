from setuptools import setup

setup(name='aztecdecoder',
      version='1.0.0',
      description='Biblioteka programistyczna pozwalająca na dekodowanie danych z dowodów rejestracyjnych pojazdów samochodowych zapisanych w formie kodu AZTEC 2D.',
      keywords = "aztec2d aztec-decoder aztec",
      url='https://www.pelock.com',
      author='Bartosz Wójcik',
      author_email='support@pelock.com',
      license='Apache-2.0',
      packages=['pelock'],
      zip_safe=False,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Natural Language :: Polish",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
      ],
)