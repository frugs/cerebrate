from distutils.core import setup


setup(
    name='cerebrate',
    version='0.0.1',
    description='Offline Replay Manager for StarCraft II',
    author='Hugo Wainwright',
    author_email='wainwrighthugo@gmail.com',
    url='https://github.com/frugs/cerebrate',
    download_url='https://github.com/frugs/cerebrate/tarball/0.0.1',
    packages=['replaymanager', 'replaysearch'],
    py_modules=['cerebrate'],
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
