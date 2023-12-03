import pandas as pd
        

class ItemList:
    def __init__(self, items=[], quantity=[], units=[], unitType=[]):
        self.ItemName = items
        self.ItemQty = quantity
        self.Units = units
        self.UnitType = unitType

    # def addItem(self, item, amount, unit, type):
    #     self.ItemName.append(item)
    #     self.ItemQty.append(amount)
    #     self.Units.append(unit)
    #     self.UnitType.append(type)

    # def removeItem(self, id):
    #     self.ItemName.pop(id)
    #     self.ItemQty.pop(id)
    #     self.Units.pop(id)
    #     self.UnitType.pop(id)

class Recipes:
    def __init__(self, names=[], inst=[], serving=[], desc=[]):
        self.RecipeName = names
        self.Instructions = inst
        self.Servings = serving
        self.Description = desc

    # def addRecipe(self, name, inst, serving, desc):
    #     self.RecipeName.append(name)
    #     self.Instructions.append(inst)
    #     self.Servings.append(serving)
    #     self.Description.append(desc)

    # def removeRecipe(self, id):
    #     self.RecipeName.pop(id)
    #     self.Instructions.pop(id)
    #     self.Servings.pop(id)
    #     self.Description.pop(id)

class PrivateRecipes:
    def __init__(self, recipes=[], instructions=[], servings=[], desc=[], isPublic=[]):
        self.RecipeName = recipes
        self.Instructions = instructions
        self.Servings = servings
        self.Description = desc
        self.isPublic = isPublic

    # def addPrivateRecipe(self, recipe, inst, serve, desc, public):
    #     self.RecipeName.append(recipe)
    #     self.Instructions.append(inst)
    #     self.Servings.append(serve)
    #     self.Description.append(desc)
    #     self.isPublic.append(public)

    # def removePrivateRecipe(self, id):
    #     self.RecipeName.pop(id)
    #     self.Instructions.pop(id)
    #     self.Servings.pop(id)
    #     self.Description.pop(id)
    #     self.isPublic.pop(id)

    # def setToPrivate(self, id):
    #     if self.isPublic[id]:
    #         self.isPublic[id] = False


class AllIng:
    def __init__(self, recipes=[], items=[], quantity=[], units=[], unitType=[]):
        self.RecipeName = recipes
        self.ItemName = items
        self.ItemQty = quantity
        self.Units = units
        self.UnitType = unitType


    # def addAllIng(self, recipe, item, quantity, unit, type):
    #     self.RecipeName.append(recipe)
    #     self.ItemName.append(item)
    #     self.ItemQty.append(quantity)
    #     self.Units.append(unit)
    #     self.UnitType.append(type)

    # def removeAllIng(self, id):
    #     self.RecipeName.pop(id)
    #     self.ItemName.pop(id)
    #     self.ItemQty.pop(id)
    #     self.Units.pop(id)
    #     self.UnitType.pop(id)

