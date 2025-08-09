# Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.
def total_calc(amount,tip_percentage):
    tip=amount*tip_percentage*0.01
    total=amount+tip
    return total
amount=int(input("Enter the pay:"))
tip=int(input("Enter the tip:"))
print(total_calc(amount,tip))