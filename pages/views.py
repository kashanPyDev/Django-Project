# from django.shortcuts import render

# Create your views here.
# # pages/views.py
# from django.shortcuts import render

# def home_page_view(request):
#     context = {  # new
#         "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
#         "greeting": "THAnk you FOR visitING.",
#     }
#     return render(request, "home.html", context)


# pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView  # new

# def home_page_view(request):
#     context = {
#         "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
#         "greeting": "THAnk you FOR visitING.",
#     }
#     return render(request, "home.html", context)

class baseview(TemplateView):  # new
    template_name = "base.html"

class homepageview(TemplateView):  # new
    template_name = "home.html"

class aboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "kashan shafique"  # new
        context["age"] = "63"  # new
        return context
    
#    def get_context_data(self, **kwargs):  # new
#         context = super().get_context_data(**kwargs)
#         context["address"] = "Azad Chaiwala Institute Rawalpindi"
#         context[""] = "555-555-5555"
#         return context



