from django.http import HttpResponse


def index(request):
    return HttpResponse("Patrzysz na index glosowania.")

def detail(request, question_id):
	return HttpResponse("Patrzysz na pytanie %s." % question_id)

def results(request, question_id):
	response = "Patrzysz na pytanie %s."
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("Glosujesz na pytanie %s." % question_id)
