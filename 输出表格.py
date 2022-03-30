import xlwt
import openpyxl as op
list1 = []
list1.append(i)#i就是存储持续读取到的数据的变量，根据你的需求来定就可以
wb = op.load_workbook("data2.xlsx")#打开已有的excel表格，我这里是新版的excel，后缀名是xlsx.老版本的好像不支持
sh = wb['Sheet1'] #找到要写入的工作页
for k in range(1, len(list1)):#循环让最后一个数据写入到最后一行
    sh.cell(k+1, 1, list1[k-1])#行数 列数 要写入的数据
wb.save("data2.xlsx")