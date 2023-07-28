
from django.shortcuts import render , HttpResponse ,redirect
import qrcode
import qrcode.image.svg

from io import BytesIO
from .models import Profile,add_ativity,add_data_all
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
import base64

def qrcode_g(request,id):
    id_str = str(id)
    get_ativity = add_ativity.objects.get(id=id)
    #ดึงข้อมูลuser มังนะ
    get_user = request.user.id
    mydata = Profile.objects.filter(user_id=get_user).values_list()
    getmydata = mydata[0]
    getmydata2 = getmydata[2]
    textlasc = "TEFTQw"
    datastuden = textlasc+' '+ str(getmydata2)+' '+id_str
    context = {}
    
    qr_image = qrcode.make(datastuden, box_size=15)
    qr_image_pil = qr_image.get_image()
    stream = BytesIO()
    qr_image_pil.save(stream, format='PNG')
    qr_image_data = stream.getvalue()
    qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
    context['qr_image_base64'] = qr_image_base64
    context['variable'] = get_ativity
    return render(request, 'index.html', context=context)


# หน้าแรก
def home(requset):
    return render(requset,"home.html")#category

#ลงทะเบียนเข้าใช้งาน
def register(request):
    if request.method == 'POST':
        usersname = request.POST['user_name']
        fname = request.POST['f_name']
        lname = request.POST['l_name']
        password = request.POST['password']
        repassword = request.POST['repassword']
        id_name = request.POST['id_name']
        fieldstudy = request.POST['fieldstudy'] 
        

        if usersname =="" or fname ==""  or password =="" or lname=="":
            messages.info(request,"ป้อนข้อมูลให้ครบถ้วน")
            return redirect('register')
        else:
            if User.objects.filter(username=usersname).exists():
                messages.info(request,"ชื่อผู้ใช้ถูกใช้ไปแล้ว")
                return redirect('register')
            else:
                if password == repassword:
                    user = User.objects.create_user(
                        username=usersname ,
                        first_name=fname,
                        password = password,
                        last_name=lname)
                    Profile = user.profile # because of signal and one2one relation
                    Profile.idstuden = id_name
                    Profile.fieldstudy = fieldstudy
                    Profile.save()
                    return redirect('loginuser')
                   
                else:
                    messages.info(request,"ยืนยันรหัสผ่านไม่ถูกต้อง")
                    return redirect('register')    
    else:
        return render(request,'register.html')


#ลงชื่อเข้าใช้
def loginuser(requset):
    if requset.method == 'POST':
        username = requset.POST['usersname']
        password = requset.POST['password']
        #LOGIN.objects.all()
        if username == "" or password == "":
            messages.info(requset,"ป้อนข้อมูลให้ครบถ้วน")
            return redirect('loginuser')
        else:
            user = authenticate(requset, username=username, password=password )
            if user is not None:
                login(requset, user)
                return redirect('home')
            else:
                messages.info(requset,"ข้อมูลไม่ถูกต้อง")
                return redirect('loginuser')

    else:
        return render(requset,"login.html")

#สร้างqrcode

    
    


#สแกน ตัวสแกนต้องมีเน็ต
def qrscan(requset):
    if requset.method == "POST":
        name = requset.POST["name"]
        if name == "":
            messages.info(requset,"ไม่มีข้อมูล")
            return  redirect('qrscan')
        else:
            split_data = name.split(" ")
            symbol = split_data [0]
            #การเข้ารหัส Base64Url TEFTQw=LASC
            if symbol =="TEFTQw":
                id_name_data = split_data [1]
                activity_data = split_data [2]

                if add_data_all.objects.filter(add_Id_studen = id_name_data,add_id_activity = activity_data).exists() :

                    messages.info(requset,"ข้อมูลนี้ถูกบันทึกไปเเล้ว")
                    return redirect('qrscan')
                else:
                    get_userdata = Profile.objects.filter(idstuden = id_name_data).values_list()
                    get_activity_data = add_ativity.objects.filter(id = activity_data ).values_list()
                    getid_pk = get_userdata[0][1]
                    get_userdatapk = User.objects.filter(id = getid_pk).values_list()
                    
                    get_user = get_userdatapk[0][4]
                    get_userf = get_userdatapk[0][5]
                    get_userl = get_userdatapk[0][6]

                    getid = get_userdata[0][2]
                    getfieldstudy = get_userdata[0][3]
                    getactivity = get_activity_data[0][1]
                    

                    f = add_data_all(
                        add_user_name = get_user,
                        add_Id_studen = getid,
                        add_f_name = get_userf,
                        add_l_name = get_userl,
                        add_fieldstudy = getfieldstudy,
                        add_activity = getactivity,
                        add_id_activity = activity_data
                    
                    )
                    f.save()
                    messages.info(requset,"บันทึกข้อมูลเรียบร้อย")
                    return  redirect('qrscan')
            else:
                messages.info(requset,"ข้อมูล qr code ไม่ถูกต้อง")
                return redirect('qrscan')
    else:
        return render(requset,"qr2.html")


