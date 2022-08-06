import PyInstaller.__main__

PyInstaller.__main__.run(['3_pyopenxl_application.py', '--add-data=3_some_excel_data.xlsx;.', '--add-data=3_optional_json_file.json;.', '-y'])

