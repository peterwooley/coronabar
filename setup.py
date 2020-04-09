from setuptools import setup

APP = ['app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'plist': {
        'CFBundleShortVersionString': '0.2.1',
        'LSUIElement': True,
    },
    'packages': ['rumps', 'requests', 'humanize'],
}

setup(
    app=APP,
    name='CoronaBar',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps', 'requests', 'humanize']
)