pantry = ItemList()
# pantry = {"ItemName": [], "ItemQty": [], "Units": [], "UnitType": []}
# pantry = pd.DataFrame(pantry)
pantry = pd.DataFrame(pantry.__dict__)
# groceries = {"ItemName": [], "ItemQty": [], "Units": [], "UnitType": []}
groceries = ItemList()
groceries = pd.DataFrame(groceries.__dict__)
# privateRecipes = {"RecipeName": [], "Instructions": [], "Servings": [], "Description": [], "isPublic": []}
privateRecipes = PrivateRecipes()
privateRecipes = pd.DataFrame(privateRecipes.__dict__)
# publicRecipes = {"RecipeName": [], "Instructions": [], "Servings": [], "Description": []}
publicRecipes = Recipes()
publicRecipes = pd.DataFrame(publicRecipes.__dict__)
# mealPlan = {"RecipeName": [], "Instructions": [], "Servings": [], "Description": []}
mealPlan = Recipes()
mealPlan = pd.DataFrame(mealPlan.__dict__)
# allIngPrivate = {"RecipeName": [], "ItemName": [], "ItemQty": [], "Units": [], "UnitType": []}
allIngPrivate = AllIng()
allIngPrivate = pd.DataFrame(allIngPrivate.__dict__)
# allIngPublic = {"RecipeName": [], "ItemName": [], "ItemQty": [], "Units": [], "UnitType": []}
allIngPublic = AllIng()
allIngPublic = pd.DataFrame(allIngPublic.__dict__)
# allIngMealPlan = {"RecipeName": [], "ItemName": [], "ItemQty": [], "Units": [], "UnitType": []}
allIngMealPlan = AllIng()
allIngMealPlan = pd.DataFrame(allIngMealPlan.__dict__)

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
    # reset index and find all matching pantry items
    pantry.reset_index(drop=True, inplace=True)
    currentType = pantry.loc[pantry["ItemName"] == itemName, "UnitType"].values
    # change imperial units to metric
    if currentType == "Imperial":
        update = pantry["ItemName"] == itemName
        pantry.loc[update, "UnitType"] = "Metric"
        x = pantry.loc[update, "Units"].values.tolist()
        pantry.loc[update, "ItemQty"] = pantry.loc[update, "ItemQty"] * unitValsDict[x[0]]
        pantry.loc[update, "Units"] = unitNameDict[x[0]]
    # change metric units to imperial
    elif currentType == "Metric":
        update = pantry["ItemName"] == itemName
        pantry.loc[update, "UnitType"] = "Imperial"
        x = pantry.loc[update, "Units"].values.tolist()
        pantry.loc[update, "ItemQty"] = pantry.loc[update, "ItemQty"] * unitValsDict[x[0]]
        pantry.loc[update, "Units"] = unitNameDict[x[0]]
        x = pantry.loc[update, "Units"].values.tolist()
        y = pantry.loc[update, "ItemQty"].values.tolist()
        # simplifying units from tsp to Tbsp and oz to cups when applicable
        if (x[0] == "tsp") and (y[0] % 3 == 0):
            y[0] /= 3
            pantry.loc[update, "ItemQty"] = y[0]
            pantry.loc[update, "Units"] = "Tbsp"
        if (x[0] == "oz (liquid)") and (y[0] % 8 == 0):
            y[0] /= 8
            pantry.loc[update, "ItemQty"] = y[0]
            pantry.loc[update, "Units"] = "cups (liquid)"
    else:
        print("no change made")


'''public/private recipe functions'''  # finished :)


def addPrivateRecipe(title, instructions, servings, desc, ispublic):
    # checking if a recipe with that name already exists
    if (privateRecipes["RecipeName"] == title).any():
        print("This recipe is already in your library. Please choose another name.")
    else:
        # appending a new recipe to the table
        privateRecipes.loc[-1] = [title, instructions, servings, desc, ispublic]
        privateRecipes.index = privateRecipes.index + 1
        if ispublic == True:
            publicRecipes.loc[-1] = [title, instructions, servings, desc]
            publicRecipes.index = publicRecipes.index + 1


