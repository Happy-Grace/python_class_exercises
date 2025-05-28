# Python Program that welcomes the user

firstName = input("Please, enter your first name: \t")
middleName = input("Please, enter your middle name: \t")
lastName = input("Please, enter your last name: \t")

fullName = "%s %s %s" % (firstName, middleName, lastName)

print("Hello " + fullName + ", welcome to this new week!!")
