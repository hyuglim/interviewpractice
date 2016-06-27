def comb_parens(num_parens):
	if num_parens == 1:
		return "()"
	return "()" + comb_parens(num_parens - 1) + ",(" + comb_parens(num_parens - 1) + ")," + comb_parens(num_parens - 1) + "()"

print comb_parens(3)


#()
#()(),(())
#()()(),(()()),()(()),(())(),((()))
