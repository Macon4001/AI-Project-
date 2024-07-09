import aiml
import nltk
# Create a new instance of the AIML interpreter
k = aiml.Kernel()

# Load the standard AIML file
k.learn("standard.aiml")

# Load a custom AIML file
k.learn("flstudio_categories.aiml")

# Start the main loop
while True:
    # Get the user's input
    user_input = input("You: ")
    
    # Get the bot's response
    bot_response = k.respond(user_input)
    
    # Print the bot's response
    print("Bot: " + bot_response)
