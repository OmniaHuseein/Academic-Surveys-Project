from django.conf.urls import url
from django.urls import reverse_lazy

from .views import SurveyQuestionCreate, SurveyList, SurveyQuestionUpdate, SurveyRead, SurveyOption, SurveyReadPDF

app_name = 'survey'
urlpatterns = [
    url(r'^$', SurveyOption.as_view(), name="option"),
    url(r'^(?P<pk>\d+)$', SurveyRead.as_view(), name="read"),
    url(r'^list$', SurveyList.as_view(), name='list'),
    url(r'^create$', SurveyQuestionCreate.as_view(success_url=reverse_lazy('home:option')), name="create"),
    url(r'^(?P<pk>\d+)/update$', SurveyQuestionUpdate.as_view(success_url=reverse_lazy('home:option')), name="update"),
    url(r'^(?P<pk>\d+)/pdf$', SurveyReadPDF.as_view(), name="pdf"),
]
