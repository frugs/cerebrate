from setuptools import setup, find_packages


setup(
    name='cerebrate',
    version='0.0.3',
    description='Offline Replay Manager for StarCraft II',
    author='Hugo Wainwright',
    author_email='wainwrighthugo@gmail.com',
    url='https://github.com/frugs/cerebrate',
    download_url='https://github.com/frugs/cerebrate/tarball/0.0.3',
    packages=find_packages(),
    py_modules=['cerebrate'],
    include_package_data=True,
    install_requires=[
        'tinydb',
        'click',
        'ujson'
    ],
    entry_points='''
        [console_scripts]
        cerebrate=cerebrate:cli
    ''',
)