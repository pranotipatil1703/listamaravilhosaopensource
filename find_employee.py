class Solution():
	def __init__(self):
		pass

	def assignAndPrint(self,t):
		#We will directly permute over t. Access 2nd element(i.e. manager) of certain tuple and assign the relation in
		# dictionary. We will assign list of employees to a particular manager so that with iterations, we can append
		# more employees to that list and list grows.
		d = dict()
		for pair in t:
			if(pair[0]==pair[1]): # because we dont want to assign self managing role
				continue
			if pair[0] not in d: # assign employee a empty list of employees
				d[pair[0]] = []
			# for managers -
			if pair[1] not in d:
				d[pair[1]] = [pair[0]]
			else:
				d[pair[1]].append(pair[0])
		#print(d)
		# now we know how many employees are directly under a particular manager.
		# now lets count the total number of employees under a particular manager.
		c = dict() # store manager:count of employee as key value
		for manager in d:
			c[manager] = len(d[manager])
			for employee in d[manager]:
				c[manager] += len(d[employee])
			print("{} : {}".format(manager,c[manager]))	 # prints which manager has total how many employees
		# Note : Employees having no employees under are also considered as managed with 0 employees.


if __name__=="__main__":
	# t is tuple containing employee and boss pair.
	t = (("A", "C"),("B", "C"),("C", "F"),("D", "E"),("E", "F"),("F", "F"))
	obj = Solution()
	obj.assignAndPrint(t)
