# -*- coding: utf-8 -*-
# CH03_01.py

# 建立節點物件
class student():
    def __init__(self):
        self.name = ''
        self.no = ''
        self.Eng = 0
        self.Math = 0
        self.next = None

head = student() # 首指標 無資料 只提供指標連結第一個有資料的節點
ptr = head
select = 0
Msum = Esum = student_no = 0

while select != 2:
    print('1.新增 2.離開')
    try:
        select = int(input('輸入一個選項:'))
    except ValueError:
        print('輸入錯誤')
        print('請重新輸入\n')
    if select == 1:
        new_data = student()
        new_data.name = input('姓名:')
        new_data.no = input('學號:')
        new_data.Eng = eval(input('英文成績:'))
        new_data.Math = eval(input('數學成績:'))
        ptr.next = new_data # 前一次迴圈做的節點的指標欄位指向這次迴圈做的新節點
        new_data.next = None # 最後一個節點指標為空
        ptr = ptr.next # ptr為最後節點，供下一次迴圈使用

ptr = head.next # 指向第一個有資料的節點
print('---------------------------------------------------------')
while ptr != None:
    print('姓名：%s\t學號：%s\t英文成績：%d\t數學成績：%d\t' %(ptr.name,ptr.no,ptr.Eng,ptr.Math))
    Msum = Msum + ptr.Math
    Esum = Esum + ptr.Eng
    student_no = student_no + 1
    ptr = ptr.next  # 將ptr移往下一元素

if student_no != 0:
    print('---------------------------------------------------------')
    print('本串列學生英文平均成績：%.2f\t數學平均成績：%.2f' %(Esum/student_no, Msum/student_no))