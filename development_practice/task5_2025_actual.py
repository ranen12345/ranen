
# #5.1

# def total_cost(cost):
#     tax = cost * 0.09             #cal tax of 9%
#     cost_with_tax = cost + tax
#     return cost_with_tax




#5.2

# def total_cost(cost):
#     tax = cost * 0.09             #cal tax of 9%
#     cost_with_tax = cost + tax
#     return cost_with_tax

# def discount(cost):
#     total = total_cost(cost)
    
#     if total >= 50 and total < 100:
#         discount_cost = total - (total * 0.05)
#     elif total > 100:
#         discounted_cost = total - (total * 0.10)
#     else:
#         discount_cost = total # if not discount then its the original total

#     return discount_cost






#5.3

def total_cost(cost):
    tax = cost * 0.09             #cal tax of 9%
    cost_with_tax = cost + tax
    return cost_with_tax

def discount(cost):
    total = total_cost(cost)
    
    if total >= 50 and total < 100:
        discount_cost = total - (total * 0.05)
    elif total > 100:
        discounted_cost = total - (total * 0.10)
    else:
        discount_cost = total # if not discount then its the original total

    return discount_cost

def reward_points (total_discounted_cost)