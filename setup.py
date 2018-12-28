from setuptools import setup

APP = ['gui.py']
DATA_FILES = ['configuration.json']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
        'CFBundleDisplayName': 'HuaweiMeter',
        'CFBundleName': 'HuaweiMeter',
    },
    'iconfile': 'icon.icns',
    'packages': ['rumps', 'requests'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
