#1
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))
# c = int(input("Enter c:"))

# def quadratic_equation(a, b, c):
# 	d=( (b * b-4 * a * c) ) ** 0.5
# 	r = ( (-b) + d) // (2 * a)
# 	return r
#
# quadratic_equation(a, b, c)

#4
# def box_seq(step):
#     if step == 0:
#         return 0
#     elif step % 2 == 0:
#         return step
#     else:
#         return step+2

#5
o = input("Enter first num:")
d = input("Enter second num:")
i = input("Enter third num:")

n = o[1]
a = d[1]
y = i[2]
print(n, a)
for x in a:
 if n * a == y:
     print(True)
 else:
     print(False)

#8
a = int(input("Enter : "))

def is_repdigit(num):
    for ele in str(num):
        if ele != str(num)[0]:
            return False
            break
        else:
            continue
    return True

