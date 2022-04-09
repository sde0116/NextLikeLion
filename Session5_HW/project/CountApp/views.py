from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request,'count.html')


def result(request):
    text = request.POST['text']
    word = len(text.split())
    total_len = len(text)
    no_blank_len = len(text.replace(' ',''))
    return render(request,'result.html', {
        'text': text,
        'total_lens': total_len,
        'no_blank_lens': no_blank_len,
        'words': word,
        })