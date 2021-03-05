from tkinter import *

class calculator:
	def __init__(self, win):
		self.win = win
		self.win.title("계산기")
		self.win.geometry("320x245+200+100")
		self.win.resizable(True, True)	

		self.process = Entry(self.win, width = 40, justify = RIGHT)
		self.process.insert(0, '0')
		self.process.pack()

		self._input = Entry(win, width = 40, justify = RIGHT)
		self._input.insert(0,'0')
		self._input.pack()

		self.frm = Frame(self.win)
		self.frm.pack()
		self.cal_component = "789*456-123+C0./"

		# 계산기의 버튼을 만드는 반복문 grid 사용
		self.ind = 0
		for row in range(4):
			for col in range(4):
				btn = Button(self.frm, text = self.cal_component[self.ind], relief=GROOVE, width=10, height=2,\
					command = lambda char = self.cal_component[self.ind]:self.operater(char))
				btn.grid(row = row, column = col)
				self.ind+=1
		btn = Button(self.frm, text = '=', relief=GROOVE, width=10, height=2,\
			command = lambda char = '=' : self.operater(char))
		btn.grid(row = 4, column = 0)
		self.bf_num = 0
		self.operation = ''

	def operater(self, n):
		if n == "C":
			self.process.delete(0, END)
			self._input.delete(0, END)
			self.process.insert(0, 0)
			self._input.insert(0, 0)
			self.bf_num = 0
			self.operation = ''

		elif n in "+-*/":
			self.process.insert(END, n)
			self.operate()
			self.operation = n
			self.bf_num = eval(self._input.get())
			self._input.delete(0, END)

		elif n == '=':
			self.process.insert(END, n)
			self.operate()
			self.operation = ''
			self.process.insert(END, self.bf_num)
		
		elif self._input.get() == '0':
			self._input.delete(0, END)
			self._input.insert(END, n)
			self.process.delete(0, END)
			self.process.insert(END, n)

		else:
			self._input.insert(END, n)
			self.process.insert(END, n)

	def operate(self):
		if self.operation == '+':
			self.bf_num += eval(self._input.get())
			self.operation = ''
			self._input.delete(0, END)
			self._input.insert(0, self.bf_num)
		elif self.operation == '*':
			self.bf_num *= eval(self._input.get())
			self.operation = ''
			self._input.delete(0, END)
			self._input.insert(0, self.bf_num)
		elif self.operation == '-':
			self.bf_num -= eval(self._input.get())
			self.operation = ''
			self._input.delete(0, END)
			self._input.insert(0, self.bf_num)
		elif self.operation == '/':
			if self._input.get() == '0':
				self._input.delete(0, END)
				self._input.insert(0, "0으로 나눌 수 없습니다")
			self.bf_num /= eval(self._input.get())
			self.operation = ''
			self._input.delete(0, END)
			self._input.insert(0, self.bf_num)

if __name__ == "__main__":
	window = Tk()
	mycal = calculator(window)
	window.mainloop()