from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "No text provided! Please provide text to analyze."

    # Pass the text to the function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the response contains an error
    if 'error' in response:
        return f"Error: {response['error']}"
    
    # return response

    # Extract the emotion scores from the response
    predictions = response.get('emotionPredictions', [])
    if predictions and 'emotion' in predictions[0]:
        emotions = predictions[0]['emotion']

        # Prepare the formatted response
        emotion_scores = ', '.join([f"'{emotion}': {score:.9f}" for emotion, score in emotions.items()])
        dominant_emotion = max(emotions, key=emotions.get)

        if dominant_emotion is None:
            return "Invalid text! Please try again!"

        # Return the formatted output
        return (f"For the given statement, the system response is {emotion_scores}. "
                f"The dominant emotion is {dominant_emotion}.")
    else:
        return "Unable to detect emotion. Please try with different text."


@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main application
    page over the Flask channel."""
    return render_template('index.html')


if __name__ == "__main__":
    """This function executes the Flask app and deploys it on localhost:5000."""
    app.run(host="0.0.0.0", port=5000)
