import random
import math
import os
from kivy.app import App
import kivy
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty, ListProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import ThreeLineAvatarListItem
from kivymd.uix.list import ImageLeftWidget
from kivymd.uix.list import ThreeLineListItem
import mysql.connector as sqltor
from fpdf import FPDF, HTMLMixin
from kivy.uix.widget import Widget
from datetime import datetime
import smtplib
import yagmail
from typing import Union
from kivy.lang import Builder
from firebase import firebase
from kivy.uix.screenmanager import NoTransition
from kivymd.uix.textfield import MDTextField
from fpdf.enums import XPos, YPos
from kivymd.uix.list import OneLineListItem
from kivy.core.window import Window
Window.size = (400, 600)

try:
    firebase=firebase.FirebaseApplication("https://anusav-technology-default-rtdb.asia-southeast1.firebasedatabase.app")
    result=firebase.get("/room_rent_khata",None)
    mycon=sqltor.connect(host=result.get("host"),port=result.get("port") ,user=result.get("user"),password=result.get("password"),database=result.get("database"))
    mycursor = mycon.cursor()
    err=1
except Exception as e:
    try:
        err = 0
        mycon=sqltor.connect(host="localhost",port="3306" ,user="root",password="Kumar4285@",database="room_rent_khata")
        mycursor = mycon.cursor()
    except Exception as e:
        print(e)
class CheckItem(MDBoxLayout):
    text = StringProperty()
    group = StringProperty()
    def checkbox_click(self, instance, value):
        if value is True:
            print("Checkbox Checked")
            check_out=1
        else:
            print("Checkbox Unchecked")
            check_out=0
class LineRectangle(Widget):
    pass
class Content(BoxLayout):
    pass

class MyContentComunes(BoxLayout, Screen):
    pass
class ContentNavigationDrawer(MDBoxLayout):
    pass
class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty()

class DrawerList(MDList,ThemableBehavior):
    def set_color_item(self, instance_item):
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
            break            
        instance_item.text_color = self.theme_cls.primary_color
