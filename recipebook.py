'''ingredients = [["1 cup raspberries", "1/2 mint", "1 tablespoon sugar", "3/4 cup rum", "1 tablespoon lime", "750 milliliter bottle Lillet", "ice", "1 cup seltzer"], ["1 piece"]]
directions = ["blah", "blahh"]

drink_recipe = {'ingredients' : ingredients[0], 'directions' : directions[0]}
other_recipe = {'ingredients' : ingredients[1], 'direction' : directions[1]}

cookbook = {'drink' : drink_recipe, 'other' : other_recipe}

recipe = input("Which recipe do you want?")

if (recipe == "drink"):
    x = 0
if (recipe == "other"):
    x = 1

for i in ingredients[x]:
    print(i)
print(directions[x])'''

drink_recipe = {'raspberries' : '1 cup', 'mint' : '1/2 cup'}

ingredient = input("What ingredient?")

print(ingredient.value())
