a = 5.8
b = 3
c = 4
result = a + b * (c ** 2)
# a + 3 * 16
# a + 48
print("5 + 3 * (4 ** 2) ===> ", result)
# No float points will be added based on the value. except for // division
a = 50
result = a / b * (c ** 2)
# 50 / 3 * 16
# 16.666666667 * 16
# 266.66666667
print("50 / 3 * (4 ** 2) ===> ", result)

result = a // b * (c ** 2)
# 50 // 3 * 16
# 16 + 16
# 256
print("5 // 3 * (4 ** 2) ===> " , result)

'''
Precedence	Operator	Description
1 (highest)	()	Parentheses (grouping)
2	**	Exponentiation (right to left)
3	+x, -x, ~x	Unary plus, Unary minus, Bitwise NOT
4	*, /, //, %	Multiplication, Division, Floor Division, Modulus
5	+, -	Addition, Subtraction
6	<<, >>	Bitwise shift operators
7	&	Bitwise AND
8	^	Bitwise XOR
9	`	`
10	==, !=, >, >=, <, <=	Comparison Operators
11	not	Logical NOT
12	and	Logical AND
13 (lowest)	or	Logical OR


'''
