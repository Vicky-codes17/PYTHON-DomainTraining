### Changeing User Input to Removal of the  Symbols and Numbers to Show the String Only And Capitalize the first Letter

inpt_string = input("Enter the String : ")
# a = "$tiki123"
res = "".join(char for char in inpt_string if char.isalpha())
print(res.capitalize())
