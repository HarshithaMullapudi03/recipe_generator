import pandas as pd

# Data for the recipes
data = {
    "recipe": [
        "Tomato Soup", "Garlic Bread", "Mixed Berry Smoothie", "Vegetable Stir-fry",
        "Chicken Salad", "Beef Stew", "Egg Salad", "Pasta", "Butter Chicken", "Chocolate Cake"
    ],
    "ingredients": [
        "tomato, butter, garlic, onion", "garlic, butter, bread", "mixed berries, yogurt, honey", 
        "onion, garlic, broccoli, carrot", "chicken, lettuce, tomato, onion", "beef, potato, carrot, onion, garlic", 
        "egg, mayonnaise, mustard, lettuce", "spaghetti, tomato, garlic, onion, olive oil", 
        "chicken, butter, garlic, onion, tomato, spices", "flour, sugar, egg, butter, cocoa powder"
    ],
    "procedure": [
        "1. Heat the butter in a pan. 2. Add garlic and onion and sauté. 3. Add tomatoes and cook until soft. 4. Blend the mixture and simmer. 5. Serve hot.",
        "1. Preheat the oven to 350°F. 2. Spread butter and garlic on bread slices. 3. Bake for 10 minutes.",
        "1. Blend mixed berries, yogurt, and honey until smooth. 2. Serve chilled.",
        "1. Stir-fry garlic and onion in a pan. 2. Add broccoli and carrot. 3. Cook until vegetables are tender. 4. Serve hot.",
        "1. Boil the chicken and shred it. 2. Mix with lettuce, tomato, and onion. 3. Add dressing and toss.",
        "1. Brown the beef in a pot. 2. Add onion and garlic, sauté. 3. Add potatoes and carrots. 4. Simmer for 1 hour.",
        "1. Boil eggs and chop them. 2. Mix with mayonnaise and mustard. 3. Serve on a bed of lettuce.",
        "1. Boil spaghetti in salted water. 2. Sauté garlic and onion in olive oil. 3. Add tomato and cook. 4. Toss pasta with the sauce.",
        "1. Cook chicken with spices. 2. Sauté garlic and onion in butter. 3. Add tomato and cook. 4. Add chicken to the sauce and simmer.",
        "1. Preheat the oven to 350°F. 2. Mix flour, sugar, cocoa powder, eggs, and butter. 3. Pour into a pan and bake for 30 minutes."
    ]
}

# Create a DataFrame
recipes_df = pd.DataFrame(data)

# Save to CSV
recipes_df.to_csv('recipes.csv', index=False)

print("recipes.csv file has been created successfully.")
