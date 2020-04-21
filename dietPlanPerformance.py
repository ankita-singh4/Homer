def dietPlanPerformance(calories, k, lower, upper):
    n = len(calories)
    caloricSum = 0
    pts =0
    caloricSum =sum(calories[i] for i in range(k))
    if caloricSum < lower:
        pts -= 1
    elif caloricSum > upper:
        pts += 1
    for i in range(n-k):
        caloricSum = caloricSum- calories[i]+ calories[i+k]
        if caloricSum < lower:
            pts -=1
        elif caloricSum > upper:
            pts +=1
    return pts


calories = [6,5,0,0]
k = 2
lower = 1
upper = 5
print(dietPlanPerformance(calories,k,lower,upper))

di