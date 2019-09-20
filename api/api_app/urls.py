from django.urls import path
from api_app import views

urlpatterns = [
    path('ip',views.ip),
    path("host",views.host),
    path("machine_platform",views.machine_platform),
    path("cpu",views.cpu),
    path("vmem",views.vmem),
    path("os_information",views.os_information),
    path("disk_storage",views.disk_storage),
    path("Netstat_info",views.Netstat_info),
    path("process_running",views.process_running),
    path("device_mount",views.device_mount),

    
]
