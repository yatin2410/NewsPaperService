# NewsPaper Service

Main idea of this project is to scrape newspapers from various sites, combine pages into one pdf, upload pdfs on google drive and mail those pdfs to users according to their choice.

Please visit [here](https://epaper-service.azurewebsites.net/) for subscribe newspapers of your choice.

## Currently available epapers

* **Sandesh** - Ahmedabad, Surat, Rajkot, Baroda
* **DivyBhaskar** - Ahmedabad, Surat, Rajkot, Baroda
* **GujaratSamachar** - Ahmedabad, Surat, Rajkot, Baroda
* **DainikBhaskar** - Delhi, Surat
* **The Indian Express** - Delhi
* **Times of India** - Delhi
* **The Econimics Times** - Delhi
* **The Tribune** - Delhi

## Runnig Backend

These instructions will get you a copy of the project up and running backend on your local machine for development and testing purposes. 

### Prerequisites

* Gmail account for sending mail 
* GoogleDrive API key, look [here](https://developers.google.com/drive/api/v3/enable-sdk) for more info.
* firebase realtime database, look [here](https://console.firebase.google.com/) for more info.
* python3 

### Installing

A step by step series of examples that tell you how to get a development env running

first clone this repo by 
```
git clone https://github.com/yatin2410/NewsPaperService.git
```
```
cd NewsPaperService\BackEnd
```

put below things in following manner

```
create gmailcred.py file and put EMAIL = your gmail and PASS = your password 
```
```
create firebasecred.py and put your api key for firebase database.
```
```
put your credentials.json file and settings.yaml for GoogleDrive API key
```

Now install dependencies globaly or by creating environment from pipfile and then start the server by following command 

```
python manage.py collectstatic
```
and then 
```
python manage.py runserver 0.0.0.0:5000
```

Now goto [url](http://localhost:5000). Output should be 'Hello,World' on browser.

There are APIs for scraping and sending, for more info look into NewsPaperService\BackEnd\hello\views.py

## Authors List

* [Yatin Patel](https://github.com/yatin2410)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Thanks ❤
