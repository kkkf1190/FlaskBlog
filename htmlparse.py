from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "img":
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == "src":
                        if(value.find('.jpg')>0):
                            self.links.append(value)