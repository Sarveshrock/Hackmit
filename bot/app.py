# app.py
from flask import Flask, render_template, request, jsonify
import google.generativeai as generativeai
from IPython.display import Markdown
import textwrap

app = Flask(__name__, template_folder='templates')

# Set your Google API key
GOOGLE_API_KEY = 'AIzaSyCGautKJUtA75NMHcSznE7-LB-ehY7UwDI'

# Configure GenAI with your API key
generativeai.configure(api_key=GOOGLE_API_KEY)

# Create a GenerativeModel object
model = generativeai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['input']
    
    # Generate text using the model
    response = model.generate_content(user_input)
    
    # Format the response as Markdown
    response_text = response.text
    
    return jsonify({'response': response_text})


def to_markdown(text):
    if isinstance(text, str):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    else:
        return text  # Return unchanged if not a string


if __name__ == '__main__':
    app.run(debug=True)
