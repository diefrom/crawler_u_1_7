#!/usr/bin/env python
# coding=utf-8
#python2
#2014/09/07 by diefrom
import urllib
from urllib2 import Request, urlopen, URLError, HTTPError
import base64
import re
import os
import sys

'''make the number of name'''
def mkNumber(i):
    number = i /10
    if number == 0:
        i = '000' + str(i)
    elif number < 10:
        i = '00' + str(i)
    else:
        i = '0' + str(i)
    return i

'''make the directory named u17, that uses save the directores of chapter'''
def mkDir():
    existDir = os.path.exists('u17')
    if existDir == True:
        print('\033[31mexisting the directory named u17, please change the name of it\033[0m')
        sys.exit(1)
    else:
        os.mkdir('u17')
        os.chdir('u17')

'''find images and download'''
def findImg(url):
    try:
        '''get the infomations from html'''
        htmlUrl = urlopen(url)
        htmlSource = htmlUrl.read()
        imgListOriginal = re.findall('image\_list.*?\)\,', htmlSource, re.S)
        imgTemp = ''.join(imgListOriginal)
        imgList= re.findall('src\"\:\".*?\"', imgTemp)
        
        '''decode the http using base64'''
        for i in range(0, len(imgList)):
            imgLen = len(imgList[i]) - 1
            imgList[i] = ''.join(imgList[i][6:imgLen])
            imgList[i] = base64.decodestring(imgList[i])

            '''save the images and display the schedule'''
            imgName = mkNumber(i) + '.jpg'
            imgSave = urllib.urlretrieve(imgList[i], imgName)
            if imgSave:
                print('\033[36msave:%s\033[0m' %imgList[i]) 
            else:
                print('\033[31msave imgaes failed!\033[0m')
                sys.exit(1)

    except URLError,e:
        if hasattr(e, 'code'):
            print('\033[31mThe server couldn\'t fulfill the request.\033[0m')
            print('Error code:', e.code)
        elif hasattr(e, 'reason'):
            print('\033[31mWe failed to reach a server\033[0m')
            print('Reason', e.reason)

def findChapter(url, start, end):
    try:
        '''get the infomations from html'''
        htmlUrl = urlopen(url)
        htmlSource = htmlUrl.read()
        chapterListOriginal = re.findall('id=\"chapter.*?\/ul', htmlSource, re.S)
        chapterTemp = ''.join(chapterListOriginal)
        chapterList = re.findall('href=\".*?\"', chapterTemp, re.S)
        chapterTemp = ''.join(chapterListOriginal)
        titleList = re.findall('title=\".*?\"',chapterTemp, re.S)
        chapterNum= len(chapterList)
        if end > chapterNum:
            end = chapterNum

        '''make the directory named u17'''
        mkDir()

        '''get every http of chapter, than make directores and save the images'''
        for i in range(0, chapterNum):
            chapterLen = len(chapterList[i]) - 1
            titleLen = len(titleList[i]) - 1
            chapterList[i] = ''.join(chapterList[i][6:chapterLen])
            chapterList[i] = chapterList[i] + '?t=old'
            titleList[i] = ''.join(titleList[i][7:titleLen])
            
        for j in range(start, end):
            chapterName = 'Chapter' + mkNumber(j) + ':' + titleList[j]
            os.mkdir(chapterName)
            os.chdir(chapterName)
            findImg(chapterList[j])
            print('\033[32m%s done!\033[0m') %chapterName
            os.chdir('../')            

    except URLError,e:
        if hasattr(e, 'code'):
            print('\033[31mThe server couldn\'t fulfill the request.\033[0m')
            print('Error code:',e.code)
        elif hasattr(e, 'reason'):
            print('\033[31mWe failed to reach a server\033[0m')
            print('Reason', e.reason)

'''main->select 1 to findChapter, select 2 to findImg'''
inputUrl = raw_input('please input Web\'s URL: ')
print('select 1 to download the whole directory.')
print('select 2 to download the part of chapter.')
select = raw_input('please input your selection: ')
if select == '1':
    findChapter(inputUrl, 0, 500)
elif select == '2':
    start = raw_input('please input the start of chapter: ')
    end = raw_input('please input the end of charpter: ')
    findChapter(inputUrl, int(start), int(end))
else:
    print('input error! The program exits.')

