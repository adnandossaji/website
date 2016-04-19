from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter

@app.route("/")
def template_test():

    programming_languages = [
        ["devicons devicons-html5", "HTML", 99],
        ["devicons devicons-css3", "CSS", 85],
        ["devicons devicons-python", "Python", 75],
        ["devicons devicons-javascript", "JavaScript", 65],
        ["devicons devicons-java", "Java", 60],
        ["devicons devicons-swift", "Swift", 45],
        ["devicon devicon-c-plain", "C", 40],
        ["devicons devicons-php", "PHP", 35],
        ["devicons devicons-scala", "Scala", 30]
    ]

    softwares = [
        ["fa fa-file-word-o", "Word", 99],
        ["fa fa-file-powerpoint-o", "Powerpoint", 99],
        ["devicon devicon-photoshop-plain", "Photoshop", 95],
        ["devicons devicons-git", "Git", 92],
        ["devicons devicons-mysql", "SQL/MySQL", 89],
        ["devicon devicon-apache-plain", "Apache", 85],
        ["fa fa-file-excel-o", "Excel", 82],
        ["devicon devicon-illustrator-plain", "Illustrator", 75]
    ]

    spoken_languages = [
        ["", "English (native)", 99],
        ["", "Urdu", 45],
        ["", "Gujurati", 35],
        ["", "Arabic", 25],
    ]

    return render_template(
        'resume.html',
        my_string="FooBar",
        my_list=[18,19,20,21,22,23],
        title="",
        current_time=datetime.datetime.now(),
        programming_languages=programming_languages,
        softwares=softwares,
        spoken_languages=spoken_languages

    )

@app.route("/home")
def home():
    return render_template('template.html', my_string="Foo", 
        my_list=[6,7,8,9,10,11], title="Home", current_time=datetime.datetime.now())

@app.route("/about")
def about():
    return render_template('template.html', my_string="Bar", 
        my_list=[12,13,14,15,16,17], title="About", current_time=datetime.datetime.now())

@app.route("/contact")
def contact():
    return render_template('template.html', my_string="FooBar"
        , my_list=[18,19,20,21,22,23], title="Contact Us", current_time=datetime.datetime.now())

@app.route("/resume")
def resume():

    programming_languages = [
        ["devicons devicons-html5", "HTML", 99],
        ["devicons devicons-css3", "CSS", 85],
        ["devicons devicons-python", "Python", 75],
        ["devicons devicons-javascript", "JavaScript", 65],
        ["devicons devicons-java", "Java", 60],
        ["devicons devicons-swift", "Swift", 45],
        ["devicon devicon-c-plain", "C", 40],
        ["devicons devicons-php", "PHP", 35],
        ["devicons devicons-scala", "Scala", 30]
    ]

    softwares = [
        ["fa fa-file-word-o", "Word", 99],
        ["fa fa-file-powerpoint-o", "Powerpoint", 99],
        ["devicon devicon-photoshop-plain", "Photoshop", 95],
        ["devicons devicons-git", "Git", 92],
        ["devicons devicons-mysql", "SQL/MySQL", 89],
        ["devicon devicon-apache-plain", "Apache", 85],
        ["fa fa-file-excel-o", "Excel", 82],
        ["devicon devicon-illustrator-plain", "Illustrator", 75]
    ]

    spoken_languages = [
        ["", "English (native)", 99],
        ["", "Urdu", 45],
        ["", "Gujurati", 35],
        ["", "Arabic", 25],
    ]

    return render_template(
        'resume.html',
        my_string="FooBar",
        my_list=[18,19,20,21,22,23],
        title="",
        current_time=datetime.datetime.now(),
        programming_languages=programming_languages,
        softwares=softwares,
        spoken_languages=spoken_languages

    )


if __name__ == '__main__':
    app.run(host='local.adnandossaji.com', port=8000)