def result_sd(requset):
    return HttpResponse("บันทึกข้อมูข้อมูล")

def test1(requset):
    return HttpResponse("ไม่ มีข้อมูล")

#กลอกข้อมูลการจัดกิจกรรม
def listname(requset):
    if requset.method == "POST":
        
        data_name = requset.POST["activity"]
        data_Date = requset.POST["day_data"]
        data_data = requset.POST["text_data"]

        if data_name == "" or data_Date == ""or data_data == "":
            messages.info(requset,"ป้อนข้อมูลให้ครบถ้วน")
            return redirect('listname')


        else:
            data_seve = add_ativity(
                activity_name = data_name,
                activity_Date = data_Date,
                activity_data = data_data,)
            data_seve.save()
            return render(requset,"check.html")
            
    else:
        return render(requset,"add-ativity.html")       
        

#หน้าแสดงข้อมูลรายการกิจกรรม
def listativity(requset):
    list_data = add_ativity.objects.all()
    return render(requset,"list-ativity.html",{"lists_data":list_data})


#-ข้อมูลของฉัน
def mydata(requset):
    getuser_md = requset.user.first_name
    getuser_2 = requset.user
    mydata1 = Profile.objects.filter(user = getuser_2).values_list()
    profileuser = list(mydata1[0])
    #print(profileuser[2])


    get_mydata = add_data_all.objects.filter(add_f_name = getuser_md)
    get_activity = add_ativity.objects.all()
    texticon = []
    #ส่วนตรวจสอบสถานะ
    for i in get_activity:
        a = add_data_all.objects.filter(add_f_name = getuser_md,add_activity = i)
        
       
        if not(a):
            texticon.append("fa fa-close")
    
        else:
            texticon.append("fa fa-check")

    mydatasactivity=zip(get_activity,texticon)
    return render(requset,"my_data.html",{"mydatas":get_mydata,"profileuser1":profileuser[2],"profileuser2":profileuser[3],"mydatasactivity":mydatasactivity})
    
   



def table(requset,id):
    getdata_at = add_data_all.objects.filter(add_id_activity = id)
    
    return render(requset,"table.html",{"getdata_at":getdata_at})

def datatabel(requset):
    list_data = add_ativity.objects.all()
    return render(requset,"datatabel.html",{"lists_data":list_data})
    


#def save_data(requset):
    #a = requset.user.first_name
    #print(a)
    #print("..........................................save_data")
    #return  redirect('listativity2')
    #return render(requset,"list-ativity copy.html")


def check(requset):
    return render(requset,"check.html")

def edituser(requset,id):
    blogedit = User.objects.get(id=id)
    editprofile = Profile.objects.get(user_id = id) 
    return render(requset,"editdata.html",{"blogedit":blogedit,"editprofile":editprofile})

def updetedata(request,id):
    if request.method == 'POST':
        upuser = User.objects.get(id=id)
        upprofile = Profile.objects.get(user_id = id) 
        #usersname = request.POST['user_name']
        fname = request.POST['f_name']
        lname = request.POST['l_name']
        #password = request.POST['password']
        #repassword = request.POST['repassword']
        id_name = request.POST['id_name']
        fieldstudy = request.POST['fieldstudy'] 

        #อัพเดท

        upuser.first_name = fname
        upuser.last_name = lname
            
        upprofile.idstuden = id_name
        upprofile.fieldstudy = fieldstudy
        upuser.save()
        upprofile.save()

        return redirect('mydata')
   