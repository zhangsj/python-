#coding:utf-8
import smtplib
from email.mime.text import MIMEText

HOST="smtp.126.com"
SUBJECT=u"测试邮件"
FROM="6.com"
TO="j@126.com"
msg=MIMEText("""
    <table width="800" border="0" cellspacing="0" cellpadding="4">
      <tr>
        <td bgcolor="#CECFAD" height="20" style="font-size:14px">*测试数据 <a href="www.baidu.com">更多>></a></td>
      </tr>
      <tr>
        <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
         1)日访问量:<font color=red>123123</font> 访问次数：23651 页面浏览量：45123 点击数：545122 数据流量：500Mb<br>
         2)状态码信息<br>
         &nbsp;&nbsp;500:105  404:3254 503:212<br>
         3)访客浏览器信息<br>
         &nbsp;&nbsp;/index.php 123123<br>
         &nbsp;&nbsp;/index.php 123123<br>
         &nbsp;&nbsp;/index.php 123123<br>
         &nbsp;&nbsp;/index.php 123123<br>
         </td>
        </tr>
      </table>""","html","utf-8")

msg['Subject']=SUBJECT
msg['From']=FROM
msg['To']=TO
try:
    server = smtplib.SMTP()
    server.connect(HOST,"25")
    server.starttls() 
    server.login("j@126.com","m")
    server.sendmail(FROM,TO,msg.as_string())
    server.quit()
    print "邮件发送成功"
except Exception,e:
    print "失败"+str(e)
