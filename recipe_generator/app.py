from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the recipe dataset
recipes_df = pd.read_csv('recipes.csv')

# Normalize ingredients function
def normalize_ingredients(ingredients):
    if pd.isna(ingredients):  # Handle NaN or missing values
        return []
    # Clean and normalize the ingredients
    ingredients = ingredients.lower().replace(" ", "").split(",")
    return [ingredient.strip() for ingredient in ingredients if ingredient]

# Function to recommend recipes based on user ingredients
def recommend_recipes(user_ingredients):
    recommended_recipes = []

    # Normalize user ingredients
    normalized_user_ingredients = normalize_ingredients(user_ingredients)
    
    # Iterate through recipes and compare ingredients
    for index, row in recipes_df.iterrows():
        recipe_ingredients = normalize_ingredients(row['ingredients'])  # Normalize recipe ingredients
        
        # Match ingredients (intersection of user ingredients and recipe ingredients)
        if set(normalized_user_ingredients).intersection(set(recipe_ingredients)):
            recommended_recipes.append({
                'name': row['recipe'],
                'procedure': row['procedure'],
                'ingredients': row['ingredients']
            })  # Add recipe details to recommendations
    print(recommended_recipes)

    return recommended_recipes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommendations():
    user_ingredients = request.form['ingredients']
    recommended_recipes = recommend_recipes(user_ingredients)
    return render_template('recommendations.html', recipes=recommended_recipes)

@app.route('/recipe/<recipe_name>')
def recipe_details(recipe_name):
    # Find the recipe by name
    recipe = recipes_df[recipes_df['recipe'] == recipe_name].iloc[0]
    return render_template('recipe_detail.html', recipe=recipe)



if __name__ == '__main__':
    app.run(debug=True)
