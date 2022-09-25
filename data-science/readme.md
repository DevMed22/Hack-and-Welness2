# DietKit
## Class Structure
This library includes three classes to represent diet: Ingredient, Menu and Diet.  
Ingredient class stands for grocery ingredients. Each Ingredient instance includes nutrition information.  
Menu class stands for dishes served in diet. Each Menu instance contains its own ingredients.  
Diet class stands for diet plan. It is not single diet, but bundle of several diets. It is consist with pair of identifier and contents of diet.  
Also, Dietkit contains class 'Criteria' which stands for nutrition criteria. It is used as input to the evaluation method to evaluate nutrition of the menu or diet.

## Functions
Dietkit's function is divided into three main functions: Loader, Evaluator and Visualizer.  
Loader functions load ingredient, menu or diet data. If the specific file path is not passed, it automatically loads the our sample data.  
Evaluator functions evaluate the menu or diet in terms of ingredients and nutrition based on user's criteria.
Visualizer functions graphically visualize the diet's information or evaluation results.
