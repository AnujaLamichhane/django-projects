from django.shortcuts import render
# from django.http import HttpResponse
from.forms import ContactForm,FeedbackForm

def feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        # process form.cleaned_data
        print(form.cleaned_data)
        form.save()
        return render(request, 'myform/thankyou.html')

    context = {
        "form":form
    }
    template_name = "myform/feedback.html"

    return render(request, template_name, context)


# Create your views here.
def index(request):
    # 
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # process form.cleaned_data
        print(form.cleaned_data)
        return render(request, 'myform/thankyou.html')

    context = {
        "form":form
    }
    template_name = "myform/forms.html"

    return render(request, template_name, context)
    #return HttpResponse("my forms are loading")
