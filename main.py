# Gradez by cscheerer on GitHub
# NOTE: There are these subjects. Because of my horrible skills, the amount of subjects cannot be changed easily. Sorry!
# Oh, and if you can make a version that can control the amount of subjects, please let me know!
import time

print("Welcome!")
print("There is no Pd. 9 due to it being for a double period.")
print("You cannot have decimals.")
print("You can have a space only before the number.")
print("")

s1 = input("Grade for Pd. 1:")
s2 = input("Grade for Pd. 2:")
s3 = input("Grade for Pd. 3:")
s4 = input("Grade for Pd. 4:")
s5 = input("Grade for Pd. 5:")
s6 = input("Grade for Pd. 6:")
s7 = input("Grade for Pd. 7:")
s8 = input("Grade for Pd. 8:")


s1 = int(s1)
s2 = int(s2)
s3 = int(s3)
s4 = int(s4)
s5 = int(s5)
s6 = int(s6)
s7 = int(s7)
s8 = int(s8)


print("Loading...")
print("")
time.sleep(2)

total = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8
total = int(total)
avarage = total / 8

print(f"Your avarage is: {avarage}%.")
