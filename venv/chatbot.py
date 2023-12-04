from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import csv

# Flask app setup
app = Flask(__name__)

# Create a ChatBot instance
bot = ChatBot('WeatherBot')

# Load chatbot data from a CSV file
def load_chatbot_data(file_path):
    conversations = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            conversations.append(row)
    return conversations

# Path to CSV file containing chatbot data
file_path = 'data_input_training/data.csv'
conversation_data = load_chatbot_data(file_path)

# Train the bot with conversation data from CSV
trainer = ListTrainer(bot)
for conversation in conversation_data:
    trainer.train(conversation)

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get bot responses
@app.route('/get_response', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = str(bot.get_response(user_input))
    return render_template('index.html', response=response)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

