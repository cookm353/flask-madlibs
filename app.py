from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route("/")
def story_form():
    return render_template("form.html", prompts=story.prompts,
        template = story.template)

if __name__ == "__main__":
    # app.run()
    print(story.prompts)