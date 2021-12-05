Python 3.9.5 (default, May 11 2021, 08:20:37) 
[GCC 10.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Pen()

#controls
def t.forward(var):
	t.forward(var)
def b(var):
	t.backward(var)
def t.left(var):
	t.left(var)
def r(var):
	t.right(var)

#shapes
def square(length):
	x = 0
	while x < 4:
		t.forward(length)
		t.left(90)
		x+=1
		
		
def grid(size, row, column):
	while column != 0:
		while row != 0:
			t.forward(size)
			t.left(90)
			t.forward(size)
			t.left(90)
			t.forward(size)
			t.left(90)
			t.forward(size)
			t.left(90)
			t.forward(size)
			row-=1
		t.left(180)
		t.forward(size*row)
		t.left(90)
		t.forward(size)
		t.left(90)
		column -= 1
		
#these 3 work for some reason idk why		
def square(size):
	t.forward(size)
	t.left(90)
	t.forward(size)
	t.left(90)
	t.forward(size)
	t.left(90)
	t.forward(size)
	t.left(90)
	t.forward(size)
	
def column(amt,size):
	while amt != 0:
		square(size)
		amt -= 1
	t.backward(size*amt)
	
def row(row,col,size):
	while row != 0:
		column(col,size)
		t.up()
		t.backward(col*size)
		t.right(90)
		t.forward(size)
		t.left(90)
		t.down()
		row -= 1
		
#THIS WORKS POGGERS!!!!!!!!!!!!!!!!!!!!!!!!
def grid(row,col,size):
	def column(amt,size):
		def square(size):
			t.forward(size)
			t.left(90)
			t.forward(size)
			t.left(90)
			t.forward(size)
			t.left(90)
			t.forward(size)
			t.left(90)
			t.forward(size)
		while amt != 0:
			square(size)
			amt -= 1
		t.backward(size*amt)
	while row != 0:
		column(col,size)
		t.up()
		t.backward(col*size)
		t.right(90)
		t.forward(size)
		t.left(90)
		t.down()
		row -= 1

		
#not working idk why, do some debugging		
def grid(row,col,size):
	while row != 0:
		while col != 0:
			t.forward(size)
			t.left(90)
			t.forward(size)
			t.left(90)
			t.forward(size)
			t.left(90)
			t.forward(size)
			t.left(90)
			t.forward(size)
			col -= 1
		t.backward(size*col)
		t.up()
		t.backward(col*size)
		t.right(90)
		t.forward(size)
		t.left(90)
		t.down()
		row -= 1
		
def triangle(size):
	t.forward(size)
	t.left(120)
	t.forward(size)
	t.left(120)
	t.forward(size)
	t.left(120)
