# Raihan Khalil Abdillah, 30065695
# AT2.2 Question 1
# String Manipulation

print("Acquaintance, Address, Definitely")

str_input = input("Input : ")
print("Word inputted: ", str_input)

new_text1 = str_input.replace("acquaintence", "acquaintance")
new_text2 = new_text1.replace("adress", "address")
new_text3 = new_text2.replace("defiantly", "definitely")

print("The correct spelling is ", new_text3)
