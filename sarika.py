
def sa(n1):
	if n1:
		return (n1+2)+sa(n1-1)
    else:
        return 3

def ea(n2):
	if n2:
		return sa(n2)+ea(n2-1)
	else:
		return 0
print(ea(5))