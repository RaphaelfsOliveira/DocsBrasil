
def cpf_valid(cpf):

	cpf = cpf.replace('.', '').replace('-', '')
	if len(cpf) != 11 or len(set(cpf)) == 1:
		return False

	for NUM in range(9, 11):
				
		c = [int(n) for n in cpf[:NUM]]
		n = list(range(NUM+1, 1, -1))
		s = sum(map(lambda i: c[i]*n[i], range(NUM)))

		dv = 0
		if (s%11) >= 2: dv = 11 - (s%11)

		if not int(cpf[NUM]) == dv:
			return False

	return True
	