from kaggle import KaggleApi

#Práctica 1 - Obtención de csv desde kaggle
def Práctica_1():
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_file('heesoo37/120-years-of-olympic-history-athletes-and-results','athlete_events.csv')

    from zipfile import ZipFile 
    zf = ZipFile('athlete_events.csv.zip')
    zf.extractall() 
    zf.close()  

Práctica_1()