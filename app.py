import google.generativeai as genai

# the "brain" for scanning meals
def scan_meal(image_path):
    model = genai.GenerativeModel('gemini-1.5-flash')
    # we ask the ai to be a nutritionist
    prompt = "look at this meal and estimate the calories, protein, carbs, and fat. be realistic."
    response = model.generate_content([prompt, image_path])
    return response.text

# the habit tracking logic
habits = {"gym": False, "read": False, "no sugar": False}

def check_habit(habit_name):
    if habit_name in habits:
        habits[habit_name] = True
        print(f"safe, you completed {habit_name}! 💫")

# example run
# meal_stats = scan_meal("chicken_rice.jpg")
# print(meal_stats)

