def calculate_averages():
    pos_sum, pos_count = 0, 0
    neg_sum, neg_count = 0, 0
    
    print("Enter numbers to find averages. Enter -1 to exit.")

    while True:
        num = float(input("Enter the number: "))

        if num == -1:
            break
        elif num > 0:
            pos_sum += num
            pos_count += 1
        elif num < 0:
            neg_sum += num
            neg_count += 1

    if pos_count > 0:
        print("The average of positive numbers is:", pos_sum / pos_count)
    else:
        print("No positive numbers entered.")
    
    if neg_count > 0:
        print("The average of negative numbers is:", neg_sum / neg_count)
    else:
        print("No negative numbers entered.")


calculate_averages()
