from django.shortcuts import render
from .forms import SsForm

def post_list(request):
    return render(request, 'stady/post_list.html', {})

def add(request):
    bbf = SsForm()
    context = {'form': bbf}
    return render (request, 'stady/post_list.html', context)

def add_save(request):
    bbf = BbForm(request.POST)
    if bbd.is_valid():
        bbf.save()
        return HttpResponseDedirect (reverse('by_rubric',
                        kwargs = {'rubric_id': bbf.cleaned['rubric'].pk}))
    else:
        context = {'form': bbf}
        return render (request, 'stady/post_list.html')
