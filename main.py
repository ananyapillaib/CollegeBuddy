from flask import Flask, render_template, jsonify, request
import google.generativeai as genai

# Configure the Google Generative AI API
genai.configure(api_key="AIzaSyDNO9QlZWLkSC3ZZAcrYplHInj9YeT2qvQ")

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello_world():
    # Return the index.html template for the home page
    return render_template("index.html")

# Route for the chat page
@app.route('/chatpage')
def render_chat():
    # Return the chat.html template for the chat page
    return render_template("chat.html")

# Route to handle the chatbot conversation
@app.route('/chat', methods=['POST'])
def say_hello():
    print ("hello")
    user_query = request.json.get('message') 
    

     # This will get the 'message' field from the JSON body
    
    if not user_query:
        return jsonify({
            'response': "Sorry, no message received. Please try again.",
            'playMotivation': False
        })
    

    # Create an instance of the generative model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # System Instructions
    system_instructions = """You are a helpful and sarcastic chatbot. 
    Your responses should be concise and easy to understand."""


    # Combine system instructions and user prompt
    prompt = f"{system_instructions}\n\n{user_query}"

    # Get the response from the model
    try:
        response = model.generate_content(prompt)
        print("check point")
        print(response)
        # if hasattr(response, 'result') and response.result.candidates:
        #     # Extract the text from the first candidate's parts
        #     bot_response = response.result.candidates[0].content.parts[0].text
        # else:
        #     bot_response = "Sorry, I couldn't generate a response. Please try again."
        bot_response = response.candidates[0].content.parts[0].text

        # Return the bot's response as JSON
        print(bot_response)
        return jsonify({
            'response': bot_response,
            'playMotivation': 'motivation' in user_query.lower()  # Example: play motivational audio if 'motivation' in query
        })
    except Exception as e:
        return jsonify({
            'response': f"Error: {str(e)}",
            'playMotivation': False
        })

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, jsonify
import google.generativeai as genai

genai.configure(api_key="AIzaSyDNO9QlZWLkSC3ZZAcrYplHInj9YeT2qvQ")


# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/chatpage')
def render_chat():
    return render_template("chat.html")



@app.route('/chat', methods=['POST'])
def say_hello():
    # Create an instance of the generative model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # System Instructions
    system_instructions = """You are a helpful and friendly chatbot. 
    Your responses should be concise and easy to understand."""

    # Get the user's query (replace with actual input from the front-end)
    user_query = "I am bored"  # For testing purposes, you can replace this with actual input

    # Combine system instructions and user prompt
    prompt = f"{system_instructions}\n\n{user_query}"

    # Get the response from the model
    try:
        response = model.generate_content(prompt)


        # Ensure that the response is in a valid string format (assuming model returns a string)
       
        if isinstance(response, str):
            return jsonify({
                'response': response,
                'playMotivation': 'motivation' in user_query.lower()  # Example: condition to play motivation audio
            })
        else:
            return jsonify({
                'response': "Something went wrong. Please try again.",
                'playMotivation': False
            })
    except Exception as e:
        return jsonify({
            'response': f"Error: {str(e)}",
            'playMotivation': False
        })

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)