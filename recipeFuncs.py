import pandas as pd

pantry = {"ItemName": [], "ItemQty": [], "Units": [], "UnitType": []}
pantry = pd.DataFrame(pantry)
groceries = {"ItemName": [], "ItemQty": [], "Units": [], "UnitType": []}
groceries = pd.DataFrame(groceries)
privateRecipes = {"RecipeName": [], "Instructions": [], "Servings": [], "Description": [], "isPublic": []}
privateRecipes = pd.DataFrame(privateRecipes)
publicRecipes = {"RecipeName": [], "Instructions": [], "Servings": [], "Description": []}
publicRecipes = pd.DataFrame(publicRecipes)
mealPlan = {"RecipeName": [], "Instructions": [], "Servings": [], "Description": []}
mealPlan = pd.DataFrame(mealPlan)
allIngPrivate = {"RecipeName": [], "ItemName": [], "ItemQty": [], "Units": [], "UnitType": []}
allIngPrivate = pd.DataFrame(allIngPrivate)
allIngPublic = {"RecipeName": [], "ItemName": [], "ItemQty": [], "Units": [], "UnitType": []}
allIngPublic = pd.DataFrame(allIngPublic)
allIngMealPlan = {"RecipeName": [], "ItemName": [], "ItemQty": [], "Units": [], "UnitType": []}
allIngMealPlan = pd.DataFrame(allIngMealPlan)

# all units not in these dicts will not be changed during conversion
unitValsDict = {"oz (liquid)": 29.574,
                "mL": (1 / 29.574),
                "oz (dry)": 28.3495,
                "g": (1 / 28.3495),
                "cups (liquid)": 236.592,
                "Tbsp": 1.5,
                "tsp": 0.5,
                "dsp": 2}

unitNameDict = {"oz (liquid)": "mL",
                "mL": "oz (liquid)",
                "oz (dry)": "g",
                "g": "oz (dry)",
                "cups (liquid)": "mL",
                "Tbsp": "dsp",
                "tsp": "dsp",
                "dsp": "tsp"}

'''view tables'''


def viewAll(table):
    table = table.sort_index()
    print(table)


'''pantry functions'''  # finished:)


def addPantryItem(food, qty, units, unitType):
    if (pantry["ItemName"] == food).any():
        print("This item is already in your pantry")
    else:
        pantry.loc[-1] = [food, qty, units, unitType]
        pantry.index = pantry.index + 1


def removePantryItem(itemName):
    pantry.drop(pantry[(pantry["ItemName"] == itemName)].index, inplace=True)


def searchPantryByName(itemName):
    foundItems = pantry[pantry["ItemName"] == itemName]
    viewAll(foundItems)


def updatePantry(type, itemName, newValue):
    update = pantry["ItemName"] == itemName
    pantry.loc[update, type] = newValue


def changePantryUnitType(itemName):
    pantry.reset_index(drop=True, inplace=True)
    currentType = pantry.loc[pantry["ItemName"] == itemName, "UnitType"].values
    if currentType == "Imperial":
        update = pantry["ItemName"] == itemName
        pantry.loc[update, "UnitType"] = "Metric"
        x = pantry.loc[update, "Units"].values.tolist()
        pantry.loc[update, "ItemQty"] = pantry.loc[update, "ItemQty"] * unitValsDict[x[0]]
        pantry.loc[update, "Units"] = unitNameDict[x[0]]
    if currentType == "Metric":
        update = pantry["ItemName"] == itemName
        pantry.loc[update, "UnitType"] = "Imperial"
        x = pantry.loc[update, "Units"].values.tolist()
        pantry.loc[update, "ItemQty"] = pantry.loc[update, "ItemQty"] * unitValsDict[x[0]]
        pantry.loc[update, "Units"] = unitNameDict[x[0]]
        x = pantry.loc[update, "Units"].values.tolist()
        y = pantry.loc[update, "ItemQty"].values.tolist()
        if (x[0] == "tsp") and (y[0] % 3 == 0):
            y[0] /= 3
            pantry.loc[update, "ItemQty"] = y[0]
            pantry.loc[update, "Units"] = "Tbsp"
        if (x[0] == "oz (liquid)") and (y[0] % 8 == 0):
            y[0] /= 8
            pantry.loc[update, "ItemQty"] = y[0]
            pantry.loc[update, "Units"] = "cups (liquid)"


