ingredients = {}
ingredients['Sugar'] = {'capacity': 3, 'durability': 0, 'flavor': 0, 'texture': -3, 'calories': 2}
ingredients['Sprinkles'] = {'capacity': -3, 'durability': 3, 'flavor': 0, 'texture': 0, 'calories': 9}
ingredients['Candy'] = {'capacity': -1, 'durability': 0, 'flavor': 4, 'texture': 0, 'calories': 1}
ingredients['Chocolate'] = {'capacity': 0, 'durability': 0, 'flavor': -2, 'texture': 2, 'calories': 8}

total_size = 100

recipes = [(i,j,k,l) for i in range(total_size+1) for j in range(total_size+1-i) for k in range(total_size+1-i-j) for l in range(total_size+1-i-j-k)]
recipes = [r for r in recipes if sum(r)==total_size]

scores = []
cal_scores = []
for recipe in recipes:
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for i, ingr in enumerate(ingredients):
        capacity += recipe[i]*ingredients[ingr]['capacity']
        durability += recipe[i]*ingredients[ingr]['durability']
        flavor += recipe[i]*ingredients[ingr]['flavor']
        texture += recipe[i]*ingredients[ingr]['texture']
        calories += recipe[i]*ingredients[ingr]['calories']
    if min(capacity, durability, flavor, texture) < 0:
        score = 0
    else:
        score = capacity*durability*flavor*texture
    scores.append(score)
    if calories == 500:
        cal_scores.append(score)

print max(scores)
print max(cal_scores)
