from flask import Flask, render_template, request, flash, redirect, url_for
import google.generativeai as genai
import json
import os

# Configure the Gemini API key
# It's recommended to set this as an environment variable for security
genai.configure(api_key="YOUR_KEY") # Replace with your API key

app = Flask(__name__)
app.secret_key = os.urandom(24)

def prompt_engineering(complexity: int) -> str:
    """
    Generates the prompt for the Gemini model to create a quiz question.
    """
    # This function is identical to the one in your notebook
    return f"""
You are an expert Python teacher. A student selects a complexity level, and your task is to create a learning exercise.

### Instructions:
1. Generate the Python code that corresponds exactly to the chosen complexity level: {complexity}.
2. Calculate the **total number of iterations** executed by the code when run with the default or given `num` parameter.
3. Provide **three multiple-choice options** for the number of iterations:
   - One option must be the correct number.
   - Two options must be plausible but incorrect.
4. Return the answer **only in JSON format**, with the following structure:

{{
  "code": "Python code as a string",
  "choices": [int, int, int],
  "correct_choice": int
}}

### Notes:
- "code" should contain the full Python function(s) for the chosen complexity.
- "choices" should contain exactly three integer values.
- "correct_choice" must match one of the integers in "choices".
- Do not include any explanation or text outside the JSON.
- Focus only on the requested complexity level: {complexity}.
    """

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles the complexity selection and redirects to the quiz page.
    """
    if request.method == 'POST':
        try:
            complexity = int(request.form['complexity'])
            if 1 <= complexity <= 3:
                return redirect(url_for('quiz', complexity=complexity))
            else:
                flash('Please select a valid complexity level (1-3).')
        except ValueError:
            flash('Invalid input. Please enter a number.')
    return render_template('index.html')

@app.route('/quiz/<int:complexity>')
def quiz(complexity):
    """
    Generates and displays the quiz question for the selected complexity.
    """
    try:
        model_name = "gemini-1.5-flash"  # Or another suitable model
        prompt = prompt_engineering(complexity)
        response = genai.GenerativeModel(model_name).generate_content(prompt)
        
        # Clean the response to get a valid JSON
        cleaned_response = response.text.strip().replace("```json", "").replace("```", "").strip()
        quiz_data = json.loads(cleaned_response)
        
        return render_template('quiz.html', quiz=quiz_data, complexity=complexity)
    except Exception as e:
        flash(f'An error occurred while generating the quiz: {e}')
        return redirect(url_for('index'))

@app.route('/submit', methods=['POST'])
def submit():
    """
    Processes the user's answer and provides feedback.
    """
    try:
        user_answer = int(request.form['choice'])
        correct_answer = int(request.form['correct_choice'])
        complexity = int(request.form['complexity'])

        if user_answer == correct_answer:
            flash('Correct! Well done.', 'success')
        else:
            flash(f'Incorrect. The correct answer was {correct_answer}.', 'danger')
        
        return redirect(url_for('quiz', complexity=complexity))
    except (KeyError, ValueError):
        flash('Invalid submission. Please try again.', 'warning')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)