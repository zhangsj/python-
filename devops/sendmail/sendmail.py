#!/usr/bin/env python
#coding:utf-8

import smtplib
import string

HOST="smtp.126.com"
SUBJECT="Test email from Python"
TO="j@126.com"
FROM="j@126.com"
text="Python rules them all!"
BODY=string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
    ),"\r\n")
server = smtplib.SMTP()
server.connect(HOST,"25")
#server.starttls()
server.login("j@126.com","m")
server.sendmail(FROM,[TO],BODY)
server.quit()

