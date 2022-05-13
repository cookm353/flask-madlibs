from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route("/")
def story_form():
    return render_template("form.html", prompts=story.prompts,
        template = story.template)

@app.route("/story")
def show_story():
    answers = {arg: request.args[arg] for arg in request.args}
    
    # print(keys)
    # print(vals)
    # print(request.args)
    # print(answers)
    print(answers)
    print(story.generate(answers))
    for arg in request.args:
        ...
        # print(arg)
        # print(request.args[arg])
        # print(request.args.values)
    return render_template("story.html", story=story.generate(answers))

if __name__ == "__main__":
    # app.run()
    print(story)