import requests

area_to_flag = {
    'American': 'US',
    'Australian': 'AU',
    'British': 'GB',
    'Canadian': 'CA',
    'Chinese': 'CN',
    'Dutch': 'NL',
    'French': 'FR',
    'Greek': 'GR',
    'Indian': 'IN',
    'Italian': 'IT',
    'Jamaican': 'JM',
    'Japanese': 'JP',
    'Malaysian': 'MY',
    'Mexican': 'MX',
    'Moroccan': 'MA',
    'Norwegian': 'NO',
    'Portuguese': 'PT',
    'Polish': 'PL',
    'Russian': 'RU',
    'Spanish': 'ES',
    'Thai': 'TH',
    'Tunisian': 'TN',
    'Turkish': 'TR',
    'Vietnamese': 'VN'
}


def search_recipes():
    ingredient = input('Enter ingredient: ')
    url = f'https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            meals = data['meals']
            if meals is None:
                print('No result found')
                return None
            for meal in meals: 
                print(meal['strMeal'])
            choice = int(input('Pick a number: '))
            if choice < 1 or choice > len(meals):
                print('Invalid choice')
                return None
            
            selected_meal = meals[choice -1] 
            return selected_meal
        elif response.status_code == 404:
            print("Error: Dessert not found")
            return None
        else:
            print(f"Server Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException:
        print("Error: Could not connect to the internet.")
        return None
   

def get_details(selected_meal):
    if selected_meal is None:
        return None
    
    meal_id = selected_meal['idMeal']
    second_url = f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}'

    response = requests.get(second_url)
    meal_data = response.json()
    meal = meal_data['meals'][0]

    area = meal["strArea"]  
    flag = area_to_flag.get(area, "Unknown")   
    print(f"Origin: {area} {flag}") 
    return meal
def display_result(meal):
    if meal is not None:
        print(meal['strInstructions'])
    else:
        print('No instructions to display')


selected_meal = search_recipes()
if selected_meal is not None:
    meal = get_details(selected_meal)
    if meal is not None:
        display_result(meal)
    else:
        print('Could not get meal details')
else:
    print('No recipe selected')



