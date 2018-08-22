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
#		print(pythondata["news"][data]["sub"])
#		print(pythondata["news"][data]["email"])
		papers = pythondata["news"][data]["sub"].split()
		for paper in papers:
#			print(paper)
			userdict[paper] = userdict[paper]+";"+pythondata["news"][data]["email"]
#	print(userdict)
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


def scrapedb(city,code):
    main_url = "http://digitalimages.bhaskar.com/gujarat/epaperpdf/"
    if time.localtime(time.time()).tm_mon<10 :
        month = '0'+str(time.localtime(time.time()).tm_mon)
    else :
        month = time.localtime(time.time()).tm_mon;
    if time.localtime(time.time()).tm_mday<10 :
        date = '0'+str(time.localtime(time.time()).tm_mday)
    else :
        date = time.localtime(time.time()).tm_mday;
    pdfs = []
    id = str(date)+str(month)+'2018'+'/'+str(date-1)+city+'%20CITY-PG'
    merger = PdfFileMerger()
    for i in range(1, 35):
        try:
            back_url = str(id)+str(i)+str('-0')+'.PDF'
            print(main_url+back_url)
            respose =  urlopen(main_url+str(back_url))
            pagename = 'temp'+str(i)+'.pdf'
            fl = open(pagename, 'wb')
            fl.write(respose.read())
            fl.close()
            pdfs.append(pagename)
        except:
            print(pdfs)
            for pdf in pdfs:
                print(pdf)
                merger.append(pdf)
            merger.write("db"+code+".pdf")
            break

def dbahm(request):
    scrapedb('AHMEDABAD','ahm')
    return HttpResponse('<h1>Done<h1>')

def dbbar(request):
    scrapedb('BARODA','bar')
    return HttpResponse('<h1>Done<h1>')

def dbraj(request):
    scrapedb('RAJKOT','raj')
    return HttpResponse('<h1>Done<h1>')

def dbsur(request):
    scrapedb('SURAT','sur')
    return HttpResponse('<h1>Done<h1>')

def scrapegs(code):
    name = code.upper()
    main_url = "http://gujaratsamacharepaper.com/download.php?file=http://enewspapr.com/News/GUJARAT/"+name+"/"
    if time.localtime(time.time()).tm_mon<10 :
        month = '0'+str(time.localtime(time.time()).tm_mon)
    else :
        month = time.localtime(time.time()).tm_mon;
    if time.localtime(time.time()).tm_mday<10 :
        date = '0'+str(time.localtime(time.time()).tm_mday)
    else :
        date = time.localtime(time.time()).tm_mday;
    pdfs = []
    id = '2018'+str(month)+str(date)+'_'
    merger = PdfFileMerger()
    for i in range(1, 35):
        back_url = '2018' + '/'+str(month)+'/'+str(date)+'/'+str(id)+str(i)+'.PDF'
        print(main_url+back_url)
        respose = urlopen(main_url+str(back_url))
        pagename = 'temp'+str(i)+'.pdf'
        pdfs.append(pagename)
        fl = open(pagename, 'wb')
        fl.write(respose.read())
        fl.close()
        if os.stat('temp'+str(i)+'.pdf').st_size > 0:
            merger.append('temp'+str(i)+'.pdf')
    merger.write("gs"+code+".pdf")

def gsahm(request):
    scrapegs("ahm")
    return HttpResponse('<h1>Done<h1>')

def gsbar(request):
    scrapegs("bar")
    return HttpResponse('<h1>Done<h1>')

def gsraj(request):
    scrapegs("raj")
    return HttpResponse('<h1>Done<h1>')

def gssur(request):
    scrapegs("sur")
    return HttpResponse('<h1>Done<h1>')


def scrapedab(main_url,idd,code):
    if time.localtime(time.time()).tm_mon<10 :
        month = '0'+str(time.localtime(time.time()).tm_mon)
    else :
        month = time.localtime(time.time()).tm_mon;
    if time.localtime(time.time()).tm_mday<10 :
        date = '0'+str(time.localtime(time.time()).tm_mday)
    else :
        date = time.localtime(time.time()).tm_mday;
    pdfs = []
    id = str(date)+str(month)+'2018'+'/'+str(date-1)+idd
    merger = PdfFileMerger()
    for i in range(1, 35):
        try:
            back_url = str(id)+str(i)+str('-0')+'.PDF'
            print(main_url+back_url)
            respose = urlopen(main_url+str(back_url))
            pagename = 'temp'+str(i)+'.pdf'
            pdfs.append(pagename)
            fl = open(pagename, 'wb')
            fl.write(respose.read())
            fl.close()
        except:
            for pdf in pdfs:
                merger.append(pdf)
            merger.write("dab"+code+".pdf")
            break

def dabsur(request):
    scrapedab("http://digitalimages.bhaskar.com/mpcg/epaperpdf/",'SURAT%20CITY%20HINDI-PG','sur')
    return HttpResponse('<h1>Done<h1>')

def dabdel(request):
    scrapedab("http://digitalimages.bhaskar.com/cph/epaperpdf/",'DELHI%20CITY-PG','del')
    return HttpResponse('<h1>Done<h1>')



def scrapeother(main_url,code):
	req = Request(main_url,headers={'User-Agent': 'Mozilla/5.0'})
	page_html = urlopen(req).read()
	page_soup = soup(page_html,'html.parser')
	containersbtn = page_soup.find('button',{'class':'button_next'})
	lnk = containersbtn.parent.get('href')
	print(lnk)
	req = Request(lnk,headers={'User-Agent': 'Mozilla/5.0'})
	page_html = urlopen(req).read()
	page_soup = soup(page_html,'html.parser')
	container = page_soup.find('div',{'class':'bars'})
	dlnk = container.a.get('href')
	response = urlopen(dlnk)
	fl = open(code+'.pdf','wb')
	fl.write(response.read())
	fl.close()

def othertie(request):
	scrapeother('http://www.sscias.com/p/indian-express-epaper.html','tie')
	return HttpResponse('<h1>Done<h1>')

def otherfe(request):
	scrapeother('http://www.sscias.com/p/economic-times-epaper.html','fe')
	return HttpResponse('<h1>Done<h1>')

def othertoi(request):
	scrapeother('http://www.sscias.com/p/times-of-india-epaper.html','toi')
	return HttpResponse('<h1>Done<h1>')

def othertt(request):
	scrapeother('http://www.sscias.com/p/the-tribune-epaper.html','tt')
	return HttpResponse('<h1>Done<h1>')

print('google drive')
#uploading in drive and sharing
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def sendnews(code):
	print('insendnews')
	userdict = getusers()
	for fullname in userdict:
		#print(fullname)
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

def sendnewsdb(request):
    sendnews('db')
    return HttpResponse('<h1> send </h1>')


def sendnewsgs(request):
    sendnews('gs')
    return HttpResponse('<h1> send </h1>')

def sendnewsdab(request):
    sendnews('dab')
    return HttpResponse('<h1> send </h1>')

def sendnewsother(request):
	sendnews('tie')
	sendnews('toi')
	sendnews('fe')
	sendnews('tt')
	return HttpResponse('<h1> send </h1>')

def index(request):
	return HttpResponse('<h1> Hello,World!! </h1>')