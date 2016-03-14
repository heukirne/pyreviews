from xml.dom.minidom import parse
import xml.dom.minidom
from unidecode import unidecode

def parseit(file):
    rp = reviewparser()
    return rp.parse(file)

class reviewparser:

    def __init__(self):
        self.opinion=""
        self.thumbsup=0
        self.thumbsdown=0
        self.stars=0
        self.user=""
        self.category=""
        self.evaluation_date=""
        self.recommends=""

    def parse(self, file):

        DOMTree = xml.dom.minidom.parse(file)
        review = DOMTree.documentElement
        self.opinion = review.getElementsByTagName("opinion")[0].childNodes[0].data
        self.thumbsup = review.getElementsByTagName("thumbsUp")[0].getAttribute("value")
        self.thumbsdown = review.getElementsByTagName("thumbsDown")[0].getAttribute("value")
        self.stars = review.getElementsByTagName("stars")[0].getAttribute("value")
        self.user = unidecode(review.getElementsByTagName("user")[0].getAttribute("value"))
        #remover caracteres nao-letra como > ,
        self.category = unidecode(review.getElementsByTagName("category")[0].getAttribute("value"))
        self.evaluation_date = review.getElementsByTagName("evaluation_date")[0].getAttribute("value")
        self.recommends = review.getElementsByTagName("recommends")[0].getAttribute("value")

        return self