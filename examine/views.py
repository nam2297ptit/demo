# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Dictionary

import random
# Create your views here.
def tests(request):
	I = ["A", "B", "C", "D"]
	answer = random.choice(I)  
	numbers = Dictionary.objects.values_list('id', flat=True).order_by('id')
	Engsub = Dictionary.objects.values_list('Engsub', flat=True).order_by('Engsub')
	Vietsub = Dictionary.objects.values_list('Vietsub', flat=True).order_by('Vietsub')
	H = Dictionary.objects.values_list('id', 'Engsub','Vietsub')
	return render(request, 'examine/examine.html', {'H': H,'Engsub': Engsub,'answer': answer})