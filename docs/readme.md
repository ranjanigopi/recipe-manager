#Recipe Manager
Recipe Manager is an application which manages pantry and recipes based on the 
ingredient quantity in pantry. This application has three main scopes of managing the kitchen.
 - Pantry
   - Pantry contains all the items in the kitchen essential for cooking along with quantity.
   - We can add items to the pantry and manage them
 - Recipes
   - Recipes contains all the recipe to cook with ingredients needed and the procedure
   - We can add new recipe with their procedure and ingredients needed
   - Shows the recipes to cook based on the pantry item availability
   - Cooking the available recipe will decrease the used ingredients quantity from pantry
   - Allows us to add the unavailable item to shopping list
 - Shopping list
   - Shows the unavailable recipe's ingredients
   - Allows us to add individual items to shopping list
   - Item bought from the shopping list will update the Pantry      

##Models :
 - Item
   - repository of all items and its unit
 - Unit
   - repository of all units and its base unit with conversion rate
 - Pantry
   - Contains Item and its quantity
 - Recipe
   - Contains name, image and the cooking time of the recipe
 - Ingredient
   - Contains item, quantity and unit for the recipe
 - Step
   - Contains the step order number with step name and detailed procedure of the recipe
 - ShoppingList
   - Contains quantity and unit of item to buy

##Pages Functionality
- Index page
  - Shows menu for three scopes of the project. **Pantry**, **Recipes** and **Shopping list**
 - Pantry
   - Pantry menu from index page shows us the list of items available in pantry with quantity and unit.
   - This page also allows us to add items to Pantry.
-   Add Item (From Pantry page)
    - Add Item button in Pantry page allows us to *add items to the pantry*.
    - If the added item is already present in Pantry, the quantity gets increased for the item.
    - If not present, the newly added item gets stored in the pantry table.
    - Same kind of check for Item table happens. If the newly added item is not present in Item table, it is added to the Item table.
 - Recipe page
   - Recipe from index page or from menu takes us to the page which *lists all the recipes*.
   - Clicking on a recipe will shows the Recipe view page.
        -   Recipe view page
            - Shows us all the details about the recipe such as name, Image, Cooking time, ingredients and procedure with steps.
    - Recipe page has two buttons, Recipe availability and Add recipe.
        -   Add Recipe 
            - Allows us to add new recipe by filling the form.
            - Can add multiple ingredients using Add next ingredient button. Added ingredients will be listed above ingredient field (for reference).
            - Can add multiple steps using Add Next step. Added steps will be listed above Step name field (for reference).
   
        -   Recipe availability page
            - Shows recipe status based on the items available in pantry.
            - Recipes list in Available recipe category are ready to cook, i.e. all the ingredients are present in pantry.
            - Recipes in unavailable category does not have one or more ingredients available in pantry.            
            
                 1.   Available recipe:
                      - Clicking on any of the recipe from available recipe list, displays the recipe view page with Cooked this recipe button.
                      - On clicking Cooked this recipe, the ingredients quantity will be reduced from the pantry.(if the recipe is cooked)
                 1.   Unavailable recipe:
                      - Clicking on any of the recipe from unavailable recipe list, displays the recipe view page with Add to shopping list button.
                      - On clicking Add to shopping list button, all the ingredients of the recipe are added to the shopping list table.
 - Shopping list
   - Clicking on Shopping list from menu takes us to the page which lists all the items to buy.  
   - Also allows us to add individual items to shopping list using Add item button. (Same functionality as Pantry Add item)
   - Shopping list page displays the items added from the unavailable recipe view page and also from add item button.
   - Item bought button updates the pantry with the quantity of item bought. Quantity and unit of item bought can be entered by us.
   - Remove item button removes the item from the shopping list.
   
 #Specification:
  - Uniqueness of project:
    - It will not resemble any of the projects taught in the course or copy from others.
    - It is an own concept designed to use on daily basis
  - Django Model and JavaScript:
    - It uses 7 models (listed above) for Django
    - It uses JavaScript for  Adding ingredients and steps in Add recipe form.
  - Mobile responsive
    - Designed to meet this criteria
  - Design and complexity
    - In order to have a clear shopping list, collection of recipes and manage the pantry effectively, I created this project. 
    - It is created for my own use to help manage my Kitchen efficiently.
    - Used HTML, CSS, Python and Javascript for the development of this project. No additional packages were used.
    - Creating this application through the learnings form this course, I believe this application stand unique.