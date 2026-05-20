from flask import Flask, render_template, request
#used to import groq api model
from groq import Groq     

# it  Create Flask application
app = Flask(__name__)

# greq is an AI models like gemini and let users create api key,it creates unique key for each user ....
client = Groq(
    api_key="your_api_key_here......"   #generate an groq api or gemini and paste here also make change in model name if using gemini as its groq based .......
)

# Create route(home page),( GET -> when page first opens) ,( POST -> when user submits message form)
@app.route("/", methods=["GET", "POST"])
def home():

    reply = ""  # it stores ai response


    if request.method == "POST":       # Check if form is submitted using POST method

        # Get message from input box
        user_message = request.form.get("message")

        try:

            # Send message to AI
            chat_completion = client.chat.completions.create(

                messages=[
                    {
                        "role": "user",
                        "content": user_message,
                    }
                ],

                model="llama-3.3-70b-versatile"

            )

            # Store AI reply
            reply = chat_completion.choices[0].message.content

        except Exception as e:

            reply = str(e)

    return render_template("index.html", reply=reply)

# Run app
if __name__ == "__main__":
    app.run(debug=True)