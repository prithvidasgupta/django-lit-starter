from django.http import FileResponse

# Create your views here.
def home(request):
  return FileResponse(open("web/static/index.html", 'rb'))