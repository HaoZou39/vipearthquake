	def add(x,y):
		x = driver.find_element_by_name("box1")
		y = driver.find_element_by_name("box2")
		ctypes.windll.user32.MessageBoxA(0, "x+y = "+x+y, "Answer", 1)
	def mul(x,y):
		x = driver.find_element_by_name("box1")
		y = driver.find_element_by_name("box2")
		ctypes.windll.user32.MessageBoxA(0, "x*y = "+x*y, "Answer", 1)	
	def sub(x,y):
		x = driver.find_element_by_name("box1")
		y = driver.find_element_by_name("box2")
		ctypes.windll.user32.MessageBoxA(0, "x-y = "+x-y, "Answer", 1)