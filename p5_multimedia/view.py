from p5_multimedia import model
from flask import Flask, render_template, url_for, request, redirect, flash, render_template_string
from p5_multimedia import p5_multimedia_bp

#create a Flask instance
# app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']
popular= []

#connects default URL to a function
@p5_multimedia_bp.route('/', methods=['GET', 'POST'])
def index():
  if(request.method == 'POST'):
    form = request.form
    product = form['product']  
    open("./p5_multimedia/products.txt", "a").write("\n" + product)
    a = open("p5_multimedia/products.txt", "r").read()
    popular = a.split("\n")
    if(len(popular) > 7):
      popular.pop(0)
      seperator = '\n'
      newContent = seperator.join(popular)
      open("./p5_multimedia/products.txt", "w").write(newContent)
    return redirect("https://www.amazon.com/s?k=" + product +"&ref=nb_sb_noss")
  a = open("p5_multimedia/products.txt", "r").read()
  popular = a.split("\n")
  return render_template('p5_multimedia/home.html', projects=model.setup(), popular=popular)


@p5_multimedia_bp.route('/youtube/', methods=['GET', 'POST'])
def youtube():
  if(request.method == 'POST'):
    form = request.form
    link = form['link']
    if not(link.startswith("https://youtube.com/embed/")):
      
      return render_template_string('<h1>please enter a valid link<br><p>If you have a "www." make sure to remove it</p><iframe frameborder="0" width="666px" height="375px" src="https://owo.whats-th.is/ARRGFC3.gif"</iframe>')
    else:
      open("./p5_multimedia/youtube.txt", "a").write("\n" + link + '?controls=0')
  a = open("./p5_multimedia/youtube.txt", "r").read()
  links = a.split("\n")
  return render_template("p5_multimedia/youtube.html", projects=model.setup(), links=links)

  
@p5_multimedia_bp.route('/spotify/', methods=['GET', 'POST'])
def spotify():
  if(request.method == 'POST'):
    form = request.form
    link = form['link']
    if not(link.startswith("https://open.spotify.com/embed/")):
      return render_template_string("<h1>Please enter a valid spotify playlist url</h1><br><p>Did you add the /embed between /playlist/ and the playlist id?</p>")
      return
    else:
      open("./p5_multimedia/spotify.txt", "a").write("\n" +  link)
  a = open("./p5_multimedia/spotify.txt", "r").read()
  links = a.split("\n")
  return render_template("p5_multimedia/spotify.html", projects=model.setup(), links=links)


@p5_multimedia_bp.route('/flask/')
def flask():
    #Flask import uses Jinga to render HTML
    return render_template("fseries.html", projects=model.setup())


@p5_multimedia_bp.route('/hello/')
def hello():
    #Flask import uses Jinga to render HTML
    return render_template("hseries.html", projects=model.setup())


@p5_multimedia_bp.route('/template1/')
def testing():
    return render_template("template1.html", projects=model.setup())


@p5_multimedia_bp.route('/selfgrade/')
def selfgrade():
    return render_template("selfgrade.html", projects=model.setup())


@p5_multimedia_bp.route('/videos/')
def videos():
    return render_template('videos.html', projects=model.setup())


@p5_multimedia_bp.route('/products/')
def products():
  return render_template('products.html')




