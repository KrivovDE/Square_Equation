import math

from django.shortcuts import render


def start(request):
    return render(request, 'start.html')


def finish(request):
    a = float(request.GET.get('a'))
    b = float(request.GET.get('b'))
    c = float(request.GET.get('c'))

    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return render(request, 'finish.html', {'a': a, 'b': b, 'c': c, 'D': D, 'x1': x1, 'x2': x2})
    elif D == 0:
        x3 = (-b + math.sqrt(D)) / (2 * a)
        return render(request, 'finish.html', {'a': a, 'b': b, 'c': c, 'D': D, 'x3': x3})
    else:
        x4 = 'Уравнение не имеет решений'
        return render(request, 'finish.html', {'a': a, 'b': b, 'c': c, 'D': D, 'x4': x4})

