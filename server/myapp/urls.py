from django.urls import path

from myapp import views

app_name = 'myapp'
urlpatterns = [
    # api
    path('admin/overview/count', views.admin.overview.count),
    path('admin/overview/sysInfo', views.admin.overview.sysInfo),
    path('admin/family/list', views.admin.family.list_api),
    path('admin/family/create', views.admin.family.create),
    path('admin/family/update', views.admin.family.update),
    path('admin/family/delete', views.admin.family.delete),
    path('admin/medical/list', views.admin.medical.list_api),
    path('admin/medical/create', views.admin.medical.create),
    path('admin/medical/update', views.admin.medical.update),
    path('admin/medical/delete', views.admin.medical.delete),
    path('admin/worker/list', views.admin.worker.list_api),
    path('admin/worker/create', views.admin.worker.create),
    path('admin/worker/update', views.admin.worker.update),
    path('admin/worker/delete', views.admin.worker.delete),
    path('admin/thing/list', views.admin.thing.list_api),
    path('admin/thing/detail', views.admin.thing.detail),
    path('admin/thing/create', views.admin.thing.create),
    path('admin/thing/update', views.admin.thing.update),
    path('admin/thing/delete', views.admin.thing.delete),
    path('admin/classification/list', views.admin.classification.list_api),
    path('admin/classification/create', views.admin.classification.create),
    path('admin/classification/update', views.admin.classification.update),
    path('admin/classification/delete', views.admin.classification.delete),
    path('admin/tag/list', views.admin.tag.list_api),
    path('admin/tag/create', views.admin.tag.create),
    path('admin/tag/update', views.admin.tag.update),
    path('admin/tag/delete', views.admin.tag.delete),
    path('admin/banner/list', views.admin.banner.list_api),
    path('admin/banner/create', views.admin.banner.create),
    path('admin/banner/update', views.admin.banner.update),
    path('admin/banner/delete', views.admin.banner.delete),
    path('admin/notice/list', views.admin.notice.list_api),
    path('admin/notice/create', views.admin.notice.create),
    path('admin/notice/update', views.admin.notice.update),
    path('admin/notice/delete', views.admin.notice.delete),
    path('admin/loginLog/list', views.admin.loginLog.list_api),
    path('admin/loginLog/create', views.admin.loginLog.create),
    path('admin/loginLog/update', views.admin.loginLog.update),
    path('admin/loginLog/delete', views.admin.loginLog.delete),
    path('admin/opLog/list', views.admin.opLog.list_api),
    path('admin/errorLog/list', views.admin.errorLog.list_api),
    path('admin/user/list', views.admin.user.list_api),
    path('admin/user/create', views.admin.user.create),
    path('admin/user/update', views.admin.user.update),
    path('admin/user/updatePwd', views.admin.user.updatePwd),
    path('admin/user/delete', views.admin.user.delete),
    path('admin/user/info', views.admin.user.info),
    path('admin/adminLogin', views.admin.user.admin_login),


]
