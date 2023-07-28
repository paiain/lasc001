
from django.urls import path
from myapp.views import home, loginuser,register,qrscan,result_sd,listname,listativity,mydata, table,check,edituser,updetedata,datatabel,qrcode_g
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(home,login_url='/loginuser'), name='home' ),#หน้าหลัก
    path('loginuser/register', register, name='register' ),#หน้าลงทะเบียน
    path('loginuser/', loginuser, name='loginuser' ),#หน้าลงชื่อเข้าใช้
    path('qrscan/', qrscan, name='qrscan' ),#หน้าสแกน
    path('result_sd/', result_sd, name='result_sd' ),#ข้อมูลนักศึกษา
    #path('test/', test1, name='test1' ),
    path('listname/', listname, name='listname' ),path('check/', listname, name='check/listname' ),#
    path('listativity/', login_required(listativity,login_url='/loginuser'), name='listativity' ),#กิจกรรม
    #path('listativity2/', listativity2, name='listativity2' ),
    path('list/<int:id>', qrcode_g, name='list' ),#สร้างqrcode
    path('mydata/', login_required(mydata,login_url="/loginuser"), name='mydata' ),#หน้าข้อมูลของฉัน
    #path('save_data/', save_data, name='save_data' ),
    path('check/',check,name='check'),#
    path('edituser/<int:id>',edituser,name='edituser'),#ส่งidไปแก้ไขข้อมูล
    path('updetedata/<int:id>',updetedata,name='updetedata'),#อัพเดทข้อมูล
    path('datatabel/',datatabel,name='datatabel'),#ตารางการเข้าร่วม
    path('table/<int:id>', table, name='table' ),#ส่งidไปตาราง
    
]