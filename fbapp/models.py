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
    def __init__(self, description):
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

    db.session.add(Content("في هدوءك .. ستكتشف انك كنت بداخل دوامه افكارك .. ستستنكر شئ : لماذا كنت قلق لهذه الدرجه ؟ هي ابسط بكثير مما تعتقد .   في الهدوء .. تشاهد ذاتك فالخوف قد صمت!"))
    db.session.add(Content("الشمس تشرق كل يوم. لكن كل شروق هو يحصل لأول مرة و لا يتكرر. فقط العقل هو من يرى التكرار. لكن كل شيء يحدث دائما لأول مرة. كل لحظة هي جديدة. إلا إذا اخترت أنت أن تضع فوقها فلتر من الماضي و التجارب السابقة."))
    db.session.add(Content("عندما نحرر أنفسنا من القصة الزائفة المتمثلة في الحاجة أن نكون مثاليين او جيدين بما فيه الكفاية ، فإننا نسمح بشكل طبيعي للآخرين بأن يكونوا ناقصين !"))
    db.session.add(Content("في تلك اللحظة عندما يمكنك أن تشكر نفسك على المكان الذي أنت فيه الآن، ستستدير، وستبدأ في التحرك مع تدفّق الرفاه، وستتوقف تلك الأحلام التي حلمت بها عن كونها أوهام. ستزهر وتصبح حقيقة."))
    db.session.add(Content("هناك متعة غريبة في تشبثنا بالألم ! فهو يُرضي حاجتنا اللاواعية في التخفيف من وطأة الشعور بالذنب من خلال العقاب"))
    db.session.add(Content("كل ما نراه في الخارج محتواه داخلنا ... حتى الاساءة من الاخر هي انعكاس لتأنيب داخلي غارق في العقل الباطني ... راقب علاقتك مع ذاتك قبل ان تبدأ الشروع في اي علاقة أخرى."))
    db.session.add(Content("كل ماخففت من التفكير ، كل ما أصبحت الحياة أجمل.. كثرة التفكير تعقد وتصعب وتضيق علينا الحياة. التوازن مطلب."))
    db.session.add(Content("إن الناس الذين يحملون الكثير من الكراهية يجدون أنهم يعيشون في عالم زاخر بالكراهية وأن هناك الكثير من الناس الذين يكرهونهم ويرون أن المواقف الخارجية والعالم كلهم ممتلئين بالكره إلا أن ما فشلوا في إدراكه هو أن هذا الموقف بأكمله من إنشائهم !"))
    db.session.add(Content("الناس من حولك ليسوا في حياتك ليجعلوك سعيدا، ولكنهم موجودون في حياتك ليجعلوك واعياً !"))
    db.session.add(Content("تفقد قدرتك على رؤيتة الأشياء على حقيقتها وكما هي الآن، حين تسمح لعقلك بالتدخل دائماً، عادي تحلل اذا كان هالشي يخدمك، لكن اسمح لنفسك برؤية الأمور على ما هي عليه قبلها."))
    db.session.add(Content("إنتقادك لكل شيء و خاصة لما لا يهمك يسرق من طاقتك دون أن تستفيد شيئا. دع الناس يعيشون كما يريدون حتى لو أخطأوا من وجهة نظرك فلكل تجربته."))
    



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