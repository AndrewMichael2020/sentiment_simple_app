from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sent_analyze", methods=["GET", "POST"])
def sent_analyze():
    text_to_analyze = request.args.get('textToAnalyze') or request.form.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']
    if not label:
        return "Invalid input! Try again."
    else:
        # Safely split label if possible
        sentiment = label.split('_')[1] if '_' in label else label
        return f"The given text has been identified as {sentiment} with a score of {score}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