class Room_Rent_Khata(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    def build(self):
        kv = Builder.load_file("main.kv")          
        kv1 = Builder.load_file("log_sucess.kv")
        kv2 = Builder.load_file("myrenter.kv")
        kv3 = Builder.load_file("addrenter.kv")
        kv4 =Builder.load_file("modifyrenter.kv")
        kv5 =Builder.load_file("searchrenter.kv")
        kv6 =Builder.load_file("deleterenter.kv")
        kv7 =Builder.load_file("edit_profil.kv")
        kv8 =Builder.load_file("payment.kv")
        kv9 =Builder.load_file("scan.kv")
        kv10 =Builder.load_file("renterdet.kv")
        kv11 =Builder.load_file("renter.kv")
        kv12 =Builder.load_file("sign_up.kv")
        kv13 =Builder.load_file("pay.kv")
        kv14 =Builder.load_file("about_us.kv")
        kv15 =Builder.load_file("reminder.kv")
        kv16 =Builder.load_file("edit_modify.kv")
        kv17 =Builder.load_file("help_sup.kv")
        kv18 =Builder.load_file("setting.kv")
        kv19 =Builder.load_file("forget.kv")
        kv20 =Builder.load_file("addrenternxt.kv")
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.primary_palette ="Teal"
        screen_manager.add_widget(kv)
        screen_manager.add_widget(kv1)
        screen_manager.add_widget(kv2)
        screen_manager.add_widget(kv3)
        screen_manager.add_widget(kv4)
        screen_manager.add_widget(kv5)
        screen_manager.add_widget(kv6)
        screen_manager.add_widget(kv7)
        screen_manager.add_widget(kv8)
        screen_manager.add_widget(kv9)
        screen_manager.add_widget(kv10)
        screen_manager.add_widget(kv11)
        screen_manager.add_widget(kv12)
        screen_manager.add_widget(kv13)
        screen_manager.add_widget(kv14)
        screen_manager.add_widget(kv15)
        screen_manager.add_widget(kv16)
        screen_manager.add_widget(kv17)
        screen_manager.add_widget(kv18)
        screen_manager.add_widget(kv19)
        screen_manager.add_widget(kv20)
        return screen_manager
    def on_start(self):
        screen_manager.current="MainScreen" 
        if err==0:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = "Please check your internet connection !",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    
            
    def sign_in(self):
        screen_manager.current="Sign_Up"
        ScreenManager(transition=NoTransition())
    
    def back_home_in(self,events):
        self.dialog.dismiss()
    def back2_home_in(self):
        self.dialog.dismiss()
        screen_manager.current="MainScreen"
    def back_sign_in(self):
        screen_manager.current="MainScreen"
    def help_st(self):
        screen_manager.current="help_supp"
    def for_log_in(self):
        try:
            forgt1=screen_manager.get_screen('ForgetScreen').ids.username_id_fiels.text
            forgt2=screen_manager.get_screen('ForgetScreen').ids.enter_cap.text
            if forgt1==forgt2=="":
                cancel_btn_username_dialogue = MDFlatButton(text='Try Again',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "User Id & Capta Cant be Empty",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            elif forgt2!=self.OTP:
                cancel_btn_username_dialogue = MDFlatButton(text='Try Again',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Capta Doesnot Match",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            
            else:
                exeqq="SELECT * FROM landloard_user WHERE user_id="+'"'+forgt1+'"'+";"
                mycursor.execute(exeqq)
                myresultt = mycursor.fetchall()
                if myresultt!=[]:
                    sed=myresultt[0]
                    server=smtplib.SMTP('smtp.gmail.com',587)
                    yag = yagmail.SMTP('infoanusav@gmail.com',"zvuvmibinbqlknke")
                    receiver = sed[4]
                    body = "Dear "+sed[3]+" ! \n\n I hope you are well. You Forget Your Password Don't Worry We are here.Your Current Password is "+sed[1]+" . I would recommand you to change your pasword.\n \nThanks\n Room Rent Khata Teams\nPowered by Anusav Tehnology"
                    yag.send(
                        to=receiver,
                        subject="Forget Password",
                        contents=body,
                    )
                    cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'Sucess !',text = "Email Send Sucessfully",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()

                else:
                    cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                    self.dialog = MDDialog(title = 'error !',text = "User Not Exist",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                    self.dialog.open()


        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

            
            
            

    def forget(self):
        digits = "0123456789"
        self.OTP = ""
        for i in range(6) :
            self.OTP += digits[math.floor(random.random() * 10)]
        screen_manager.current="ForgetScreen"
        screen_manager.get_screen('ForgetScreen').ids.capta.text=self.OTP
    def home(self):
        screen_manager.current="LSucessScreen"
    def sting(self):
        screen_manager.current="setting"
        
    def set_1(self):

        if self.theme_cls.primary_palette =="Teal":
            self.theme_cls.primary_palette ="Red"
        else:
            self.theme_cls.primary_palette ="Teal"

    





    def pay(self):
        try:
            screen_manager.current="Pay"
            rent_id=screen_manager.get_screen('PaymentScreen').ids.renter_id.text
            adm_id = screen_manager.get_screen('MainScreen').ids.username_text_fied.text
            exeqq="SELECT * FROM renter WHERE RENTER_USER_NAME="+'"'+rent_id+'"'+"AND ADMIN_ID =" +'"'+adm_id+'"'+";"
            mycursor.execute(exeqq)
            myresultt = mycursor.fetchall()     
            mycon.commit()
            self.pass1=myresultt[0]
            exeqq1="SELECT * FROM payment_details WHERE renter_id ="+'"'+rent_id+'"'+"AND landloard__user_id  =" +'"'+adm_id+'"'+" ORDER BY payment_date DESC;"
            mycursor.execute(exeqq1)
            myresultt1 = mycursor.fetchall()
            pass2=myresultt1
            if pass2==[]:
                self.p_e_read=self.pass1[13]
                self.p_w_read=self.pass1[14]
                self.p_g_read=self.pass1[15]
                self.rem_bal=str(0)
                user_q=self.pass1[6]
                screen_manager.get_screen('Pay').ids.pre_bal.text="Previous Balance : 0"
                self.recpt=str(user_q)+str(0000)        
            else:
                pass3=pass2[0]
                self.rem_bal=pass3[13]
                self.p_e_read=pass3[8]
                self.p_w_read=pass3[9]
                self.p_g_read=pass3[10]
                screen_manager.get_screen('Pay').ids.pre_bal.text="Previous Balance : "+self.rem_bal
                user_q=pass3[1]
                user_l=len(user_q)
                sef2q=list(pass3[16])
                sef3q=sef2q[user_l: ]
                sef4q="".join(sef3q)
                self.recpt=str(user_q)+str(int(sef4q)+1)
            t_e_cost=screen_manager.get_screen('PaymentScreen').ids.t_e_cost.text
            t_w_cost=screen_manager.get_screen('PaymentScreen').ids.t_w_cost.text
            t_g_cost=screen_manager.get_screen('PaymentScreen').ids.t_g_cost.text
            additional=screen_manager.get_screen('PaymentScreen').ids.additional.text
            r_rent=self.pass1[9]
            self.tcur_bal=str(float(t_e_cost)+float(t_w_cost)+float(t_g_cost)+float(additional)+float(r_rent))
            screen_manager.get_screen('Pay').ids.cur_bal.text="Current Balance : "+self.tcur_bal
            self.fin_bal=str(float(self.rem_bal)+float(self.tcur_bal))
            screen_manager.get_screen('Pay').ids.T_balance.text="Total Balance : "+self.fin_bal
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

    def rem(self):
        screen_manager.current="Reminder"
    def next_sign_in(self):
        try:
            self.next1=screen_manager.get_screen('Sign_Up').ids.name.text
            self.next2=screen_manager.get_screen('Sign_Up').ids.user_id.text
            self.next3=screen_manager.get_screen('Sign_Up').ids.password.text
            self.next4=screen_manager.get_screen('Sign_Up').ids.con_password.text
            exeqq="SELECT * FROM landloard_user WHERE user_id="+'"'+self.next2+'"'+";"
            mycursor.execute(exeqq)
            myresultta = mycursor.fetchall()
            if self.next1==""or self.next2=="" or self.next3==""or self.next4=="":       
                cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Error',text = "Please Fill All Details",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            elif self.next3!=self.next4:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Error',text = "Password donot match",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
            elif myresultta==[]:
                self.dialog = MDDialog(
                title="Contact Details",
                type="custom",
                content_cls=MDBoxLayout(
                    MDTextField( id ="moblle",
                                hint_text="Mobile No",
                                ),
                    MDTextField( id= "emmale",
                                hint_text="Email",),
                    orientation="vertical",
                    spacing="12dp",
                    size_hint_y=None,
                    height="120dp",
                    ),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release = self.close_username_dialogue,
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press = self.sign_con_up
                    ),
                    ],
                    )
                self.dialog.open()
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Error',text = "UserId already exits",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def sign_con_up(self,events):
        try:    
            next5=self.dialog.content_cls.ids.moblle.text
            next6=self.dialog.content_cls.ids.emmale.text
            if next5==next6=="":
                self.dialog.dismiss()

            else:
                exeqq="insert into landloard_user(user_id,PASSWORD,USER_NAME,MOBILE_NO,EMAIL_ID,USERPIC) values("+'"'+self.next2+'","'+self.next4+'","'+self.next1+'","'+next5+'","'+next6+'","images/logo.png"'+");"
                print(exeqq)
                mycursor.execute(exeqq)
                mycon.commit()
                self.back2_home_in()
        except Exception as e:
            print(e)

    def myrenter(self):
        try:
            screen_manager.current="myrenterScreen"
            exez1=screen_manager.get_screen('MainScreen').ids.username_text_fied.text
            quar1="SELECT * FROM renter WHERE ADMIN_ID="+'"'+exez1+'"'+";"
            mycursor.execute(quar1)
            exe2 = mycursor.fetchall()
            self.exe3=len(exe2)
            for i in range(self.exe3):
                exe4=exe2[i]
                self.us_id=exe4[6]
                self.nem=exe4[1]
                self.ret=exe4[9]
                self.pic=exe4[10]
                self.icons = ImageLeftWidget(source=exe4[10])
                self.items =  ThreeLineAvatarListItem(text=f"{exe4[1]}",secondary_text=f"Renter Id: {exe4[6]}",tertiary_text=f"Adhar Number : {exe4[5]}",on_release=self.myclick)
                self.items.add_widget(self.icons)
                screen_manager.get_screen('myrenterScreen').ids.three_list_viewer.add_widget(self.items) 
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    

    def myclick(self, ThreeLineAvatarListItem):
        try:
            sef1=ThreeLineAvatarListItem.secondary_text
            sef2=list(sef1)
            sef3=sef2[11: ]
            sef4="".join(sef3)
            screen_manager.current="RenterScreen"
            exez1=screen_manager.get_screen('MainScreen').ids.username_text_fied.text
            quar2="SELECT * FROM payment_details WHERE landloard__user_id="+'"'+exez1+'" And renter_id='+'"'+sef4+'"'+";"
            mycursor.execute(quar2)
            exel2 = mycursor.fetchall()
            quar12="SELECT * FROM renter WHERE ADMIN_ID="+'"'+exez1+'" And RENTER_USER_NAME ='+'"'+sef4+'"'+";"
            exel12=mycursor.execute(quar12)
            exel12 = mycursor.fetchall()
            self.exel13=len(exel12)
            self.exel3=len(exel2)
            for i in range(self.exel13):
                exel14=exel12[i]         
                screen_manager.get_screen('RenterScreen').ids.rent_id.text=sef1
                screen_manager.get_screen('RenterScreen').ids.nam.text=exel14[1]
                screen_manager.get_screen('RenterScreen').ids.rentt.text="Monthly Rent : "+exel14[9]
                screen_manager.get_screen('RenterScreen').ids.imagexpa.source=exel14[10]
                screen_manager.get_screen('RenterScreen').ids.email.text=exel14[3]
                screen_manager.get_screen('RenterScreen').ids.mobile.text="Mobile No : "+exel14[2]
     
            for i in range(self.exel3):
                exel4=exel2[i]         
                self.items1 =  ThreeLineListItem(text=f"MONTHS : {exel4[2]}",secondary_text=f"TOTAL PAYMENT : {exel4[6]}",tertiary_text=f"Payment Date: {exel4[7]}",on_release=self.myclick11)
                screen_manager.get_screen('RenterScreen').ids.three_list_viewer.add_widget(self.items1)    
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

    def myclick11(self, ThreeLineListItem):
        sef1=ThreeLineListItem.tertiary_text
        sef2=list(sef1)
        sef3=sef2[14: ]
        sef4="".join(sef3)
        exez2=screen_manager.get_screen('RenterScreen').ids.rent_id.text
        sefv2=list(exez2)
        sefv3=sefv2[11: ]
        sefv4="".join(sefv3)
        quar2="SELECT * FROM payment_details WHERE renter_id= "+'"'+sefv4+'"'+' And payment_date='+'"'+sef4+'"'+";"
        mycursor.execute(quar2)
        exel2 = mycursor.fetchall()
        dig=exel2[0]
        cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
        self.dialog = MDDialog(title = dig[2],text = "Electric Meter Reading: "+dig[8]+"\nElectric Cost: "+dig[4]+"\nWater Reading: "+dig[9]+"\nWater Cost: "+dig[3]+"\nGas Reading: "+dig[10]+"\nGas Cost: "+dig[11]+"\nMaintanance Cost: "+dig[12]+"\nTotal Cost: "+dig[5]+"\nTotal Payment: "+dig[6]+"\nPayment Type:"+dig[14],size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
        self.dialog.open()

    


    def back_payyy(self):
        screen_manager.current="PaymentScreen"
    def back_payy(self):
        screen_manager.current="Pay"
    def conpay(self):
        try:
            screen_manager.get_screen('Pay').ids.biill.disabled=False
            now = datetime.now()
            self.dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            rent_id=screen_manager.get_screen('PaymentScreen').ids.renter_id.text
            months=screen_manager.get_screen('PaymentScreen').ids.months.text
            c_e_read=screen_manager.get_screen('PaymentScreen').ids.c_e_read.text
            c_w_read=screen_manager.get_screen('PaymentScreen').ids.c_w_read.text
            c_g_read=screen_manager.get_screen('PaymentScreen').ids.c_g_read.text
            t_e_cost=screen_manager.get_screen('PaymentScreen').ids.t_e_cost.text
            t_w_cost=screen_manager.get_screen('PaymentScreen').ids.t_w_cost.text
            t_g_cost=screen_manager.get_screen('PaymentScreen').ids.t_g_cost.text
            additional=screen_manager.get_screen('PaymentScreen').ids.additional.text
            adm_id = screen_manager.get_screen('MainScreen').ids.username_text_fied.text
            depo=screen_manager.get_screen('Pay').ids.depo.text
            date=self.dt_string
            p_type=screen_manager.get_screen('Pay').ids.p_type.text
            det_pay=screen_manager.get_screen('Pay').ids.det_pay.text
            self.reming_ball=str(float(self.fin_bal)-float(depo))
            co1="insert into payment_details(landloard__user_id,renter_id,months,total_water_cost,total_electric_cost,total_cost,total_payment,payment_date,electric_reading,water_reading,gas_reading,total_gas_cost,maintanance,remaining_bal,P_type,add_P_type,recpt_no) values("+'"'+adm_id+'","'+rent_id+'","'+months+'","'+t_w_cost+'","'+t_e_cost+'","'+self.fin_bal+'","'+depo+'","'+date+'","'+c_e_read+'","'+c_w_read+'","'+c_g_read+'","'+t_g_cost+'","'+additional+'","'+self.reming_ball+'","'+p_type+'","'+det_pay+'","'+self.recpt+'"'+");"
            exeqq=co1
            mycursor.execute(exeqq)
            mycon.commit()
            cancel_btn_username_dialogue = MDFlatButton(text='Print Bill',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Sucess !',text = "Added In Database",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
       
    def backrenter(self):
        try:
            if screen_manager.current=="RenterScreen":
                try:
                    self.items1.clear_widgets()
                    screen_manager.get_screen('RenterScreen').ids.three_list_viewer.clear_widgets() 
                except Exception as e:
                    print(e)
                    screen_manager.get_screen('RenterScreen').ids.three_list_viewer.remove_widget(self.items)
            screen_manager.current="myrenterScreen"  
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

    def back(self):
        try:
            # for backing puropse
            if screen_manager.current=="myrenterScreen":
                try:
                    self.items.clear_widgets()
                    screen_manager.get_screen('myrenterScreen').ids.three_list_viewer.clear_widgets() 
                except Exception as e:
                    print(e)
                    try:
                        self.items.remove_widget(self.icons)
                        screen_manager.get_screen('myrenterScreen').ids.three_list_viewer.remove_widget(self.items)
                    except Exception as e:
                        print(e)
            screen_manager.current="LSucessScreen"           
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
 
    
    def us_about(self):
        screen_manager.current="About_Us"
    def editpro(self):
        try:
            screen_manager.current="myprofilScreen"
            n1=screen_manager.get_screen('MainScreen').ids.username_text_fied.text
            exeq1="SELECT * FROM landloard_user WHERE USER_ID="+'"'+n1+'"'
            mycursor.execute(exeq1)
            myresult = mycursor.fetchall()     
            if myresult!=[]:
                pasd=myresult[0]    
                screen_manager.get_screen('myprofilScreen').ids.imagexpa.source= pasd[2]
                screen_manager.get_screen('myprofilScreen').ids.u_name.text= pasd[3]
                screen_manager.get_screen('myprofilScreen').ids.u_id.text= pasd[0]
                screen_manager.get_screen('myprofilScreen').ids.pas.text= pasd[1]
                screen_manager.get_screen('myprofilScreen').ids.email.text= pasd[4]
                screen_manager.get_screen('myprofilScreen').ids.m_no.text= pasd[5]
                screen_manager.get_screen('myprofilScreen').ids.p_link.text= pasd[2]
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'error !',text = "Error",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()

        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

    def conf_del(self,obj):
        try:
            dele1=screen_manager.get_screen('deleterenterScreen').ids.renter_id.text
            dele12=screen_manager.get_screen('MainScreen').ids.username_text_fied.text
            dele2="DELETE FROM ROOM_RENT_KHATA.renter WHERE(RENTER_USER_NAME ="+ '"'+dele1+'"'+");"
            mycursor.execute(dele2)
            dele21="DELETE FROM payment_details WHERE renter_id ="+ '"'+dele1+'"'+"and landloard__user_id= "+'"'+dele12+'"'+";"
            mycursor.execute(dele21)
            mycursor.fetchall()
            mycon.commit()
            self.dialog.dismiss()
            cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Sucess',text = "Delete Sucessfully",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

    def fetch_del(self):
        try:
            self.dele1=screen_manager.get_screen('modifyrenterScreen').ids.renter_id.text
            self.dele12=screen_manager.get_screen('MainScreen').ids.username_text_fied.text
            dele21="SELECT * FROM renter WHERE renter_user_name ="+ '"'+self.dele1+'"'+"and ADMIN_ID= "+'"'+self.dele12+'"'+";"
            mycursor.execute(dele21)
            fetch_1=mycursor.fetchall()
            fetch_2=fetch_1[0]
            screen_manager.get_screen('editrenter').ids.name.text=fetch_2[1]
            screen_manager.get_screen('editrenter').ids.f_name.text=fetch_2[11]
            screen_manager.get_screen('editrenter').ids.mobile_no.text=fetch_2[2]
            screen_manager.get_screen('editrenter').ids.email.text=fetch_2[3]
            screen_manager.get_screen('editrenter').ids.adress.text=fetch_2[4]
            screen_manager.get_screen('editrenter').ids.adhar_no.text=fetch_2[5]
            screen_manager.get_screen('editrenter').ids.pasword.text=fetch_2[7]
            screen_manager.get_screen('editrenter').ids.no_of_person.text=fetch_2[8]
            screen_manager.get_screen('editrenter').ids.mon_name.text=fetch_2[9]
            screen_manager.get_screen('editrenter').ids.renter_image.text=fetch_2[10]
            screen_manager.get_screen('editrenter').ids.adhar_pic.text=fetch_2[12]         
            screen_manager.current = "editrenter"
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

 
    def fin_upd(self):
        try:
            fetch_4=screen_manager.get_screen('editrenter').ids.name.text
            fetch_5=screen_manager.get_screen('editrenter').ids.f_name.text
            fetch_6=screen_manager.get_screen('editrenter').ids.mobile_no.text
            fetch_7=screen_manager.get_screen('editrenter').ids.email.text
            fetch_8=screen_manager.get_screen('editrenter').ids.adress.text
            fetch_9=screen_manager.get_screen('editrenter').ids.adhar_no.text
            fetch_10=screen_manager.get_screen('editrenter').ids.pasword.text
            fetch_11=screen_manager.get_screen('editrenter').ids.no_of_person.text
            fetch_12=screen_manager.get_screen('editrenter').ids.mon_name.text
            fetch_13=screen_manager.get_screen('editrenter').ids.renter_image.text
            fetch_14=screen_manager.get_screen('editrenter').ids.adhar_pic.text         
            update="update renter set NAME="+'"'+fetch_4+'",'+"FATHERS_NAME= "+'"'+fetch_5+'",'+"MOBILE_NO="+'"'+fetch_6+'",'+"EMAIL="+'"'+fetch_7+'",'+"adress="+'"'+fetch_8+'",'+"ADHAR_NO="+'"'+fetch_9+'",'+"PASWORD="+'"'+fetch_10+'",'+"NO_OF_PERSON="+'"'+fetch_11+'",'+"MONTHLY_RENT="+'"'+fetch_12+'",'+"image_link="+'"'+fetch_13+'",'+"Aadhar_pic="+'"'+fetch_14+'"'+"WHERE renter_user_name ="+ '"'+self.dele1+'"'+"and ADMIN_ID= "+'"'+self.dele12+'"'+";"
            mycursor.execute(update)
            mycursor.fetchall()
            mycon.commit()
            cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Sucess !',text = "Sucessfully Updated",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()


    def del_con(self):
        try:
            cancel_btn_username_dialogue = MDFlatButton(text='No',on_release = self.close_username_dialogue)
            sucess_btn_username_dialogue = MDFlatButton(text='Yes',on_release = self.conf_del)
            self.dialog = MDDialog(title = '!',text = "Are You Sure you want to Delete",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue,sucess_btn_username_dialogue])
            self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

    def next_rem(self):
        try:    
            self.dele1=screen_manager.get_screen('Reminder').ids.renter_id.text
            self.dele12=screen_manager.get_screen('MainScreen').ids.username_text_fied.text
            dele21="SELECT * FROM renter WHERE renter_user_name ="+ '"'+self.dele1+'"'+"and ADMIN_ID= "+'"'+self.dele12+'"'+";"
            mycursor.execute(dele21)
            fetch_1=mycursor.fetchall()
            fetch_2=fetch_1[0]
            exeeqq1="SELECT * FROM payment_details WHERE renter_id ="+'"'+self.dele1+'"'+"AND landloard__user_id  =" +'"'+self.dele12+'"'+" ORDER BY payment_date DESC;"
            mycursor.execute(exeeqq1)
            myres1 = mycursor.fetchall()
            pass2=myres1[0]
            applx="SELECT * FROM landloard_user WHERE user_id ="+'"'+self.dele12+'";'
            mycursor.execute(applx)
            mytestq = mycursor.fetchall()
            mytest1=mytestq[0]
            self.ad_nam=mytest1[3]
            self.rembal=pass2[13]
            self.rcpt=pass2[16]
            self.dete=pass2[7]
            self.e_mail=fetch_2[3]
            self.e_name=fetch_2[1]
            server=smtplib.SMTP('smtp.gmail.com',587)
            yag = yagmail.SMTP('infoanusav@gmail.com',"zvuvmibinbqlknke")
            receiver = self.e_mail
            body = "Dear "+self.e_name+" ! \n\n I hope you are well. I just wanted to drop you a quick note to remind you that RS "+self.rembal+" in respect of invoice "+self.rcpt+" is due for payment on "+str(self.dete)+"  \nI would like be really greatfull if you could confirm that everything is on track for payment.\n \nThanks\n"+self.ad_nam
            filename = "recept/"+self.rcpt+".pdf"
            yag.send(
                to=receiver,
                subject="Payment Reminder",
                contents=body, 
                attachments=filename,
            )
            cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Sucess !',text = "Email Send Sucessfully",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

        

        


    def edit_pro(self): 
        try:
            exea1 = screen_manager.get_screen('MainScreen').ids.username_text_fied.text
            exeq2 = screen_manager.get_screen('myprofilScreen').ids.u_name.text
            exeq3 = screen_manager.get_screen('myprofilScreen').ids.u_id.text
            exeq4 = screen_manager.get_screen('myprofilScreen').ids.pas.text
            exeq5 = screen_manager.get_screen('myprofilScreen').ids.email.text
            exeq6 = screen_manager.get_screen('myprofilScreen').ids.m_no.text
            exeq7 = screen_manager.get_screen('myprofilScreen').ids.p_link.text
            exeq8= "UPDATE ROOM_RENT_KHATA.landloard_user SET USER_ID="+"'"+exeq3+"'" +", PASSWORD="+"'"+exeq4+"'"+", USERPIC="+"'"+exeq7+"'"+", USER_NAME="+"'"+exeq2+"'" +", EMAIL_ID="+"'"+exeq5+"'" +", MOBILE_NO="+"'"+exeq6+"'"+" WHERE (USER_ID="+'"'+exea1+'"'+");"
            mycursor.execute(exeq8)    
            mycursor.fetchall()
            mycon.commit()
            cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Sucess !',text = "Sucessfully added on Databases",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()       
    def addrenter(self):
        screen_manager.current = "addrenterScreen"
    def logout(self):
        screen_manager.current = "MainScreen"
    def modifyrenter(self):
        screen_manager.current="modifyrenterScreen"
    def searchrenter(self):
        screen_manager.current="searchrenterScreen"
    def deleterenter(self):
        screen_manager.current="deleterenterScreen"
    def bill(self):
        screen_manager.current="billrenterScreen" 
    def billpdf(self):
        try:
            class PDF(FPDF, HTMLMixin):
                pass
            pdf = PDF()
            rent_id=screen_manager.get_screen('PaymentScreen').ids.renter_id.text
            months=screen_manager.get_screen('PaymentScreen').ids.months.text
            c_e_read=screen_manager.get_screen('PaymentScreen').ids.c_e_read.text
            c_w_read=screen_manager.get_screen('PaymentScreen').ids.c_w_read.text            
            c_g_read=screen_manager.get_screen('PaymentScreen').ids.c_g_read.text
            t_e_cost=screen_manager.get_screen('PaymentScreen').ids.t_e_cost.text
            t_w_cost=screen_manager.get_screen('PaymentScreen').ids.t_w_cost.text
            t_g_cost=screen_manager.get_screen('PaymentScreen').ids.t_g_cost.text
            additional=screen_manager.get_screen('PaymentScreen').ids.additional.text
            screen_manager.get_screen('MainScreen').ids.username_text_fied.text
            depo=screen_manager.get_screen('Pay').ids.depo.text
            date=self.dt_string
            p_type=screen_manager.get_screen('Pay').ids.p_type.text
            screen_manager.get_screen('Pay').ids.det_pay.text
            ren_uname=self.pass1[1]
            r_rent=self.pass1[9]
            data = [
                ("S NO.", "RENT HEAD", "TOTAL", "STATUS"),
                ("1", "ROOM RENT", r_rent, "PAID"),
                ("2", "ELECTRIC BILL", t_e_cost, "PAID"),
                ("3", "WATER BILL", t_w_cost, "PAID"),
                ("4", "GAS BILL", t_g_cost, "PAID"),
                ("5", "MAINTENANCE", additional, "PAID"),
                ("6", "TOTAL",str(float(t_e_cost)+float(t_w_cost)+float(t_g_cost)+float(additional)+float(r_rent)), "PAID"),
            ]
            data1 = [
                ("DEPOSITE", "PREVIOUS BALANCE", "CURRENT BALANCE", "PAYED TYPE"),
                (depo, self.rem_bal, self.reming_ball, p_type),
            ]
            data2 = [
                ("TYPE", "CURRENT READING", "PREVIOUS READING","TOTAL READING"),
                ("ELECTRIC", c_e_read, self.p_e_read,str(float(c_e_read)-float(self.p_e_read)) ),
                ("WATER", c_w_read, self.p_w_read,str(float(c_w_read)-float(self.p_w_read)) ),
                ("GAS", c_g_read, self.p_g_read,str(float(c_g_read)-float(self.p_g_read)) ),
            ]
            pdf.set_font_size(16)
            pdf.add_page()
            # set style and size of font
            # that you want in the pdf
            pdf.set_font('Arial', '', 12)
            pdf.set_fill_color(200, 220, 255) 
            pdf.cell(0, 6 ,"", 0, 1, 'L', True)
            pdf.ln(4)
            pdf.set_font("Arial", size = 30)
            pdf.cell(200, 10, txt = "Room Rent Khata",
                    ln = 1, align = 'C')
            pdf.set_font('Arial', '', 15)
            pdf.cell(200, 10, txt = "Powered By AnuSav Technology",
                    ln = 2, align = 'C')
            pdf.image('images/logo.png', 45, 18, 20)
            pdf.set_font('Arial', '', 12) 
            pdf.set_fill_color(200, 220, 255)  
            pdf.cell(0, 6, "", 0, 1, 'L', True)
            pdf.ln(6)
            pdf.cell(0, 10, txt = "RENTER COPY",
                    ln = 0, align = 'C')
            pdf.ln(7)
            pdf.cell(0, 8, txt = "RECEPIT ID: "+self.recpt,
                    align = 'L')
            pdf.cell(0, 8, txt = "DATE: "+date,
                    align = 'R')
            pdf.ln(8)
            pdf.cell(0, 8, txt = "RENTER DETAILS",
                    ln = 0, align = 'L')
            pdf.ln(9)
            pdf.cell(0, 8, txt = "NAME",
                    align = 'L')
            pdf.cell(0, 8, txt = ren_uname,
                    align = 'R')
            pdf.ln(10)
            pdf.cell(0, 5, txt = "ROOM RENT ID",
                    ln = 0, align = 'L')
            pdf.cell(0, 5, txt = rent_id,
                    ln = 0, align = 'R') 
            pdf.ln(11)
            pdf.cell(0, 2, txt = "PAYMENT DETAILS",
                    align = 'L')
            pdf.cell(0, 4, txt = "MONTHS : "+months,
                    align = 'R')
            pdf.write_html(
                f"""<table border="1"><thead><tr>
                <th width="16%">{data[0][0]}</th>
                <th width="28%">{data[0][1]}</th>
                <th width="28%">{data[0][2]}</th>
                <th width="28%">{data[0][3]}</th>
            </tr></thead><tbody><tr>
                <td>{'</td><td>'.join(data[1])}</td>
            </tr><tr>
                <td>{'</td><td>'.join(data[2])}</td>
            </tr><tr>
                <td>{'</td><td>'.join(data[3])}</td>
            </tr><tr>
                <td>{'</td><td>'.join(data[4])}</td>
            </tr><tr>
                <td>{'</td><td>'.join(data[5])}</td>
            </tr><tr>
                <td>{'</td><td>'.join(data[6])}</td>
            </tr></tbody></table>"""
            )
            pdf.cell(0, 5, txt = "ADDITIONAL DETAILS",
                    align = 'L')
            pdf.write_html(
                f"""<table border="1"><thead><tr>
                <th width="16%">{data2[0][0]}</th>
                <th width="28%">{data2[0][1]}</th>
                <th width="28%">{data2[0][2]}</th>
                <th width="28%">{data2[0][3]}</th>
            </tr></thead><tbody><tr>
                <td>{'</td><td>'.join(data2[1])}</td>
                </tr><tr>
                <td>{'</td><td>'.join(data2[2])}</td>
                </tr><tr>
                <td>{'</td><td>'.join(data2[3])}</td>
            </tr></tbody></table>"""
            )
            pdf.cell(0, 5, txt = "TRANSATION DETAILS",
                    align = 'L')
            pdf.write_html(
                f"""<table border="1"><thead><tr>
                <th width="16%">{data1[0][0]}</th>
                <th width="28%">{data1[0][1]}</th>
                <th width="28%">{data1[0][2]}</th>
                <th width="28%">{data1[0][3]}</th>
            </tr></thead><tbody><tr>
                <td>{'</td><td>'.join(data1[1])}</td>
            </tr></tbody></table>"""
            )
            pdf.ln(17)
            pdf.cell(0, 10, txt = "RECIEVED BY/LANDLOARD SIGN",
                    align= 'R')
            pdf.ln(33)
            pdf.image('images/barcode.gif', 15, 255, 20)
            pdf.cell(0, 10, txt = "DOWNLOAD FROM https://www.anusavtechnology.com/room_rent_khata/download",
                    align = 'R')
            pdf.output("recept/"+self.recpt+'.pdf')
            cancel_btn_username_dialogue = MDFlatButton(text='Print Bill',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Created',text ="Bill Has been created",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def payment(self):
        screen_manager.current="PaymentScreen"
    def scan(self):
        screen_manager.current="ScanScreen"
    def close_username_dialogue(self,obj):
        self.dialog.dismiss()
    def backadd_renter(self):
        screen_manager.current="addrenterScreen"
    def add_sucessnextt(self):
        screen_manager.current="addrenternxtScreen"
    def add_sucess(self):
        try:
            as0=screen_manager.get_screen('addrenterScreen').ids.name.text
            as1=screen_manager.get_screen('addrenterScreen').ids.f_name.text
            as2=screen_manager.get_screen('addrenterScreen').ids.mobile_no.text
            as3=screen_manager.get_screen('addrenterScreen').ids.email.text
            as4=screen_manager.get_screen('addrenterScreen').ids.adress.text
            as5=screen_manager.get_screen('addrenterScreen').ids.adhar_no.text
            as6=screen_manager.get_screen('addrenternxtScreen').ids.user_id.text
            
            as8=screen_manager.get_screen('addrenterScreen').ids.no_of_person.text
            as9=screen_manager.get_screen('addrenternxtScreen').ids.mon_name.text
            as02=screen_manager.get_screen('addrenternxtScreen').ids.renter_image.text
            as03=screen_manager.get_screen('addrenternxtScreen').ids.adhar_pic.text
            as04=screen_manager.get_screen('addrenternxtScreen').ids.g_rd.text
            as05=screen_manager.get_screen('addrenternxtScreen').ids.e_rd.text
            screen_manager.get_screen('addrenternxtScreen').ids.w_rd.text            
            as01=screen_manager.get_screen('MainScreen').ids.username_text_fied.text            
            n01="'"+as01+"'"+","+"'"+as0+"'"+","+"'"+as1+"'"+","+"'"+as2+"'"+","+"'"+as3+"'"+","+"'"+as4+"'"+","+"'"+as5+"'"+","+"'"+as6+"'"+","+"'"+as8+"'"+","+"'"+as9+"'"+","+"'"+as02+"'"+","+"'"+as03+"'"+","+"'"+as05+"'"+","+"'"+as05+"'"+","+"'"+as04+"'"
            n02="INSERT INTO renter(ADMIN_ID ,NAME,FATHERS_NAME ,MOBILE_NO ,EMAIL,ADRESS ,ADHAR_NO,RENTER_USER_NAME , NO_OF_PERSON ,MONTHLY_RENT ,IMAGE_LINK,Aadhar_pic,e_meter_reading,w_meter_reading,g_meter_reading) VALUES("+n01+");" 
            mycursor.execute(n02)
            mycon.commit()
            cancel_btn_username_dialogue = MDFlatButton(text='Close',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'Sucess !',text = "Sucessfully added on Databases",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def darkthe(self):
        try:
            if self.theme_cls.theme_style == "Dark":
                self.theme_cls.theme_style = "Light"
                screen_manager.get_screen('LSucessScreen').ids.darkthe.text="Dark Theme"
            else:
                self.theme_cls.theme_style = "Dark"
                screen_manager.get_screen('LSucessScreen').ids.darkthe.text="Light Theme"
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    def log_in(self):
        try:
            n1=screen_manager.get_screen('MainScreen').ids.username_text_fied.text
            n2="SELECT * FROM landloard_user WHERE USER_ID="+'"'+n1+'"'
            n3= screen_manager.get_screen('MainScreen').ids.pasword_text_fied.text
            mycursor.execute(n2)
            myresult = mycursor.fetchall()      
            pasd=myresult[0]
            i=pasd[1]
            if i==n3:
                i1=pasd[3]
                screen_manager.get_screen('LSucessScreen').ids.name.text=i1
                i2=pasd[4]
                screen_manager.get_screen('LSucessScreen').ids.email.text=i2
                i3=pasd[2]
                if i3==None:
                    screen_manager.get_screen('LSucessScreen').ids.avatar.source="images/logo.png"
                else:
                    screen_manager.get_screen('LSucessScreen').ids.avatar.source=i3
                screen_manager.current="LSucessScreen" 
            else:
                cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Error',text = "Please enter valid pasword",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()
        except Exception as e:
            cancel_btn_username_dialogue = MDFlatButton(text='cancel',on_release = self.close_username_dialogue)
            self.dialog = MDDialog(title = 'error !',text = str(e),size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
    
Room_Rent_Khata().run()