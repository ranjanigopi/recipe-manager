const ingredient = document.getElementById("ingredient");
const quantity = document.getElementById("quantity");
const units = document.getElementById("unit")
const ingredients = document.getElementById('ingredients-list');
const stepNumber = document.getElementById("step-no");
const stepName = document.getElementById("step-name");
const stepProcedure = document.getElementById('step-procedure');
const steps = document.getElementById('steps');


const ingredientList = [];
const stepList = [];

function renderIngredients() {
    ingredients.innerHTML = '';
    ingredientList.forEach(ing => {
        const unit = units.options[ing.unit].text;
        ingredients.innerHTML += `<li><b>${ing.ingredient}</b> - ${ing.quantity} ${unit}</li>`;
    })
}

function newIngredient(ingredient, quantity, unit) {
    return {
        ingredient: ingredient,
        quantity: quantity,
        unit: unit
    }
}

function addIngredient() {
    const item = newIngredient(ingredient.value, quantity.value, units.value)
    ingredientList.push(item)

    ingredient.value = null;
    quantity.value = null;
    units.value = null;
    ingredient.focus();

    renderIngredients();
}

function renderSteps() {
    steps.innerHTML = '';
    stepList.forEach(step => {
        steps.innerHTML += `<li><b>${step.stepNumber}. ${step.stepName}</b> - ${step.stepProcedure}</li>`;
    })
}

function newStep(stepNumber, stepName, stepProcedure) {
    return {
        stepNumber: stepNumber,
        stepName: stepName,
        stepProcedure: stepProcedure
    }
}


function addStep() {
    const step = newStep(stepList.length + 1, stepName.value, stepProcedure.value)
    stepList.push(step)

    stepName.value = null;
    stepProcedure.value = null;
    stepName.focus();
    renderSteps()
}

function redirectToAllRecipes() {
    window.location.href = '/recipe';
}

function saveRecipe() {
    return fetch(`/recipe/save`, {
        method: 'POST',
        body: JSON.stringify({
            name: document.getElementById('recipe-name').value,
            image: document.getElementById('image').value,
            time: document.getElementById('cooking-time').value,
            ingredients: ingredientList,
            steps: stepList
        })
    })
        .then((response) => {
            if (response.ok) {
                redirectToAllRecipes();
            }
        })
}


