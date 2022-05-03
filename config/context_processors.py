from .models import AdminBase


def admin_data(request):
    dic_data = AdminBase.objects.first()
    context = {
        'dic_data': dic_data,
    }
    return context
