from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('PowerOfLampFilamentInAnIncandescentBulb/',views.powerlamp,name="PowerOfLampFilamentInAnIncandescentBulb"),
    path('',views.powerlamp,name="PowerOfLampFilamentInAnIncandescentBulb"),]