'''public/private recipe functions'''  # finished :)


def addPrivateRecipe(title, instructions, servings, desc, ispublic):
    privateRecipes.loc[-1] = [title, instructions, servings, desc, ispublic]
    privateRecipes.index = privateRecipes.index + 1
    if ispublic == True:
        publicRecipes.loc[-1] = [title, instructions, servings, desc]
        publicRecipes.index = publicRecipes.index + 1


def removePublicRecipe(recipeName):
    if (
            privateRecipes[
                (privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
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
    if (
            privateRecipes[
                (privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        publicRecipes.loc[update, type] = newValue
    if (type == "isPublic") and (newValue == True):
        df = privateRecipes[privateRecipes["RecipeName"] == recipeName]
        publicRecipes.loc[-1] = [df.iat[0, 0], df.iat[0, 1], df.iat[0, 2], df.iat[0, 3]]
        publicRecipes.index = publicRecipes.index + 1


'''recipe Ingredients'''  # Finished :)


def addRecipeIng(recipeName, foodList, qtyList, unitsList, unitsTypeList):
    allIngPrivate.reset_index(drop=True, inplace=True)
    allIngPublic.reset_index(drop=True, inplace=True)
    for i in range(len(foodList)):
        allIngPrivate.loc[-1] = [recipeName, foodList[i], qtyList[i], unitsList[i], unitsTypeList[i]]
        allIngPrivate.index = allIngPrivate.index + 1
    if (
            privateRecipes[
                (privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        for i in range(len(foodList)):
            allIngPublic.loc[-1] = [recipeName, foodList[i], qtyList[i], unitsList[i], unitsTypeList[i]]
            allIngPublic.index = allIngPublic.index + 1


def removeRecipeIng(recipeName, itemName):
    if (
            privateRecipes[
                (privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        allIngPublic.drop(
            allIngPublic[(allIngPublic["RecipeName"] == recipeName) & (allIngPublic["ItemName"] == itemName)].index,
            inplace=True)
    allIngPrivate.drop(
        allIngPrivate[(allIngPrivate["RecipeName"] == recipeName) & (allIngPrivate["ItemName"] == itemName)].index,
        inplace=True)


def allIngPerRecipe(table, recipeName):
    allIng = table.loc[table["RecipeName"] == recipeName]
    viewAll(allIng)


def updateRecipeIng(recipeName, itemName, type, newValue):
    update = allIngPrivate[(allIngPrivate["RecipeName"] == recipeName) & (allIngPrivate["ItemName"] == itemName)].index
    allIngPrivate.loc[update, type] = newValue
    if (
            privateRecipes[
                (privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        update = allIngPublic[(allIngPublic["RecipeName"] == recipeName) & (allIngPublic["ItemName"] == itemName)].index
        allIngPublic.loc[update, type] = newValue


def searchByIngName(table, itemName):
    foundRecipes = table[table["ItemName"] == itemName]
    viewAll(foundRecipes)


def changePubPrivRecipeUnitType(table, recipeName, changeType):
    table.reset_index(drop=True, inplace=True)
    allIng = table.index[table["RecipeName"] == recipeName].tolist()
    if changeType == "Metric":
        for i in allIng:
            if (table.iat[i, 4] == "Imperial") and (table.iat[i, 3] in unitNameDict):
                x = table.iat[i, 2] * unitValsDict[table.iat[i, 3]]
                table.iat[i, 2] = x
                table.iat[i, 3] = unitNameDict[table.iat[i, 3]]
                table.iat[i, 4] = "Metric"
    elif changeType == "Imperial":
        for i in allIng:
            if (table.iat[i, 4] == "Metric") and (table.iat[i, 3] in unitNameDict):
                x = table.iat[i, 2] * unitValsDict[table.iat[i, 3]]
                table.iat[i, 2] = x
                table.iat[i, 3] = unitNameDict[table.iat[i, 3]]
                table.iat[i, 4] = "Imperial"
                if table.iat[i, 3] == "tsp" and x % 3 == 0:
                    x /= 3
                    table.iat[i, 2] = x
                    table.iat[i, 3] = "Tbsp"
                if table.iat[i, 3] == "oz (liquid)" and x % 8 == 0:
                    x /= 8
                    table.iat[i, 2] = x
                    table.iat[i, 3] = "cups (liquid)"


def changeRecipeUnitType(recipeName, changeType):
    changePubPrivRecipeUnitType(allIngPrivate, recipeName, changeType)
    if (privateRecipes.loc[(privateRecipes["RecipeName"] == recipeName), "isPublic"]).empty == False:
        changePubPrivRecipeUnitType(allIngPublic, recipeName, changeType)


'''Build plan functions'''  # just grocery list :/


def addRecipeToMealPlan(recipeTable, ingTable, recipeName):
    allIngMealPlan.reset_index(drop=True, inplace=True)
    if (mealPlan.loc[mealPlan["RecipeName"] == recipeName]).all(1).any():
        print("This recipe is already in your meal plan")
    else:
        df = recipeTable[recipeTable["RecipeName"] == recipeName]
        mealPlan.loc[-1] = [df.iat[0, 0], df.iat[0, 1], df.iat[0, 2], df.iat[0, 3]]
        mealPlan.index = mealPlan.index + 1
        df = ingTable[ingTable["RecipeName"] == recipeName]
        for i in range(len(df)):
            allIngMealPlan.loc[-1] = [df.iat[i, 0], df.iat[i, 1], df.iat[i, 2], df.iat[i, 3], df.iat[i, 4]]
            allIngMealPlan.index = allIngMealPlan.index + 1


def changeServings(recipeName, newValue):
    allIngMealPlan.reset_index(drop=True, inplace=True)
    update = mealPlan["RecipeName"] == recipeName
    factor = newValue / (mealPlan.loc[update, "Servings"])
    mealPlan.loc[update, "Servings"] = newValue
    itemQty = allIngMealPlan.loc[allIngMealPlan["RecipeName"] == recipeName, "ItemQty"]
    ingIndex = allIngMealPlan[allIngMealPlan["RecipeName"] == recipeName].index.values.astype(int)
    for i in ingIndex:
        x = itemQty[i] * factor
        allIngMealPlan.at[i, "ItemQty"] = x


def unitChange(recipeName, changeType):
    changePubPrivRecipeUnitType(allIngMealPlan, recipeName, changeType)


def clearMealPlan():
    mealPlan.drop(mealPlan.index, inplace=True)
    allIngMealPlan.drop(allIngMealPlan.index, inplace=True)


def removeRecipeFromMealPlan(recipeName):
    mealPlan.drop(mealPlan[mealPlan["RecipeName"] == recipeName].index, inplace=True)
    allIngMealPlan.drop(allIngMealPlan[allIngMealPlan["RecipeName"] == recipeName].index, inplace=True)


def groceryList():
    # need to add something to make sure all units in one type (US/UK)
    groceries.drop(groceries.index, inplace=True)
    pantry.reset_index(drop=True, inplace=True)
    allIngMealPlan.reset_index(drop=True, inplace=True)
    viewAll(pantry)
    viewAll(allIngMealPlan)
    for i in range(len(allIngMealPlan)):
        itemName = allIngMealPlan.iat[i, 1]
        pantryItem = pantry.loc[pantry["ItemName"] == itemName]
        if (pantry.loc[pantry["ItemName"] == itemName]).all(1).any() and (
                pantryItem.Units.values == allIngMealPlan.iat[i, 3]):
            update = pantry["ItemName"] == itemName
            pantry.loc[update, "ItemQty"] = (pantry.loc[update, "ItemQty"]).values - allIngMealPlan.iat[i, 2]
        else:
            notInPantry = allIngMealPlan.iloc[i]
            x = (groceries["ItemName"] == itemName)
            y = (groceries["Units"] == notInPantry.iloc[3])
            if ((groceries.loc[y]).all(1).any() == True) & ((groceries.loc[x]).all(1).any() == True):
                groceries.loc[(y & x), "ItemQty"] = groceries.loc[(y & x), "ItemQty"].values + notInPantry.iloc[2]
            else:
                groceries.loc[-1] = [notInPantry.iloc[1], notInPantry.iloc[2], notInPantry.iloc[3], notInPantry.iloc[4]]
                groceries.index = groceries.index + 1
    addIng = pantry.loc[pantry["ItemQty"] < 0]
    pd.options.mode.copy_on_write = True
    addIng["ItemQty"] = addIng["ItemQty"].abs()
    x = list(pantry.loc[pantry["ItemQty"] == 0, "ItemName"])
    pantry.drop(pantry[(pantry["ItemQty"] <= 0)].index, inplace=True)
    for i in range(len(addIng)):
        groceries.loc[-1] = [addIng.iat[i, 0], addIng.iat[i, 1], addIng.iat[i, 2], addIng.iat[i, 3]]
        groceries.index = groceries.index + 1
    viewAll(groceries)
    viewAll(pantry)
    print(x)  # list of pantry ing == 0


"""Testing all pantry functions"""
addPantryItem("cheese", 1, "oz (dry)", "Imperial")
addPantryItem("bread", 4, "Slice", "Other")
addPantryItem("butter", 2, "Tbsp", "Imperial")
addPantryItem("eggs", 6, "each", "Other")
searchPantryByName("eggs")
updatePantry("ItemQty", "cheese", 4)
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
#              ["Slice", "oz(dry)", "Tbl", "each"], ["Other", "Imperial", "Imperial", "Other"])
# updateRecipeIng("Grilled cheese", "butter", "ItemQty", 5)
# allIngPerRecipe(allIngPrivate, "Grilled cheese")
# viewAll(allIngPublic)
# viewAll(allIngPrivate)
# removeRecipeIng("Grilled cheese", "tomato")
# viewAll(allIngPublic)
# viewAll(allIngPrivate)
# changeRecipeUnitType("Grilled cheese", "Metric")
# viewAll(allIngPrivate)
# viewAll(allIngPublic)
# changeRecipeUnitType("Grilled cheese", "Imperial")
# viewAll(allIngPrivate)
# viewAll(allIngPublic)


"""Searching recipes by ingredient"""
# addPrivateRecipe("Grilled cheese", "make the food", 3, "its good", True)
# addPrivateRecipe("cheese", "eat the food", 3, "its good", False)
# addRecipeIng("Grilled cheese", ["bread", "cheese", "butter", "tomato"], [2, 4, 1, 1],
#              ["Slice", "oz(dry)", "Tbl", "each"], ["Other", "Imperial", "Imperial", "Other"])
# addRecipeIng("cheese", ["cheese"], [2], ["oz(dry)"], ["Imperial"])
# viewAll(allIngPrivate)
# viewAll(allIngPublic)
# searchByIngName(allIngPrivate, "cheese")
# searchByIngName(allIngPublic, "cheese")


"""Testing all build plan functions"""
addPrivateRecipe("omelette", "make the food", 3, "its good", False)
addPrivateRecipe("Grilled cheese", "make the food", 3, "its good", True)
addRecipeIng("omelette", ["eggs", "cheese"], [2, 1], ["each", "oz (dry)"], ["Other", "Imperial"])
addRecipeIng("Grilled cheese", ["bread", "cheese", "butter", "tomato"], [2, 4, 1, 1],
             ["slice", "oz (dry)", "Tbsp", "each"], ["Other", "Imperial", "Imperial", "Other"])
addRecipeToMealPlan(privateRecipes, allIngPrivate, "omelette")
addRecipeToMealPlan(publicRecipes, allIngPublic, "Grilled cheese")
# addRecipeToMealPlan(privateRecipes, allIngPrivate, "omelette")
viewAll(allIngMealPlan)
viewAll(mealPlan)
changeServings("Grilled cheese", 6)
unitChange("Grilled cheese", "Metric")
print("start")
# viewAll(allIngMealPlan)
# clearMealPlan()
# viewAll(mealPlan)
# removeRecipeFromMealPlan("omelette")
# viewAll(mealPlan)
# viewAll(allIngMealPlan)
groceryList()
