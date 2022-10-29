from multiprocessing import context
from unittest import result
from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    # Part 1 code. Refactored in part 2.
    # return """
    # <form action="/froyo_results" method="GET">
    #     What is your favorite Fro-Yo flavor? <br/>
    #     <input type="text" name="flavor"><br/>
    #     What toppings would you like on your Fro-Yo? <br/>
    #     <input type="text" name="toppings"><br/>
    #     <input type="submit" value="Submit!">
    # </form>
    # """
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    # Part 1 code. Refactored in part 2.
    # users_froyo_flavor = request.args.get('flavor')
    # users_froyo_toppings = request.args.get('toppings')
    # return f'You ordered {users_froyo_flavor} flavored Fro-Yo with {users_froyo_toppings} on top!'

    context = {
        'users_froyo_flavor': request.args.get('flavor'),
        'users_froyo_toppings': request.args.get('toppings')
    }
    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What's your favorite color? <br/>
        <input type="text" name="color"><br/>
        What's your favorite animal? <br/>
        <input type="text" name="animal"> <br/>
        What's your favorite city? <br/>
        <input type="text" name="city"> <br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_fav_color = request.args.get('color')
    users_fav_animal = request.args.get('animal')
    users_fav_city = request.args.get('city')
    return f'Wow, I didn\'t know {users_fav_color} {users_fav_animal}s lived in {users_fav_city}!'

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Enter a secret message: <br/>
        <input type="text" name="message"> <br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_message = request.form.get('message')
    sorted_message = sort_letters(users_message)
    return f'Here\'s your secret message! \n{sorted_message}'

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    # Part 1 code. Refactored in part 2.
    # return """
    # <form action="/calculator_results" method="GET">
    #     Please enter 2 numbers and select an operator.<br/><br/>
    #     <input type="number" name="operand1">
    #     <select name="operation">
    #         <option value="add">+</option>
    #         <option value="subtract">-</option>
    #         <option value="multiply">*</option>
    #         <option value="divide">/</option>
    #     </select>
    #     <input type="number" name="operand2">
    #     <input type="submit" value="Submit!">
    # </form>
    # """
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    # Part 1 code. Refactored in part 2.
    # provided_operand1 = request.args.get('operand1')
    # provided_operand2 = request.args.get('operand2')
    # selected_operation = request.args.get('operation')

    # if selected_operation == "add":
    #     result = int(provided_operand1) + int(provided_operand2)
    # elif selected_operation == "subtract":
    #     result = int(provided_operand1) - int(provided_operand2)
    # elif selected_operation == "multiply":
    #     result = int(provided_operand1) * int(provided_operand2)
    # else:
    #     result = int(provided_operand1) / int(provided_operand2)

    # return f'You chose to {selected_operation} {provided_operand1} and {provided_operand2}. Your result is: {result}

    return render_template('calculator_results.html',
        provided_operand1 = int(request.args.get('operand1')),
        provided_operand2 = int(request.args.get('operand2')),
        selected_operation = request.args.get('operation'))



HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = ''

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = ''

    # TODO: Generate a random number from 1 to 99
    lucky_number = 0

    context = {
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
