from django.shortcuts import render
# when you're no longer returning and HttpResponse, then you can delete the following
# import statement... Should be using templates like it's being done inside of the
# browse_recipes method
from django.http import HttpResponse

# mock database entry
recipes = [
    {
        "name": "World's Best Lasagna",
        "ingredients": ["noodles", "pasta sauce", "ground beef"],
        "prep_time": 20,
        "total_time": 75
    },
    {
        "name": "Chicken Noodle Soup",
        "ingredients": ["noodles", "chicken", "broth"],
        "prep_time": 15,
        "total_time": 45
    }
]

def browse_recipes(request):
    # pulling mock database entry from above to be used on the
    # browse recipes page
    context = {
        "recipes": recipes
    }
    # the 3rd parameter in the return statement, 'context', allows
    # you to use the data from the mock database entry inside of the html file
    # template, browse_recipes.htm
    return render(request, 'recipe/browse_recipes.html', context)


def view_recipe(request):
    return HttpResponse('<h1>View Recipe Page</h1>')