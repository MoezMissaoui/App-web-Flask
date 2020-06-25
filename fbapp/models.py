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
    description = db.Column(db.String(1000000), nullable=False)
    def __init__(self, description, gender):
        self.description = description


class Colors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(1000000), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    def __init__(self, color, gender):
        self.color = color
        self.gender = gender



def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("في هدوءك .. ستكتشف انك كنت بداخل دوامه افكارك .. ستستنكر شئ : لماذا كنت قلق لهذه الدرجه ؟ هي ابسط بكثير مما تعتقد في الهدوء .. تشاهد ذاتك فالخوف قد صمت!", Gender['male']))

    db.session.add(Content("The youth are not just our future, they are our present. How do we create space for them?", Gender['female']))



    db.session.add(Colors("#6633CC", Gender['male']))
    db.session.add(Colors("#666666", Gender['male']))
    db.session.add(Colors("#666699", Gender['male']))
    db.session.add(Colors("#6666CC", Gender['male']))
    db.session.add(Colors("#999966", Gender['male']))
    db.session.add(Colors("#999999", Gender['male']))
    db.session.add(Colors("#0099CC", Gender['male']))
    db.session.add(Colors("#003366", Gender['male']))
    db.session.add(Colors("#607D8B", Gender['male']))
    db.session.add(Colors("#6E2C00", Gender['male']))
    db.session.add(Colors("#7B241C", Gender['male']))
    db.session.add(Colors("#515A5A", Gender['male']))
    db.session.add(Colors("#566573", Gender['male']))
    db.session.add(Colors("#145A32", Gender['male']))
    db.session.add(Colors("#1B4F72", Gender['male']))
    db.session.add(Colors("#512E5F", Gender['male']))
    db.session.add(Colors("#0E6251", Gender['male']))
    db.session.add(Colors("#7E5109", Gender['male']))
    db.session.add(Colors("#7E5109", Gender['male']))
    db.session.add(Colors("#273746", Gender['male']))
    db.session.add(Colors("#4D5656", Gender['male']))
    db.session.add(Colors("#212121", Gender['male']))
    db.session.add(Colors("#17202A", Gender['male']))
    db.session.add(Colors("#1C2833", Gender['male']))


    db.session.add(Colors("#CC0099", Gender['female']))
    db.session.add(Colors("#BB8FCE", Gender['female']))
    db.session.add(Colors("#E91E63", Gender['female']))
    db.session.add(Colors("#E91E63", Gender['female']))
    db.session.add(Colors("#FFFF66", Gender['female']))
    db.session.add(Colors("#00CC99", Gender['female']))
    db.session.add(Colors("#FF0066", Gender['female']))
    db.session.add(Colors("#0288D1", Gender['female']))
    db.session.add(Colors("#0277BD", Gender['female']))
    db.session.add(Colors("#00FF33", Gender['female']))
    db.session.add(Colors("#CCFF00", Gender['female']))
    db.session.add(Colors("#FF99FF", Gender['female']))
    db.session.add(Colors("#CC99FF", Gender['female']))
    db.session.add(Colors("#FF99CC", Gender['female']))
    db.session.add(Colors("#FF66CC", Gender['female']))
    db.session.add(Colors("#CC3399", Gender['female']))
    db.session.add(Colors("#990099", Gender['female']))
    db.session.add(Colors("#FF0033", Gender['female']))
    db.session.add(Colors("#FF0066", Gender['female']))
    db.session.add(Colors("#FF0099", Gender['female']))
    db.session.add(Colors("#FF3300", Gender['female']))
    db.session.add(Colors("#CC0000", Gender['female']))
    db.session.add(Colors("#FF33CC", Gender['female']))
    db.session.add(Colors("#FF6699", Gender['female']))
    db.session.add(Colors("#FF9999", Gender['female']))
    db.session.add(Colors("#CC6699", Gender['female']))





    db.session.commit()
    lg.warning('Database initialized!')