from django.shortcuts import render, redirect, get_object_or_404
from journal_oks.models import *
from journal_oks.forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io




def koff_coef_list(request):
    koff_coef = P1ComponentCompositionOfUnstableCondensate.objects.all()

    return render(request, 'journal_oks/forms/oks_p1/content.html', {'koff_coef': koff_coef})
 
 
