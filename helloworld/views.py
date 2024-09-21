from django.http import JsonResponse
import random

MESSAGES = ['from Django', 'world!']
def get_message(request):
  return JsonResponse({"message": random.choice(MESSAGES)})