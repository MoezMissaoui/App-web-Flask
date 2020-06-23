from flask_sqlalchemy import SQLAlchemy
import logging as lg
import enum

from .views import app
# Create database connection object
db = SQLAlchemy(app)

class Gender(enum.Enum):
    female = 0
    male = 1
    other = 2

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("You can sulk and be depressed about getting older, but what's worse than another birthday? Not having one.", Gender['male']))
    db.session.add(Content("Anyone can be confident with a full head of hair. But a confident bald man--there's your diamond in the rough.", Gender['male']))
    db.session.add(Content("Either write something worth reading or do something worth writing.", Gender['male']))
    db.session.add(Content("That's the way to live – around people who care. It may be a tough ride, but something is going to come out of it.", Gender['male']))
    db.session.add(Content("Clear communication. Respect. A lot of laughter. And a lot of orgasms. That's what makes a marriage work.", Gender['male']))
    db.session.add(Content("Clear communication. Respect. A lot of laughter. And a lot of orgasms. That's what makes a marriage work.", Gender['male']))
    db.session.add(Content("Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do, so go explore, dream, discover.", Gender['male']))
    db.session.add(Content("You've got to have something to retire to. Something you always wanted to do but your job prevented it.", Gender['male']))

    db.session.add(Content("The youth are not just our future, they are our present. How do we create space for them?", Gender['female']))
    db.session.add(Content("At the end of each day, I like to ask myself, ‘What did you learn today?’ If I have answers, then that day has been successful.", Gender['female']))
    db.session.add(Content("I think you have to be honest with yourself about attainable goals and take the time to acknowledge when you’re putting too much pressure on yourself. Try to be self-aware enough to determine whether self-applied pressure is contributing to your unhappiness.", Gender['female']))
    db.session.add(Content("Of course I have flaws I’m self-conscious about, but you learn to live with what you have been handed in life and count your blessings. If I had to live my life over, I would start at age 40.", Gender['female']))
    db.session.add(Content("I used to feel compelled to prove a point. Now I’m comfortable being solitary in an opinion.", Gender['female']))
    db.session.add(Content("The minute that every single thing is perfect, you’ve lost your sexuality, as far as I’m concerned. Where’s the juice?", Gender['female']))
    db.session.add(Content("There’s a balance of being comfortable, of having enough money to live on and then just having a good time. You’ve got to balance. You’ve got to find time to play. You gotta have a little life, a little fun. Find your soul.", Gender['female']))
    db.session.add(Content("The world needs whatever you are into. Whatever you’re obsessed with, there is someone else out there who needs that.", Gender['female']))

    db.session.commit()
    lg.warning('Database initialized!')