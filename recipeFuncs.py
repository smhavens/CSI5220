import pandas as pd

pantry = {"PantryItem": [], "ItemQty": [], "Units": []}
pantry = pd.DataFrame(pantry)
privateRecipes = {"RecipeName": [], "Instructions": [], "Servings": [], "Description": [], "isPublic": []}
privateRecipes = pd.DataFrame(privateRecipes)
publicRecipes = {"RecipeName": [], "Instructions": [], "Servings": [], "Description": []}
publicRecipes = pd.DataFrame(publicRecipes)
mealPlan = {"RecipeName": [], "Instructions": [], "Servings": [], "Description": []}
mealPlan = pd.DataFrame(mealPlan)
allIngPrivate = {"RecipeName": [], "ItemName": [], "ItemQty": [], "Units": []}
allIngPrivate = pd.DataFrame(allIngPrivate)
allIngPublic = {"RecipeName": [], "ItemName": [], "ItemQty": [], "Units": []}
allIngPublic = pd.DataFrame(allIngPublic)
allIngMealPlan = {"RecipeName": [], "ItemName": [], "ItemQty": [], "Units": []}
allIngMealPlan = pd.DataFrame(allIngMealPlan)


# view tables
def viewAll(table):
    table = table.sort_index()
    print(table)


# pantry functions
def addPantryItem(food, qty, units):
    pantry.loc[-1] = [food, qty, units]
    pantry.index = pantry.index + 1


def removePantryItem(itemName):
    pantry.drop(pantry[(pantry["PantryItem"] == itemName)].index, inplace=True)


def searchPantryByName(itemName):
    foundItems = pantry[pantry["PantryItem"] == itemName]
    viewAll(foundItems)


def updatePantry(type, itemName, newValue):
    update = pantry["PantryItem"] == itemName
    pantry.loc[update, type] = newValue


# public/private recipe functions
def addPrivateRecipe(title, instructions, servings, desc, ispublic):
    privateRecipes.loc[-1] = [title, instructions, servings, desc, ispublic]
    privateRecipes.index = privateRecipes.index + 1
    if ispublic == True:
        publicRecipes.loc[-1] = [title, instructions, servings, desc]
        publicRecipes.index = publicRecipes.index + 1


