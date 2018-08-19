from django.shortcuts import render
from django.http import HttpResponse
from .models import Greeting

import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import schedule
from firebase import firebase
import json
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import smtplib
import time
from PyPDF2 import PdfFileMerger


print('google drive')
#uploading in drive and sharing

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file = drive.CreateFile({ 'title' : 'text.txt'})
file.SetContentFile('text.txt')
file.Upload()
permission = {
    'type':'anyone',
    'value':'anyone',
    'role':'reader'
    }
file.InsertPermission(permission)
print(file['alternateLink'])

def index(request):
    return HttpResponse('<h1> Hello,World!! </h1>')

