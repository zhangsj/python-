#coding:utf-8
import xlsxwriter

workbook = xlsxwriter.Workbook('demo1.xlsx') #创建一个excel文件
worksheet = workbook.add_worksheet() #创建一个工作表对象

worksheet.set_column('A:A',20) #设定第一列宽度为20
bold=workbook.add_format({'bold':True}) #定义一个加粗的格式对象

worksheet.write('A1','Hello') #在A1单元格输入hello
worksheet.write('A2','World',bold) #A2单元格写入world并引用加粗的格式对象bold
worksheet.write('B2',u'中文测试',bold) #b2写入中文并引用bold

worksheet.write(2,0,32) #用行列表示法写入数字32与35.5
worksheet.write(3,0,35.5) #行列表示法的单元格下标以0作为起始值‘3，0’等价于A3
worksheet.write(4,0,'=SUM(A3:A4)') #求a3和a4的和并将结果写入‘4，0’及A5

worksheet.insert_image('B5','../sendmail/img/bytes_io.png') #在B5单元格插入图片
workbook.close() #关闭excel文件
