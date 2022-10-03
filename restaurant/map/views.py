from django.shortcuts import render
from django.views import generic
import folium
from .models import Restaurant


def index(request):
    m = folium.Map(location=[53.900, 27.550], zoom_start=11)
    for i in Restaurant.objects.all():
        text = folium.Html(
            '<a href="' + i.website + '"target="_blank">' + 'Сайт' + '</a>' + '</br>' + i.phone_number +
            '</br>' + i.address + '</br>' + '<a href="' +'/' + str(i.pk) +
            '"target="_blank">' + 'Подробно' + '</a>', script=True
        )
        popup = folium.Popup(text, max_width=4000)
        folium.Marker(location=[i.latitude, i.longitude], tooltip=i.name, popup=popup).add_to(m)
    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'index.html', context)


class DetailView(generic.DetailView):
    model = Restaurant
    template_name = 'detail.html'
