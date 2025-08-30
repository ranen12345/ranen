underweight = 0
overweight = 0
bags = int(input("how many bags do you have "))
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
        break
    if bag_weight < lower_bound:
        print("The bag of rice is underweight")
        break
    elif bag_weight > 4.9 and bag_weight < 5.1:
        print("The bag of rice is the correct weight")

