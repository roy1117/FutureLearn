from ftplib import FTP

ftp = FTP('')
ftp.connect('127.0.0.1', 2122)
ftp.login('edwards', 'p@$$word')
ftp.retrlines('LIST')
#
# filename = '../client_file.txt'  # replace with your file in the directory ('directory_name')
# localfile = open(filename, 'wb')
# ftp.retrbinary('RETR ' + 'server_file.txt', localfile.write, 1024)
# ftp.quit()
# localfile.close()