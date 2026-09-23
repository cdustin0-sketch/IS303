numbers = [1, 0, 3, -4, 5]
current_number = 0
num_negatives = 0
number_zero = 0
num_positives = 0

#for each number, print whether it is positive, negative, or zero
#keep counts of each category and display totals at the end


#print the numbers if they are each positive, negative, or zero

for i in range(0, 5):
    current_number = numbers[i]
    if current_number <0:
        num_negatives += 1
        print("Negative")
    elif current_number == 0:
        number_zero += 1
        print("Zero")
    elif current_number >= 0:
        num_positives += 1
        print("Positive")   



print("Total Positive numbers " + str(num_positives ))
print("Total Zero numbers " + str(number_zero ))
print("Total Negative numbers " + str(num_negatives ))
