import fenixedu
import webapp2
from webapp2_extras import routes
from webapp2_extras import jinja2
from webapp2_extras import json
from string import Template
import mimetypes
from jinja2 import Environment, select_autoescape, FileSystemLoader

from bottle import Bottle, run, template, request, debug

app_bottle = Bottle()

config = fenixedu.FenixEduConfiguration.fromConfigFile('fenixedu.ini')

client = fenixedu.FenixEduClient(config)
url = client.get_authentication_url()
print (url)


# user = client.get_user_by_code('359af2750f20ba3d45b84cfae58ae052aea33e961eae55ac794103e345a75399be4c2a1a90eb07f877d67c21ade16addb7b5145f577c06928c04acef2324be6f')

# person = client.get_person(user)

# classes = client.get_person_classes_calendar(user)

# print(classes)

# print(person)

@app_bottle.route('/')
# example: http://localhost:8080/query?a=12
#         http://localhost:8080/query?add=12
#         http://localhost:8080/query
@app_bottle.route('/genos')
def query_function():
    print("ENTROU")
    if len(request.query) == 0:
        return "query should have add argument: example: <b>Example</b>"
    if "code" in request.query.keys():
        print(request.query["code"])
        return "just inserted %s to the array<br>" % request.query["code"]
    else:
        return "query should have add argument: example: <b>http://localhost:8080/query?a=12</b>"
        # for a in request.query:
        #	print (a, request.query[a])
        #	st.store(request.query[a])
        #	return "just inserted %s to the array<br>"%request.query[a]


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
        s = "<head><title>Authentication</title></head>"
        s += '<h1> Click the button to authenticate: </h1><a href="/joinfenix">ta da</a>'
        self.response.write(s)

        # url = client.get_authentication_url()
        # print(url)
        # self.response.write(url)


# def webapp_add_wsgi_middleware(app):
#    return webapp2.WSGIApplication([('/*', webapp2.RedirectHandler.new_factory('http://www.google.com', permanent=True))], debug=True)

class joinfenix(webapp2.RequestHandler):
    def get(self):
        # ip = self.request.remote_addr
        # log = Log()
        # log.ip_address = ip
        # log.put()
        # self.redirect("http://www.appurl.com")
        url = client.get_authentication_url()
        print(url)
        self.redirect("%s" % url)

        # url = client.get_authentication_url()
        # print(url)
        # s = "<head><title>Authentication</title></head>"
        # s += '<h1> Click the button to authenticate: </h1><a href="%s">ta da</a>' % url
        # self.response.write(s)


class acess_token(webapp2.RequestHandler):
    def get(self, code):
        print(str(code))
        user = client.get_user_by_code('token' % code)
        person = client.get_person(user)
        s = "<head><title>Genos</title></head>"
        s += '<h1> Authentication sucessful %s: </h1>' % person
        self.response.write(s)


app = webapp2.WSGIApplication([
    webapp2.Route(r'/authentication', authentication),
    webapp2.Route(r'/joinfenix', joinfenix),
    webapp2.Route(r'/genos/<code>', acess_token)

], debug=True)


def main():
    from paste import httpserver
    #httpserver.serve(app, host='127.0.0.1', port='8070')
    run(app_bottle, host='localhost', port=8070, reloader=True)


if __name__ == '__main__':
    main()
