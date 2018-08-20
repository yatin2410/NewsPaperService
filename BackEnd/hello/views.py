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
import gmailcred
import firebasecred

EMAIL = gmailcred.EMAIL
PASS = gmailcred.PASS

FBLNK = firebasecred.FBLNK

#get users from firebase and seperate them
def getusers():
    req = Request(FBLNK)
    jsondata = str(urlopen(req).read())
    jsondata = jsondata.replace("b\'","")
    jsondata = jsondata.replace("\'","")
    pythondata = json.loads(jsondata)

    userdict = {
    "sandeshahm":"yatinpatel.gt454@gmail.com",
    "sandeshbar":"yatinpatel.gt454@gmail.com",
    "sandeshraj":"yatinpatel.gt454@gmail.com",
    "sandeshsur":"yatinpatel.gt454@gmail.com",

    "dbahm":"yatinpatel.gt454@gmail.com",
    "dbbar":"yatinpatel.gt454@gmail.com",
    "dbraj":"yatinpatel.gt454@gmail.com",
    "dbsur":"yatinpatel.gt454@gmail.com",

    "gsahm":"yatinpatel.gt454@gmail.com",
    "gsbar":"yatinpatel.gt454@gmail.com",
    "gsraj":"yatinpatel.gt454@gmail.com",
    "gssur":"yatinpatel.gt454@gmail.com",

    "dabsur":"yatinpatel.gt454@gmail.com",
    "dabdel":"yatinpatel.gt454@gmail.com",

    "tie":"yatinpatel.gt454@gmail.com",
    "toi":"yatinpatel.gt454@gmail.com",
    "fe":"yatinpatel.gt454@gmail.com",
    "tt":"yatinpatel.gt454@gmail.com",
    }

    for data in pythondata["news"]:
        print(pythondata["news"][data]["sub"])
        print(pythondata["news"][data]["email"])
        papers = pythondata["news"][data]["sub"].split()
        for paper in papers:
            print(paper)
            userdict[paper] = userdict[paper]+";"+pythondata["news"][data]["email"]
    print(userdict)
    return userdict


#start scrapping

def scrapesandesh(city,cat,code):
    req = Request('https://sandeshepaper.in/category/'+cat+'/'+city, headers={'User-Agent': 'Mozilla/5.0'})
    page_html = urlopen(req).read()
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll('section',{"class":" col-md-4 col-sm-6 epost epost-home cat text-center"})
    container = containers[0]
    lnk = container.a.get('href')
    lnk = lnk.replace('/edition/','')
    lnk = lnk.replace('/'+city,'')
    print(lnk)
    req = Request('http://sandeshepaper.in/download/'+str(lnk), headers={'User-Agent': 'Mozilla/5.0'})
    page_html = urlopen(req).read()
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll('p',{"class":"full-page"})
    container = containers[0]
    lnk = container.a.get('href')
    print(lnk)
    response = urlopen(lnk)
    fl = open('sandesh'+code+'.pdf','wb')
    fl.write(response.read())
    fl.close()

def sandeshahm(request):
    scrapesandesh('ahmedabad','21','ahm')
    return HttpResponse('<h1>Done<h1>')

def sandeshbar(request):
    scrapesandesh('baroda','38','bar')
    return HttpResponse('<h1>Done<h1>')

def sandeshraj(request):
    scrapesandesh('rajkot','27','raj')
    return HttpResponse('<h1>Done<h1>')

def sandeshsur(request):
    scrapesandesh('surat','22','sur')
    return HttpResponse('<h1>Done<h1>')



print('google drive')
#uploading in drive and sharing
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def sendnews(code):
    userdict = getusers()
    for fullname in userdict:
        if fullname.find(code) == -1:
            continue;
        print(fullname)
        file = drive.CreateFile({ 'title' : fullname+'.pdf'})
        file.SetContentFile(fullname+'.pdf')
        file.Upload()
        permission = {
            'type':'anyone',
            'value':'anyone',
            'role':'reader'
            }
        file.InsertPermission(permission)
        print(file['alternateLink'])
        link = file['alternateLink']
        toaddr = 'da2016g120@gmail.com'
        cc = ['']
        bcc = userdict[fullname].split(';')
        fromaddr = EMAIL
        message_subject = "Good Morning!! Here Is Your NewsPaper."
        message_text = "Your subscribed newspaper " + fullname + " is here: " + link
        message = "From: %s\r\n" % fromaddr + "To: %s\r\n" % toaddr + "CC: %s\r\n" % ",".join(cc) + "Subject: %s\r\n" % message_subject + "\r\n" + message_text
        toaddrs = [toaddr] + cc + bcc
        server = smtplib.SMTP_SSL('smtp.gmail.com:465')
        server.ehlo()
        #server.starttls()
        server.login(EMAIL,PASS)
        server.set_debuglevel(1)
        server.sendmail(fromaddr, toaddrs, message)
        server.quit()

def sendnewssandesh(request):
    sendnews('sandesh')
    return HttpResponse('<h1> send </h1>')

def index(request):
    return HttpResponse('<h1> Hello,World!! </h1>')