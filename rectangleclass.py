class shape_rectangle():
def __init__(self,my_length, my_breadth):
	self.length = my_length
	self.breadth = my_breadth
def calculate_area(self):
	return self.length*self.breadth
len_val = 6
bread_val = 45
print("The length of the rectangle is : ")
print(len_val)
print("The breadth of the rectangle is : ")
print(bread_val)
my_instance = shape_rectangle(len_val,bread_val)
print("The area of the rectangle : ")
print(my_instance.calculate_area())
print()
