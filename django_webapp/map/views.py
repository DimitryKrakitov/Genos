from django.http import HttpResponse
from django.template import loader
from .models import Campus

# Create your views here.
def index(request):
    all_campus = Campus.objects.all()
    template =loader.get_template('map/index.html')
    context = {
        'all_campus': all_campus,
    }
    """html=''
    for campus in all_campus:
        url = '/map/' + str(campus.id) + '/'
        html += '<a href="' + url + '">' + campus.name + '</a><br>'
    """
    return HttpResponse(template.render(context,request))

def campus_show(request, campus_id):
    return HttpResponse("<h2>Details for Campus " + str(campus_id) + "</h2>")
