from django.shortcuts import render
from .models import MenuList,mainmenu
from .serializers import menuserializer,submenuserializer
from django.db.models import Avg, Count, Min, Sum

# Create your views here.

def dynamicmenu(request):
    
    try:
        
        menuList = MenuList.menulist_objects.values('menuname').order_by('MenuType').annotate(Count('menuname'))
        submenuList = MenuList.menulist_objects.all().filter(id__in=[1,2,3,4,5,6,7,8,9,10])
        mainmenu = menuserializer(menuList,many=True)
        data = mainmenu.data
        #print(data)
        request.session['mainM'] = data
        
        submenudata = submenuserializer(submenuList,many=True)
        subdata = submenudata.data
        #print(subdata)
        request.session['submenu'] = subdata
        return render(request, 'Main/index.html', {})
    except Exception as identifier:
        return render(request, 'Main/index.html', {})
    
    