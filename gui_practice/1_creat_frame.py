from tkinter import *

root = Tk()
root.title("JSM gui")
root.geometry("640x480")
# root.geometry("640x480+1000+150") # 가로x세로+x좌표+y좌표
# root.resizable(False,False) # 창크기 변경불가


# # 버튼
# photo = PhotoImage(file="gui_practice/img.png")

# def btncomd():
#     print("클릭됨")

# btn1 = Button(root, padx=5, pady=10, text="버튼1") # 글자랑 버튼 사이 여백 # 글자 많아지면 커짐
# btn1.pack()

# btn2 = Button(root, width=10, height=5, fg="red", bg="yellow", text="버튼2") # width, height : 버튼자체의 크기 / 버튼 크기 고정 # fg : 글자색, bg : 버튼색
# btn2.pack()

# btn3 = Button(root, image=photo, command=btncomd) # image : 이미지 넣기 # command : 동작넣기
# btn3.pack()


# # 레이블
# photo = PhotoImage(file="gui_practice/img.png")

# def change():
#     global photo2 # 지역변수로 하면 중간에 삭제되버림
#     photo2 = PhotoImage(file="gui_practice/img2.png") 
#     label1.config(text ="또 만나요")
#     label2.config(image=photo2)

# btn = Button(root, text="바꾸기", command=change) 
# btn.pack()

# label1 = Label(root, text="안녕하세요")
# label1.pack()

# label2 = Label(root, image=photo)
# label2.pack()


# # 텍스트, 엔트리
# txt = Text(root, width=30, height=5) # 텍스트 위젯
# txt.pack()
# txt.insert(END, "글자를 입력하세요.") # 미리 글자 넣기

# e = Entry(root, width=30) # 엔트리 # 엔터 불가능
# e.pack()
# e.insert(0, "아이디를 넣으세요.") # 미리 글자 넣기

# def cmd ():
#     print(txt.get("1.0", END)) # 1번쨰 줄 0번쨰 인덱스부터 전부 가져와라
#     print(e.get()) # 엔트리에서 가져오기
#     txt.delete("1.0", END)
#     e.delete(0,END)

# btn = Button(root, text="가져오기", command=cmd) 
# btn.pack()


# # 리스트박스
# def cmd():
#     # listbox.delete(END) # 맨 뒤 항목 삭제
#     # listbox.delete(0) # 맨 앞 항목 삭제
#     print("리스트 갯수 : ", listbox.size()) 
#     print(" 1번쨰부터 3번째까지의 항목 : ", listbox.get(0, 2))
#     print("선택된 항목 : ", listbox.curselection()) # 위치로 반환 (1,2,3)

# btn = Button(root, text="버튼", command=cmd) 
# btn.pack()

# listbox = Listbox(root, selectmode = "extended", height = 0) # single : 하나만 선택가능 / extended : 여러개 선택 가능 # height = 0 : 리스트 전부 보기 / 1 : 1개만 보기...
# listbox.insert(0, "사과")
# listbox.insert(1, "딸기")
# listbox.insert(END, "바나나")
# listbox.insert(END, "수박")
# listbox.pack()


# 체크 박스
chkvar = IntVar() # int형으로 체크박스의 값 저장
chkvar2 = IntVar() # int형으로 체크박스의 값 저장

def cmd():
    print(chkvar.get()) # 0 : 체크 해제 / 1 : 체크
    print(chkvar2.get()) # 0 : 체크 해제 / 1 : 체크

chkbox = Checkbutton(root, text ="하루 동안 보지 않기", variable=chkvar)
chkbox.select() # 체크된 상태로 만들기
chkbox.deselect() # 체크 해제하기
chkbox.pack()

chkbox2 = Checkbutton(root, text ="일주일 동안 보지 않기", variable=chkvar2)
chkbox2.pack()


btn = Button(root, text="버튼", command=cmd) 
btn.pack()





root.mainloop() # 창 안꺼지게 유지


