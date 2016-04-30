from website import app
from flask import render_template, request, flash, session, url_for, redirect
from forms import ContactForm, SignupForm, SigninForm
from flask.ext.mail import Message, Mail
from models import *
import datetime

mail = Mail()

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter

@app.route('/')
def home():
  user = None

  if 'email' in session:
    user = User.query.filter_by(email = session['email']).first()

  #user = User.query.filter_by(email = session['email']).first()
  form = SigninForm()
  return render_template('home.html', form=form, user=user)

@app.route('/about')
def about():
  user = None

  if 'email' in session:
    user = User.query.filter_by(email = session['email']).first()

  form = SigninForm()
  return render_template('about.html', form=form, user=user)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  user = None

  if 'email' in session:
    user = User.query.filter_by(email = session['email']).first()

  contact_form = ContactForm()
  sign_in_form = SigninForm()


  if request.method == 'POST':
    if contact_form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', contact_form=contact_form, form=sign_in_form, user=user)
    else:
      msg = Message(contact_form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (contact_form.name.data, contact_form.email.data, contact_form.message.data)
      mail.send(msg)

      return render_template('contact.html', success=True, form=sign_in_form, user=user)

  elif request.method == 'GET':
    return render_template('contact.html', contact_form=contact_form, form=sign_in_form, user=user)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  user = None

  if 'email' in session:
    user = Users.query.filter_by(email = session['email']).first()
    return redirect(url_for('profile')) 
    
  form = SignupForm()
  
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form, user=user)
    else:
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
      
      session['email'] = newuser.email

      return redirect(url_for('profile'))
  
  elif request.method == 'GET':
    return render_template('signup.html', form=form, user=user)


@app.route("/resume")
def resume():
  user = None
  form = SigninForm()

  if 'email' not in session:
    return redirect(url_for('signin'))
  elif 'email' in session:
    user = User.query.filter_by(email = session['email']).first()

  professional_experience = [{
    "name": "AT&T",
    "url": "http://www.att.com",
    "title": "Big Data Technical Intern",
    "city": "Plano",
    "state": "Texas",
    "start_date": "June 2016",
    "end_date": "July 2016",
    "acheivements": [],
    "technologies": []
  }, {
    "name": "Panopta",
    "url": "http://www.panopta.org",
    "title": "Software Engineering Intern",
    "city": "Chicago",
    "state": "Illinois",
    "start_date": "July 2015",
    "end_date": "Present",
    "acheivements": [
      "Developed a tag management system organizing servers\' keyword usage into a dedicated view for Panopta\'s control panel to increase user experience (my.panopta.com)",
      "Built a performance indexing application that ranks and reports 400 popular domains by their uptime (index.panopta.com)",
      "Launched customer support platform for F.A.Q. currently in use by over 600 companies (answers.panopta.com)"
    ],
    "technologies": [
      "Git",
      "Python",
      "TurboGears",
      "Jinja2",
      "Bottle",
      "Flask",
      "HTML",
      "CSS",
      "JavaScript",
      "REST"
    ]
  },{
    "name": "Chicago Cubs",
    "url": "http://chicago.cubs.mlb.com/",
    "title": "Application Development Intern",
    "city": "Chicago",
    "state": "Illinois",
    "start_date": "June 2015",
    "end_date": "September 2015",
    "acheivements": [
      "Developed the first iteration of internal ticketing platform for over 250 employees to purchase complimentary and paid tickets",
      "Delivered an analytical recommendation on improving the Chicago Cubs waiting list from 52,000 to 72,000 members by collaborating within the cross-functional intern group"
    ],
    "technologies": [
      "Powerpoint",
      "Git",
      "Ext JS",
      "LDAP",
      "SSO",
      "SQL",
      "REST"
    ]
  },{
    "name": "Medtelligent",
    "url": "http://www.medtelligent.com",
    "title": "Web Application Development Intern",
    "city": "Chicago",
    "state": "Illinois",
    "start_date": "May 2014",
    "end_date": "July 2014",
    "acheivements": [
      "Built a real-time dashboard to improve work experience for 10 marketing, sales, and customer support employees"
    ],
    "technologies": [
      "Git",
      "Python",
      "HTML",
      "CSS",
      "Angular JS",
      "REST"
    ]
  }]

  volunteer_experience = [{
    "name": "Pakathon",
    "url": "http://www.pakathon.org",
    "title": "Global Team Web Developer & Chicago Pakathon Member",
    "city": "Chicago",
    "state": "Illinois",
    "start_date": "May 2015",
    "end_date": "Present",
    "acheivements": [
      "Developed branch website with Pakathon global technology leader to promote organization",
      "Collaborated on launching our first annual Chicago-based hackathon at University of Chicago on Oct. 4th, 2015"
    ],
    "technologies": [
      "Git",
      "Ruby",
      "Ruby on Rails"
    ]
  }]

  operating_systems = [
    "Linux",
    "Windows"
  ]

  activies_hobbies = [
    "Producing Electronic Music",
    "Painting",
    "Drawing",
    "Web Design",
    "Exploring/Traveling"
  ]

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
    form=form,
    user=user,
    my_string="FooBar",
    my_list=[18,19,20,21,22,23],
    title="",
    current_time=datetime.datetime.now(),
    professional_experience=professional_experience,
    volunteer_experience=volunteer_experience,
    programming_languages=programming_languages,
    softwares=softwares,
    operating_systems=operating_systems,
    activies_hobbies=activies_hobbies,
    spoken_languages=spoken_languages

  )

@app.route('/profile')
def profile():
  form = SigninForm()

  if 'email' not in session:
    return redirect(url_for('signin'))

  user = User.query.filter_by(email = session['email']).first()

  if user is None:
    return redirect(url_for('signin'))
  else:
    return render_template('profile.html', form=form, user=user)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    
  form = SigninForm()

  if 'email' in session:
    return redirect(url_for('profile')) 
      
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('profile'))
                
  elif request.method == 'GET':
    return render_template('signin.html', form=form)

@app.route('/signout')
def signout():
  user = None
  form = SigninForm()

  if 'email' not in session:
    return redirect(url_for('signin'))
  elif 'email' in session:
    user = User.query.filter_by(email = session['email']).first()
    
  session.pop('email', None)
  return redirect(url_for('home'))
