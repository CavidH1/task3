my_dict = {"language": [ "Azerbaijan", "French", "German" ] }
a = input("melumati daxil edin: ")
if a in my_dict["language"]:
    print("bu melumat hal-hazirda movcuddur")
my_dict["language"]. append(a)
print(my_dict)