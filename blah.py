has_error = True

while has_error:
        try:
            number = int(input("Enter a number: "))
            print(number)   

            has_error = False
        except:
            print("Invalid number. Please try again.")
            continue
        


