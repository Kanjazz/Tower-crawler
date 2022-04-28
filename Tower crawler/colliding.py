p1 = (0,0)
s1= (0,0)
p2 = (0,0)
s2 = (0,0)
def col(self, p1,s1,p2,s2):
	if (p1[0] < p2[0] + s2[0] and p1[0] + s1[0] > p2[0] and p1[1] < p2[1] + s2[1] and p1[1] + s1[1] > p2[1]):
		
		return True
	else:
		return False