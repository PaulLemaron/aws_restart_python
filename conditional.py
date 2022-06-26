userReply=input("Do you want to ship a package? (Enter Yes or No)")
if userReply== "Yes": #if statement
    print("We can help you ship that package")
else: 
    print("please come back when you need to ship the package. Thank you") #Else statement
    
    #elif or else-if
userReply= input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope or copy)")
if userReply== "stamps":
    print("We have many stamps designs to choose from")
elif userReply== "envelope":
    print("We have many envelope sizes to choose from")
    sizes= input ("What size would you like? (Enter A4, A5, A3)")
    if sizes== "A3":
        print("Here is your {} size" .format(sizes)) #Nested if elif, else
    elif sizes== "A4":
        print("Here is your {} size ".format(sizes))
    else:
        print("Here is your {} size".format(sizes))
elif userReply== "copy":
    copies= input("How many copies would you like? (Enter a number)")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you. PLease come back again")