def removePublicRecipe(recipeName):
    # checking to see if the recipe given is publicly available
    if (
            privateRecipes[
                (privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        # removing the recipe and updating table index
        privateRecipes.loc[privateRecipes["RecipeName"] == recipeName, "isPublic"] = False
        publicRecipes.drop(publicRecipes[publicRecipes["RecipeName"] == recipeName].index, inplace=True)


def removePrivateRecipe(recipeName):
    # removing the recipe and updating table index
    removePublicRecipe(recipeName)
    privateRecipes.drop(privateRecipes[privateRecipes["RecipeName"] == recipeName].index, inplace=True)


def searchRecipesByName(table, recipeName):
    foundRecipes = table[table["RecipeName"] == recipeName]
    return foundRecipes


def updateRecipe(type, recipeName, newValue):
    # finding entry to update
    update = privateRecipes["RecipeName"] == recipeName
    privateRecipes.loc[update, type] = newValue
    # updating value if in both the public and private library when applicable
    if (
            privateRecipes[
                (privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        publicRecipes.loc[update, type] = newValue
    if (type == "isPublic") and (newValue == True):
        df = privateRecipes[privateRecipes["RecipeName"] == recipeName]
        publicRecipes.loc[-1] = [df.iat[0, 0], df.iat[0, 1], df.iat[0, 2], df.iat[0, 3]]
        publicRecipes.index = publicRecipes.index + 1


'''recipe Ingredients'''  # Finished :)


def addRecipeIng(recipeName, food, qty, units, unitsType):
    allIngPrivate.reset_index(drop=True, inplace=True)
    allIngPublic.reset_index(drop=True, inplace=True)
    allIngPrivate.loc[-1] = [recipeName, food, qty, units, unitsType]
    allIngPrivate.index = allIngPrivate.index + 1
    if (
            privateRecipes[
                (privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        allIngPublic.loc[-1] = [recipeName, food, qty, units, unitsType]
        allIngPublic.index = allIngPublic.index + 1


def removeRecipeIng(recipeName, itemName):
    # checking if the listed ingredient is in both the public and private libraries
    if (
            privateRecipes[
                (privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        # removing the ingredient and updating the public table indices
        allIngPublic.drop(
            allIngPublic[(allIngPublic["RecipeName"] == recipeName) & (allIngPublic["ItemName"] == itemName)].index,
            inplace=True)
    # removing the ingredient and updating the private table indices
    allIngPrivate.drop(
        allIngPrivate[(allIngPrivate["RecipeName"] == recipeName) & (allIngPrivate["ItemName"] == itemName)].index,
        inplace=True)


def removeAllIngForOneRecipe(recipeName, removePriv):
    if (
            privateRecipes[
                (privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        allIngPublic.drop(
            allIngPublic[(allIngPublic["RecipeName"] == recipeName)].index,
            inplace=True)
    if removePriv == True:
        allIngPrivate.drop(
            allIngPrivate[(allIngPrivate["RecipeName"] == recipeName)].index,
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


def updateAllIngForOneRecipe(recipeName, type, newValue):
    update = allIngPrivate[(allIngPrivate["RecipeName"] == recipeName)].index
    allIngPrivate.loc[update, type] = newValue
    if (
            privateRecipes[
                (privateRecipes["RecipeName"] == recipeName) & (privateRecipes["isPublic"] == True)]).empty == False:
        update = allIngPublic[(allIngPublic["RecipeName"] == recipeName)].index
        allIngPublic.loc[update, type] = newValue


def searchByIngName(table, itemName):
    foundRecipes = table[table["ItemName"] == itemName]
    return foundRecipes


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
addPrivateRecipe("caprice salad", "make the food", 3, "its good", True)
addPrivateRecipe("omelette", "make the food", 3, "its good", False)
addPrivateRecipe("Grilled cheese", "make the food", 3, "its good", True)
addPrivateRecipe("soup", "make the food", 3, "its good", True)
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
addRecipeIng("Grilled cheese", "bread", 2, "Slice", "Other")
addRecipeIng("Grilled cheese", "butter", 1, "Tbsp", "Imperial")
addRecipeIng("Grilled cheese", "tomato", 1, "Each", "Other")
addRecipeIng("omelette", "eggs", 2, "Each", "Other")
# viewAll(allIngPrivate)
# viewAll(allIngPublic)
# searchByIngName(allIngPrivate, "cheese")
# searchByIngName(allIngPublic, "cheese")
# x = allIngPrivate["RecipeName"].tolist()
# print(x)


"""Testing all build plan functions"""
# addPrivateRecipe("omelette", "make the food", 3, "its good", False)
# addPrivateRecipe("Grilled cheese", "make the food", 3, "its good", True)
# addRecipeIng("omelette", ["eggs", "cheese"], [2, 1], ["each", "oz (dry)"], ["Other", "Imperial"])
# addRecipeToMealPlan(privateRecipes, allIngPrivate, "omelette")
# addRecipeToMealPlan(publicRecipes, allIngPublic, "Grilled cheese")
addRecipeToMealPlan(privateRecipes, allIngPrivate, "omelette")
viewAll(allIngMealPlan)
# viewAll(mealPlan)
# changeServings("Grilled cheese", 6)
# unitChange("Grilled cheese", "Metric")
# print("start")
# # viewAll(allIngMealPlan)
# # clearMealPlan()
# # viewAll(mealPlan)
# # removeRecipeFromMealPlan("omelette")
# # viewAll(mealPlan)
# # viewAll(allIngMealPlan)
# groceryList()

