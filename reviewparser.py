from xml.dom.minidom import parse
import xml.dom.minidom, chardet

def parseit(file):
    rp = reviewparser()
    return rp.parse(file)

class reviewparser:

    def __init__(self):
        self.opinion="bom dia"
        self.thumbsup=0
        self.thumbsdown=0

    def parse(self, file):

        DOMTree = xml.dom.minidom.parse(file)
        review = DOMTree.documentElement
        self.opinion = review.getElementsByTagName("opinion")[0].childNodes[0].data
        self.thumbsup = review.getElementsByTagName("thumbsUp")[0].getAttribute("value")
        self.thumbsdown = review.getElementsByTagName("thumbsDown")[0].getAttribute("value")

        return self