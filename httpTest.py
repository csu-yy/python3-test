#!/usr/bin/env python
#coding=utf8
import time,os,sched,urllib,httplib
import smtplib
import string

schedule = sched.scheduler(time.time, time.sleep)
def perform_command(self, inc):
    schedule.enter(inc, 0, perform_command, (self, inc))
    #os.system(cmd)
    monitoring(self)
def timming_exe(self, inc = 60):
    schedule.enter(inc, 0, perform_command, (self, inc))
    schedule.run()

def monitoring(self):
    print("开始监控...")
    httpClient = None
    try:
        params = urllib.urlencode({'name': 'tom', 'age': 22})
        headers = {"Content-type": "application/x-www-form-urlencoded"
                    , "Accept": "text/plain"}
 
        httpClient = httplib.HTTPConnection("2xx.x9.2x1.x", 8800, timeout=30)
        httpClient.request("POST", "/path/pathxxxxxxx", params, headers)
 
        response = httpClient.getresponse()
        print (response.status)
        print (response.reason)
        #print response.read()
        #print response.getheaders() #获取头信息
        
        if response.status == 200:
            print (u"正常")
        else:
            print (u"异常")
            sendmsg
            print('邮件已发送....')
    except Exception,e:
        print e          
    finally:
        if httpClient:
            httpClient.close()

def sendmsg():    
    FROM="xxx.com"
    TO="xxx.com"
    PASS="xxx"
    HOST="smtp.sina.com"
    PORT="25"
    SUBJECT="Interface alarm "
    TEXT="The alarm information !"
    BODY= string.join((
            "From: %s" % FROM,
            "To: %s" % TO,
            "Subject: %s" % SUBJECT,
            "",
            TEXT
    ), "\r\n")
    server=smtplib.SMTP()
    server.connect(HOST,"25")
    server.login(FROM,PASS)
    server.sendmail(FROM,TO,BODY)
    server.quit()
        
print("服务监控>>> 一分钟后开始执行(每10秒):")
timming_exe("echo %time%", 10)

