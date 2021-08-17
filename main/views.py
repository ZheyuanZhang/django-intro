from django.shortcuts import render
from django import forms
import csv
from datetime import datetime

# Create your views here.

def index(request):
  if request.method == 'POST':
    now = datetime.now()
    context = {
      'name': request.POST['name'],
      'email': request.POST['email'],
    }
    with open('submissions.csv', 'a', newline='') as csvfile:
      spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      spamwriter.writerow([context['name'], context['email'], 'Submitted', now.strftime("%d/%m/%Y %H:%M:%S")])
    return render(request, 'thanks.html', context)
  context = {
    'results': [
    ]
  }
  with open('submissions.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
      context['results'].append({'name': row[0], 'email': row[1], 'status': row[2], 'time': row[3]})
  return render(request, 'index.html', context)
