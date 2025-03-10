# 간단 계산기
#1. 계산기는 Entry()와 Button()으로 5*5 grid 배치로 인터페이스 구성
#2. 0행에 Entry()를 통해 계산값 입력과 결과 출력
#3. 1행 0열부터 '7', '8', '9', '+', 'C',
#   2행 0열부터 '4', '5', '6', '-', ' ',
#   3행 0열부터 '1', '2', '3', '*', ' ',
#   4행 0열부터 '0', '.', '=', '/', '%' 로 Button() 구성
#4. 숫자 버튼과 연산자 버튼이 눌러지면 엔트리 표시
#5. = 버튼이 눌러지면 계산 결과 출력
#6. C 버튼이 눌러지면 엔트리 내용을 모두 지움

from tkinter import *

window = Tk()
window.title("간단 계산기")
display = Entry(window, width = 33, bg = "yellow")
display.grid(row = 0, column = 0, columnspan = 5)

but = ['7', '8', '9', '+', 'C',
       '4', '5', '6', '-', ' ',
       '1', '2', '3', '*', ' ',
       '0', '.', '=', '/', '%']

def click(key):
    if key == "=":
        result = eval(display.get())
        s = str(result)
        display.delete(0, 'end')
        display.insert(0, s)
    else:
        if key == 'C':
            display.delete(0, 'end')
            key = ''

        display.insert(END, key)
        

row_index = 1
col_index = 0

for but_text in but:
    def process(t = but_text):
        click(t)

    Button(window, text = but_text, width = 5, command = process).grid(row = row_index, column = col_index)
    col_index += 1

    if col_index > 4:
        row_index += 1
        col_index = 0

window.mainloop()
    
