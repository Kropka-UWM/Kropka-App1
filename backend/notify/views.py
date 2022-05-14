"""Views file."""

# Create your views here.
# Django
from django.http import Http404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

# 3rd-party
from push_notifications.models import GCMDevice


class PushDemoView(TemplateView):
    """Push demo view."""

    template_name = 'demo/push_notify.html'


# class PushNavigatorView(TemplateView):
#     """Push navigator view."""
#
#     template_name = 'workers/navigatorPush.service.js'
#     content_type = 'application/javascript'


class FirebasePushView(TemplateView):
    """Push navigator view."""

    template_name = 'workers/firebase-messaging-sw.js'
    content_type = 'application/javascript'


@csrf_exempt
def register_push(request):  # noqa: D103
    if request.method != 'POST':
        raise Http404
    try:
        qs = GCMDevice.objects.filter(registration_id=request.POST['registration_id'])
        if not qs.exists():
            GCMDevice.objects.create(
                registration_id=request.POST['registration_id'],
                user=request.user,
                cloud_message_type='FCM',
            )
            return JsonResponse({'is_finished': True})
        else:
            qs.send_message('test')
    except BaseException as e:
        print(f'Register push error: {e}')
    raise Http404
