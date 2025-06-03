from django.shortcuts import render
from.models import Workshop,Member

def workshop_list(request):
    """
    this returns workshp list
    """

    template_name = "workshop/workshop_list.html"
    context = {
        "title":"Workshop List",
        "workshops":Workshop.objects.all(),
        "members":Member.objects.all(),
        #select all from workshop

    }
    return render(request, template_name, context)
def workshop_detail(request, id):
    #      """
    # this method renders single workshop object
    # """

    template_name="workshop/workshop_detail.html",
     #select all from workshop where id=id
     # .get() returns single object
     # .filter() returns multiple oblect
     # select* from workshop whre name_icontains="äbc"
     # .all() returns all
    workshop = Workshop.objects.get(id=id)
    members = Member.objects.filter(workshops=workshop)
    # filtered_obj = Workshops.objects.filter(id=id).first()

    context = {
        "workshop": workshop,
        "members": members
        # "filtered_obj": filtered_obj

    }
    return render(request, template_name, context)



# Create your views here.


# def member_list(request):
#     """
#     this returns workshp list
#     """

#     template_name = "workshop/member_list.html"
#     context = {
#         "title":"Workshop List",
#         "workshops":Workshop.objects.all(),
#         "members":Member.objects.all(),
#         #select all from workshop

#     }
#     return render(request, template_name, context)
# def member_detail(request, id):
#     #      """
#     # this method renders single workshop object
#     # """

#     template_name="workshop/member_detail.html",
#      #select all from workshop where id=id
#      # .get() returns single object
#      # .filter() returns multiple oblect
#      # select* from workshop whre name_icontains="äbc"
#      # .all() returns all
#     workshop = Workshop.objects.get(id=id)
#     # filtered_obj = Workshops.objects.filter(id=id).first()

#     context = {
#         "workshop": workshop,
#         # "filtered_obj": filtered_obj

#     }
#     return render(request, template_name)
