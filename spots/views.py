from django.shortcuts import render, redirect

from spots.forms import AddMusicForm

# Create your views here.

from .models import Album, Musical


def home(request):

    music = Musical.objects.all()
    music_list = list(Musical.objects.all().values())

    context = {'music': music, 'music_list': music_list, }

    return render(request, 'spots/home.html', context)


def addMusic(request):

    form = AddMusicForm()

    # if request.POST:
    #     form = AddMusicForm(request.POST, request.FILES)

    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         album = form.cleaned_data.get('album')
    #         if album:
    #             music_album = Album.objects.get_or_create(name=album)
    #             print(music_album)
    #             instance.album = music_album[0]
    #             instance.save()
    #             return redirect("spots:home")
    #         else:
    #             instance.save()
    #             return redirect("spots:home")

    #     else:
    #         print("no", form.data)

    context = {'form': form}

    return render(request, 'spots/addPage.html', context)
