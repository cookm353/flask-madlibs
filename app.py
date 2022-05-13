from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route("/form")
def story_form():
    return render_template("form.html", story=story)

if __name__ == "__main__":
    app.run()
    # print(story.prompts)