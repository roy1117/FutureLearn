import PyInstaller.__main__

PyInstaller.__main__.run([
    '1_simple_print_script.py 2> build.txt',
    '-y',
    '--console',
    '--log-level=DEBUG',
])