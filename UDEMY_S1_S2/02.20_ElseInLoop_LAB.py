import urllib.request
import os

data_dir = r"C:\Users\El Patrico\Desktop\tempTXT"
pages = [
    {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
    {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}]

for page in pages:
    try:
        file_name = "{}.html".format(page['name'])
        print((file_name))
        path = os.path.join(data_dir, file_name)
        print(path)
        urllib.request.urlretrieve(page['url'], path)

    except:
        print('FAILURE processing web page: {}'.format(page["name"]))
        print('Stopping the process!')
        break

else:
    print('All pages downloaded successfully!!!')
