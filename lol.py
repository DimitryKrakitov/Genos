import fenixedu
import webapp2
from webapp2_extras import routes
from webapp2_extras import jinja2
from webapp2_extras import json
from string import Template
import mimetypes
from jinja2 import Environment, select_autoescape, FileSystemLoader



config = fenixedu.FenixEduConfiguration.fromConfigFile('fenixedu.ini')

client = fenixedu.FenixEduClient(config)
url = client.get_authentication_url()
print (url)

user = client.get_user_by_code('359af2750f20ba3d45b84cfae58ae052aea33e961eae55ac794103e345a75399be4c2a1a90eb07f877d67c21ade16addb7b5145f577c06928c04acef2324be6f')

person = client.get_person(user)

classes = client.get_person_classes_calendar(user)

print(classes)




print(person)

env = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=select_autoescape(['html', 'xml', 'json'])
)

def sendFile(response, FileName):
    response.headers.add_header('Content-Type', mimetypes.guess_type(FileName)[0])
    f = open(FileName, 'r')
    response.write(f.read())
    f.close()


class authentication(webapp2.RequestHandler):
    def get(self):
        url = client.get_authentication_url()
        print(url)
        s = "<head><title>Authentication</title></head>"
        s += '<h1> Click the button to authenticate: </h1><a href="%s">ta da</a>' % url
        self.response.write(s)

        #url = client.get_authentication_url()
        #print(url)
        #self.response.write(url)


app = webapp2.WSGIApplication([
    webapp2.Route(r'/authentication', authentication),

], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8070')


if __name__ == '__main__':
    main()
