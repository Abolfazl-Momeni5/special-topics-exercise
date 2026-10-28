history=[]
result=0
memory=0
print("welcome the advanced calculator :)")
print("---------------------------------------------")
print("insert=>'+' to sum of the number\ninsert=>'-' to minus the number\ninsert=>'*' to multiply the number\n insert=>'/' to dividing the number\ninsert=>'**' to power the number\ninsert=>'h' to show the history\ninsert=>'b' to binarize the last number\ninsert=>'o' to octalize the last number\ninsert=>'x' to hexadecimal the last number\ninsert=>'m' to reuse the number stored in memory\n insert=>'m+' To add a number to a value stored in memory \n insert=>'m-' To subtract a number from the value stored in memory\ninsert=>'e' to exite the app ")
while(True):
    
    print("---------------------------------------------")
    operator=input("Enter The Math Operator:")
    print("---------------------------------------------")

    match operator:
        case "e":
            print("Good Bye")
            break
        case "h":
            if history:
                print("Calculation History:")
                for item in history:
                    print(item)
            else:
                print("History is empty!")
        case "m+":
            memory+=result
            print(f"memory:{memory}")
        case "m-":
            memory-=result
            print(f"memory:{memory}")
        case "m":
            print(f"memory:{memory}")

        case "b":
            print("Binary:", bin(int(result)))
        case "o":
            print("Octal:", oct(int(result)))
        case "x":
            print("Hexadecimal:", hex(int(result)))

        case "+"|"-"|"*"|"**"|"/":
            first_number=float(input("Enter The Number One:"))
            print("---------------------------------------------")
            secondery_number=float(input("Enter The Number Two:"))
            print("---------------------------------------------")
            match operator:
                case "+":
                    result=first_number+secondery_number
                case "-":
                    result=first_number-secondery_number
                case "*":
                    result=first_number*secondery_number
                case "**":
                    result=first_number**secondery_number
                case "/":
                    result=first_number/secondery_number
            print(f"result: {result}")
            history.append(f"{first_number}{operator}{secondery_number}={result}")
        case _:
            print("invalid input!")
            break
