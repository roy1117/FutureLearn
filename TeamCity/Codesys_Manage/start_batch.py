def start_codesys():
    with open("start_codesys.bat", 'w') as fp:
            fp.write("start /b /wait CoDeSys.exe")

    start_codesys.bat


if __name__ == "__main__":
    start_codesys()
