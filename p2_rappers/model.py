def aditis_video():
    name = "Aditi Akella"
    grade = "11th grade"
    about = "Hello! I am Aditi and I am a Junior at Del Norte. I love animals, travel, and science. This is my first year in Mr. M's class and I am learning so much about Python and html files! I look forward to learning more about computers and programming."
    contributions = "Contribution to the Flask Portfolio project: I created the about us page and formatted it. Along with Carter, I created a Navbar and added all the links. I also formatted the home page and added all the links to the projects, repl.its and resources. Then, I worked on creating the about San Diego Landmarks page. Lastly, I created the model.py file, passed data into aboutus.py through view.py, and created a Jinja template on the about us file."
    embed = "https://docs.google.com/document/d/16KCrGRWoCMhvJ_rCrNne9bVYG0nbg5ySihLXvRXlXuk/edit?usp=sharing"
    info = {"name": name, "grade": grade, "about": about, "contributions": contributions, "embed": embed}
    return info

def carters_video():
    name = "Carter Quartararo"
    grade = "11th grade"
    about = "Whats up! I'm Carter and this is a little about me. I'm a junior at Del Norte that loves to go surfing, hangout with friends. At Del Norte I play water polo which I love. I also love math and science, and now computer science with Mr.M. I am starting to learn a lot and I am becoming excited to code. I can't wait to learn so much more in the future."
    contributions = "Contribution to the Flask Portfolio project: I worked on the navbar and the app routes for the different links within our html project. At first this seemed like a tough task but with some help I was able to complete it."
    embed = "https://python-hello-series.jmort1021.repl.run"
    info = {"name": name, "grade": grade, "about": about, "contributions": contributions, "embed": embed}
    return info

def isais_video():
    name = "Yazhisai Rajaraman"
    grade = "11th grade"
    about = "Hello! I am Isai and I am an eleventh grader at Del Norte. I love reading, watching tv, and dance. This is my first time learning anything regarding Computer Science and it has been a very fun experience. I have learned different types of coding from basic Python fundamentals to .html. I hope to further improve from here."
    contributions = "Contribution to the Flask Portfolio project: I experimented a lot with how to add backgrounds. At first, I thought we could use ascii art for the background. However, I realized that .html tries to conserve as much space as possible so this wasn't a viable option. I inserted an image at the top of the website that fitted the aesthetics of the website and sized it to fit correctly. I also added a file Contents of Our Website that outlines everything in the website for users.Next I created almost a separate website in our main website that highlights different information about San Diego. In this, I added separate pages providing information about tourist spots,restaurants, landmarks, and more."
    embed = "https://python-hello-series.jmort1021.repl.run"
    info = {"name": name, "grade": grade, "about": about, "contributions": contributions, "embed": embed}
    return info

def mustafas_video():
    name = "Mustafa Sharaf"
    grade = "11th grade"
    about = "Hello everyone! My name is Mustafa Sharaf, I'm in 11th grade, and I go to Del Norte High School! This is my first time taking a coding class, besides taking coding classes in boot camps. I love learning about new types of code that makes code run faster. My favorite project has been the Rap Name Generator, it was fun to experiment with different types of code in order to display the options in the sub menus."
    contributions = "Contribution to the Flask Portfolio project:I have created and finished a new README.md file for the project,I have organized and cut down the code, and I will work on the comments in the code for users to get a better understanding of code."
    embed = "https://python-hello-series.jmort1021.repl.run"
    info = {"name": name, "grade": grade, "about": about, "contributions": contributions, "embed": embed}
    return info

def sophies_video():
    greeting= "Hi!"
    name = "Sophie Bulkin"
    grade = "11th grade"
    about = "Hello! I am Sophie and I am an eleventh grader at Del Norte. I took a  Computer Science class last year with Mr.M and it has been a very fun experience. I have learned different types of coding from basic Python fundamentals to .html. I hope to further improve from here. My main contribution has been to the about us page and I have worked on fixing the dropdown button."
    contributions = "Contribution to the Flask Portfolio project: I added all of the pictures in the website, worked on the Jinja with Aditi, and helped Carter with the dropdown menu. I also updated the readme file and helped Mustafa finish the about san diego page."
    embed = "https://docs.google.com/document/d/1RatYt0V-7duqtM0YuP8SuM_X90_fCG4qy2-H8HeBHvU/edit?usp=sharing"
    info = {"greeting": greeting, "name": name, "grade": grade, "about": about, "contributions": contributions, "embed": embed}
    return info

def journal():
    greeting="Here is my journal!"
    name= "Google Doc"
    about= "this is where I log my daily activites and accomplishments"
    contributions = "I contribute to this everyday because I add my activities"
    embed= "https://docs.google.com/document/d/1RatYt0V-7duqtM0YuP8SuM_X90_fCG4qy2-H8HeBHvU/edit?usp=sharing"
    info = {"greeting": greeting, "name": name, "about": about, "contributions": contributions, "embed": embed}
    return info

def alldata():
    return [aditis_video(), carters_video(), isais_video(), mustafas_video(), sophies_video(),journal()]