def removePublicRecipe(recipeName):
    if (privateRecipes[(privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        privateRecipes.loc[privateRecipes["RecipeName"] == recipeName, "isPublic"] = False
        publicRecipes.drop(publicRecipes[publicRecipes["RecipeName"] == recipeName].index, inplace=True)


def removePrivateRecipe(recipeName):
    removePublicRecipe(recipeName)
    privateRecipes.drop(privateRecipes[privateRecipes["RecipeName"] == recipeName].index, inplace=True)


def searchRecipesByName(table, recipeName):
    foundRecipes = table[table["RecipeName"] == recipeName]
    viewAll(foundRecipes)


def updateRecipe(type, recipeName, newValue):
    update = privateRecipes["RecipeName"] == recipeName
    privateRecipes.loc[update, type] = newValue
    if (privateRecipes[(privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        publicRecipes.loc[update, type] = newValue
    if (type == "isPublic") and (newValue == True):
        df = privateRecipes[privateRecipes["RecipeName"] == recipeName]
        publicRecipes.loc[-1] = [df.iat[0, 0], df.iat[0, 1], df.iat[0, 2], df.iat[0, 3]]
        publicRecipes.index = publicRecipes.index + 1


# recipe Ingredients
def addRecipeIng(recipeName, foodList, qtyList, unitsList):
    for i in range(len(foodList)):
        allIngPrivate.loc[-1] = [recipeName, foodList[i], qtyList[i], unitsList[i]]
        allIngPrivate.index = allIngPrivate.index + 1
    if (privateRecipes[(privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        for i in range(len(foodList)):
            allIngPublic.loc[-1] = [recipeName, foodList[i], qtyList[i], unitsList[i]]
            allIngPublic.index = allIngPublic.index + 1


def removeRecipeIng(recipeName, itemName):
    if (privateRecipes[(privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        allIngPublic.drop(allIngPublic[(allIngPublic["RecipeName"] == recipeName) & (allIngPublic["ItemName"] == itemName)].index, inplace=True)
    allIngPrivate.drop(allIngPrivate[(allIngPrivate["RecipeName"] == recipeName) & (allIngPrivate["ItemName"] == itemName)].index, inplace=True)


def allIngPerRecipe(table, recipeName):
    allIng = table.loc[table["RecipeName"] == recipeName]
    viewAll(allIng)


def updateRecipeIng(recipeName, itemName, type, newValue):
    update = allIngPrivate[(allIngPrivate["RecipeName"] == recipeName) & (allIngPrivate["ItemName"] == itemName)].index
    allIngPrivate.loc[update, type] = newValue
    if (privateRecipes[(privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        update = allIngPublic[(allIngPublic["RecipeName"] == recipeName) & (allIngPublic["ItemName"] == itemName)].index
        allIngPublic.loc[update, type] = newValue


def searchByIngName(table, itemName):
    foundRecipes = table[table["ItemName"] == itemName]
    viewAll(foundRecipes)


# Build plan functions
def addRecipeToMealPlan(recipeTable, ingTable, recipeName):
    df = recipeTable[recipeTable["RecipeName"] == recipeName]
    mealPlan.loc[-1] = [df.iat[0, 0], df.iat[0, 1], df.iat[0, 2], df.iat[0, 3]]
    mealPlan.index = mealPlan.index + 1
    df = ingTable[ingTable["RecipeName"] == recipeName]
    for i in range(len(df)):
        allIngMealPlan.loc[-1] = [df.iat[i, 0], df.iat[i, 1], df.iat[i, 2], df.iat[i, 3]]
        allIngMealPlan.index = allIngMealPlan.index + 1


def changeServings(recipeName, newValue):
    # slightly fucked
    update = mealPlan["RecipeName"] == recipeName
    factor = newValue / (mealPlan.loc[update, "Servings"])
    mealPlan.loc[update, "Servings"] = newValue
    # change Ing amount by servings
    itemQty = allIngMealPlan.loc[allIngMealPlan["RecipeName"] == recipeName, "ItemQty"]
    # get index of condition in allIngMealPlan
    rowUpdate = allIngMealPlan.loc[allIngMealPlan["RecipeName"] == recipeName]
    for i in range(len(rowUpdate)):
        x = itemQty[i] * factor
        allIngMealPlan.at[i, "ItemQty"] = x
    viewAll(allIngMealPlan)


"""Testing all build plan functions"""
addPrivateRecipe("omelette", "make the food", 3, "its good", False)
addPrivateRecipe("Grilled cheese", "make the food", 3, "its good", True)
addRecipeIng("omelette", ["eggs", "cheese"], [2, 1], ["each", "oz(dry"])
addRecipeIng("Grilled cheese", ["bread", "cheese", "butter", "tomato"], [3, 4, 1, 1],
             ["Slice", "oz(dry)", "Tbl", "each"])
addRecipeToMealPlan(privateRecipes, allIngPrivate, "omelette")
addRecipeToMealPlan(publicRecipes, allIngPublic, "Grilled cheese")
#addRecipeToMealPlan(privateRecipes, allIngPrivate, "omelette")
viewAll(allIngMealPlan)
viewAll(mealPlan)
changeServings("Grilled cheese", 6)
# viewAll(allIngMealPlan)

# def unitChange():

"""Testing all pantry functions"""
# addPantryItem("cheese", 1, "oz (dry)")
# addPantryItem("bread", 4, "slice")
# addPantryItem("eggs", 6, "each")
# searchPantryByName("eggs")
# updatePantry("ItemQty", "cheese", 4)
# removePantryItem("bread")
# viewAll(pantry)

"""Testing all recipe functions"""
# addPrivateRecipe("caprice salad", "make the food", 3, "its good", True)
# addPrivateRecipe("omelette", "make the food", 3, "its good", False)
# addPrivateRecipe("Grilled cheese", "make the food", 3, "its good", True)
# addPrivateRecipe("soup", "make the food", 3, "its good", True)
# viewAll(privateRecipes)
# viewAll(publicRecipes)
# searchRecipesByName(privateRecipes, "omelette")
# searchRecipesByName(publicRecipes, "caprice salad")
# updateRecipe("Servings", "Grilled cheese", 1)
# viewAll(privateRecipes)
# viewAll(publicRecipes)
# removePublicRecipe("caprice salad")
# removePrivateRecipe("Grilled cheese")
# viewAll(privateRecipes)
# viewAll(publicRecipes)


"""Testing all recipe functions"""
# addPrivateRecipe("Grilled cheese", "make the food", 3, "its good", True)
# addRecipeIng("Grilled cheese", ["bread", "cheese", "butter", "tomato"], [2, 4, 1, 1],
#              ["Slice", "oz(dry)", "Tbl", "each"])
# updateRecipeIng("Grilled cheese", "butter", "ItemQty", 5)
# allIngPerRecipe(allIngPrivate, "Grilled cheese")
# viewAll(allIngPublic)
# viewAll(allIngPrivate)
# removeRecipeIng("Grilled cheese", "tomato")
# viewAll(allIngPublic)
# viewAll(allIngPrivate)


"""Searching recipes by ingredient"""
# addPrivateRecipe("Grilled cheese", "make the food", 3, "its good", True)
# addPrivateRecipe("cheese", "eat the food", 3, "its good", False)
# addRecipeIng("Grilled cheese", ["bread", "cheese", "butter", "tomato"], [2, 4, 1, 1],
#              ["Slice", "oz(dry)", "Tbl", "each"])
# addRecipeIng("cheese", ["cheese"], [2], ["oz(dry)"])
# viewAll(allIngPrivate)
# viewAll(allIngPublic)
# searchByIngName(allIngPrivate, "cheese")
# searchByIngName(allIngPublic, "cheese")



