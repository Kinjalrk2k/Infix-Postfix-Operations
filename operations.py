def isopt(c):
        """Function that checks wheter the passed character is an operator."""
        if c == "+" or c == "-" or c == "*" or c == "/":
                return True
        else:
                return False

def precedence(a, b):
        """Checks precedence of the passed arguments and returns one on the following:
        negative integer: if a is at a higher precedence
        positive integer: if b is in a higher precedence
        zero: if both a and b are in same precedence"""
        if a == "(" or a == ")":
                p_a = 1
        elif a == "*" or a == "/":
                p_a = 2
        elif a == "^":
                p_a = 3
        elif a == "+" or a == "-":
                p_a = 4

        if b == "(" or b == ")":
                p_b = 1
        elif b == "*" or b == "/":
                p_b = 2
        elif b == "^":
                p_b = 3
        elif b == "+" or b == "-":
                p_b = 4

        return p_a - p_b

exp_in = []
# exp_in = ["(", 1, "+", 2, ")", "*", 3, "/", 4]
stack = ["("]
exp_post = []
raw_exp = []

"""Enter each element of the expression seperately by pressing RETURN
Press RETURN twice to exit the inputting phase"""
print("Enter an expression: ")
while True:
        x = input()
        """Taking the raw input and segregating operands"""
        if x.isdigit():
                exp_in.append(int(x))
        elif x == '':
                break
        else:
                exp_in.append(x)

print("Expression Entered:", exp_in)


"""Conversion from infix to postfix starts here"""
exp_in.append(")")

e = 0
while stack != []:
        if(exp_in[e] == "("):
                stack.append("(")
        
        elif(isopt(exp_in[e])):
                while(precedence(stack[len(stack)-1], exp_in[e]) >= 0):
                        exp_post.append(stack.pop())
                stack.append(exp_in[e])
        
        elif(exp_in[e] == ")"):
                while(stack[len(stack)-1] != "("):
                        exp_post.append(stack.pop())
                stack.pop()
        
        else:
                exp_post.append(exp_in[e])
        
        e+=1

print(exp_post)
