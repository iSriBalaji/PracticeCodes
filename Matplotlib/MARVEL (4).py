#Coding-Baju
import os
import speech_recognition as sr
import pyrebase
import time
import numpy
import cv2
#CLINICON CLOUD DATABASE
clinicon_keys={
    "apiKey": "AIzaSyA6FBqWvp-UhUbRp7h5I2jZYSge2kSZRMg",
    "authDomain": "clinicon-medineers.firebaseapp.com",
    "databaseURL": "https://clinicon-medineers.firebaseio.com",
    "projectId": "clinicon-medineers",
    "storageBucket": "clinicon-medineers.appspot.com",
    "messagingSenderId": "1049649886187"
}
cloud=pyrebase.initialize_app(clinicon_keys)
clinicon_database=cloud.database()
#GETTING CLINICON ID FROM DATABASE
clinicon_id=clinicon_database.child("CLINICON_ID").child("NO").get().val()
#DETECTING MICROPHONE 
mic_name = "USB PnP Sound Device: Audio (hw:1,0)"
sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer() 
mic_list = sr.Microphone.list_microphone_names()
print(mic_list)
for i, microphone_name in enumerate(mic_list): 
	if microphone_name == mic_name: 
		device_id = i
#MICROPHONE FUNCTION
def cliniconGetData(return_statement):
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
						chunk_size = chunk_size) as source: 
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source) 
		
            try: 
                    text = r.recognize_google(audio)
                    if(return_statement=="Gender: "):
                        if(text[0]=="M" or text[0]=="m" ):
                            text="MALE"
                    return_statement=return_statement+text
                    print(return_statement.upper())
                    return(text)
	
            except sr.UnknownValueError: 
                    print("Google Speech Recognition could not understand audio")
                    print("Repeat the statement again...")
                    return("-----")
	
            except sr.RequestError as e: 
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    return("-----")
#FUNCTION TO UPDATE CLINICPON DATABASE
def cliniconUpdateData(child,dic_key,dic_val):
        clinicon_database.child("%s"%child).update({"%s"%dic_key:"%s"%dic_val})
#STARTING OF PROGRAM
#------------------#
welcome="----WELCOME TO CLINICON----"
nwelcome=welcome.center(24)
print(nwelcome)
imgg=cv2.imread('0.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
os.system("espeak 'Welcome to Clinicon'")
print()
print("DEVICE ID: Clini_devi_34\n")
clini_dev_id="Clini_devi_34"
print("LOCATION: KOVILPATTI")
localtime=time.asctime(time.localtime(time.time()))
print(localtime)
print()
#GENERATING ID FOR THE PATIENT
clinicon_no=str(int(clinicon_database.child("CLINICON_ID").child("NO").get().val())+1)
while(len(clinicon_no)<3):
        clinicon_no="0"+clinicon_no
clinicon_database.child("CLINICON_ID").update({"NO":clinicon_no})
#PATIENT ID
patient_ID="CliniSIH"+clinicon_no
#FILE WRITING
with open(patient_ID+".doc","a") as f:
    print("CLINICON - Rural People Medical Assistant",file=f)
    print("\nDEVICE ID: Clini_devi_34\n",file=f)
    print("LOCATION: KOVILPATTI\n",file=f)
    print(localtime,file=f)
    print("\n\n")
    print("PATIENT ID: %s"%patient_ID)
    print("\n")
    print(40*"=",file=f)
#GETTING NAME
print("RECITE YOUR NAME")
os.system("espeak 'Recite your Name'")
imgg=cv2.imread('1.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
patient_name=cliniconGetData("Hello ")
patient_name=patient_name.upper()
cliniconUpdateData(patient_ID,"NAME",patient_name)
print("---------------------------")
print()
with open(patient_ID+".doc","a") as f:
    print("NAME: %s"%patient_name,file=f)
#GETTING GENDER
print("RECITE YOUR GENDER: MALE/FEMALE")
os.system("espeak 'Recite your Gender'")
imgg=cv2.imread('2.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
patient_gender=cliniconGetData("Gender: ")
patient_gender=patient_gender.upper()
if(patient_gender[0]=="M"):
        patient_gender="MALE"
cliniconUpdateData(patient_ID,"GENDER",patient_gender)
print("---------------------------")
print()
with open(patient_ID+".doc","a") as f:
    print("GENDER: %s"%patient_gender,file=f)
#GETTING AGE
print("RECITE YOUR AGE")
os.system("espeak 'Recite your age'")
imgg=cv2.imread('3.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
patient_age=cliniconGetData("AGE: ")
patient_age=patient_age.upper()
cliniconUpdateData(patient_ID,"AGE",patient_age)
print("---------------------------")
print()
with open(patient_ID+".doc","a") as f:
    print("AGE: %s"%patient_age,file=f)
#GETTING WEIGHT
print("RECITE YOUR WEIGHT")
os.system("espeak 'Recite your weight'")
imgg=cv2.imread('4.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
patient_weight=cliniconGetData("WEIGHT: ")
patient_weight=patient_weight.upper()
cliniconUpdateData(patient_ID,"WEIGHT",patient_weight)
print("---------------------------")
print()
with open(patient_ID+".doc","a") as f:
    print("WEIGHT: %s"%patient_weight,file=f)
#GETTING PHONE NUMBER
print("RECITE YOUR CONTACT NO")
os.system("espeak 'Recite your contact no'")
imgg=cv2.imread('5.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
patient_contact=cliniconGetData("CONTACT NO: ")
patient_contact=patient_contact.upper()
cliniconUpdateData(patient_ID,"CONTACT NO",patient_contact)
print("---------------------------")
print()
with open(patient_ID+".doc","a") as f:
    print("CONTACT NO: %s"%patient_contact,file=f)
    print(40*"=",file=f)
#PROVIDING CLINICON ID
print("Your CLINICON ID is: %s"%patient_ID)
print("---------------------------")
print()
#ADD IMAGE TO DOC
#CAPTURING PATIENTs
print("FACE THE CAMERA")
os.system("espeak 'Face the Camera'")
imgg=cv2.imread('6.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
os.system("espeak 'Capturing Photo'")
os.system("fswebcam %s"%patient_ID)
print("---------------------------")
print()
cliniconUpdateData(patient_ID,"DEVICE_ID",clini_dev_id)
cliniconUpdateData(patient_ID,"DATE_AND_TIME",localtime)
cliniconUpdateData(patient_ID,"DEVICE LOCATION","KOVILPATTI")
#OPENING IMAGE
imgg=cv2.imread('%s'%patient_ID)
cv2.imshow('PATIENT_PHOTO',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
#Pulse Sensor
os.system("espeak 'Enter your heart rate in B P M'")
imgg=cv2.imread('7.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
print("Enter your heart rate in BPM")
puls=input()
cliniconUpdateData(patient_ID,"PULSE",puls)
with open(patient_ID+".doc","a") as f:
    print("PULSE RATE: %s"%puls,file=f)
#Temperature Sensor
os.system("espeak 'Enter the Body Temperature'")
imgg=cv2.imread('8.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
print("Enter the Body Temperature")
tempp=input()
cliniconUpdateData(patient_ID,"TEMPERATURE",tempp)
with open(patient_ID+".doc","a") as f:
    print("BODY TEMPERATURE: %s"%tempp,file=f)
#Humidity Sensor
os.system("espeak 'Enter the Surrounding Temperature'")
imgg=cv2.imread('9.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
print("Enter the Surrounding Temperature")
s_temp=input()
cliniconUpdateData(patient_ID,"SURROUNDING TEMPERATURE",s_temp)
with open(patient_ID+".doc","a") as f:
    print("SURROUNDING TEMPERATURE: %s"%s_temp,file=f)
#Hum2 Sensor
os.system("espeak 'Enter the Surrounding Humidity'")
imgg=cv2.imread('10.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
print("Enter the Surrounding Humidity")
h_temp=input()
cliniconUpdateData(patient_ID,"SURROUNDING HUMIDITY",h_temp)
with open(patient_ID+".doc","a") as f:
    print("SURROUNDING HUMIDITY: %s"%h_temp,file=f)
    print(40*"=",file=f)
#SYMPTOMS
sym_list=[]
dis="******"
flag=0
cnt1=0
cnt2=0
kjj=[]
os.system("espeak 'SELECT YOUR SYMPTOMS'")
imgg=cv2.imread('11.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
print("SELECT YOUR SYMPTOMS")
print()
print("Cough?")
os.system("espeak 'Do you have Cough?'")
patient_sym=input()
patient_sym=patient_sym.upper()
print()
if(patient_sym=="Y" or patient_sym=="S"):
        kjj.append('1')
        sym_list.append("Cough")
print("Fever?")
os.system("espeak 'Do you have Fever?'")
patient_sym=input()
patient_sym=patient_sym.upper()
print()
if(patient_sym=="Y" or patient_sym=="S"):
        kjj.append('2')
        sym_list.append("Fever")
print("Abdominal or Stomach Pain?")
os.system("espeak 'Do you have Abdominal or Stomach Pain?'")
patient_sym=input()
patient_sym=patient_sym.upper()
print()
if(patient_sym=="Y" or patient_sym=="S"):
        kjj.append('3')
        sym_list.append("Abdominal/Stomach Pain")
print("Vomiting?")
os.system("espeak 'Do you suffer from vomiting?'")
patient_sym=input()
patient_sym=patient_sym.upper()
print()
if(patient_sym=="Y" or patient_sym=="S"):
        kjj.append('4')
        sym_list.append("Vomiting")
print("Dizziness?")
os.system("espeak 'Do you suffer from Dizziness?'")
patient_sym=input()
patient_sym=patient_sym.upper()
print()
if(patient_sym=="Y" or patient_sym=="S"):
        kjj.append('5')
        sym_list.append("Dizziness")
print("Severe Headache?")
os.system("espeak 'Do you suffer from headache?'")
patient_sym=input()
patient_sym=patient_sym.upper()
print()
if(patient_sym=="Y" or patient_sym=="S"):
        kjj.append('6')
        sym_list.append("Headache")
print()
print("***************************")
print()
print("Analysing...")
os.system("espeak 'Analysing'")
print()
if(('2' in kjj) and ('3'in kjj) and('4' in kjj)and (flag==0)):
    jkl=[]
    print("1. High Fever with shivering?\n2. Gradual increase in temperature throught the day?\n3. Night sweats?\n4. Loss of appetite?\n5. Abdominal / Body pain?\n6. Rose spots in abdomen?")
    print()
    #1
    print("High Fever with shivering?")
    os.system("espeak 'Do you suffer from High Fever with shivering?'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('1')
        sym_list.append("High Fever with shivering")
    #2
    print("Gradual increase in temperature throught the day?")
    os.system("espeak 'wheather you have Gradual increase in temperature throught the day?'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('2')
        sym_list.append("Increase in Temperature")
    #3
    print("Night sweats?")
    os.system("espeak 'Do you suffer from Night Sweats'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('3')
        sym_list.append("Night Sweats")
    #4
    print("Loss of appetite?")
    os.system("espeak 'Do you suffer from loss of appetite'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('4')
        sym_list.append("Loss of Appetite")
    #5
    print("Abdominal / Body pain?")
    os.system("espeak 'Do you suffer from Abdominal pain'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('5')
        sym_list.append("Abdominal Pain")
    #6
    print("Rose spots in abdomen?")
    os.system("espeak 'Do you suffer from rose spots in abdomen'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('6')
        sym_list.append("Rose spots in Abdomen")
    for i in jkl:
        if(i in ['1','3','5']):
            cnt1+=1
        if(i in ['2','4','6']):
            cnt2+=1
    if(cnt1>cnt2):
        dis="MALARIA"
    else:
        dis="TYPHOID FEVER"
    print()
    print("***************************")
    print()
    print("You are affected by %s"%dis)
    flag=1
    print()
    print("***************************")
    print()  
if((('1' in kjj) or ('2'in kjj))and (flag==0)):
        jkl=[]
        print("1. Cough with increased sputum or blood?\n2. Nasal congestion?\n3. Chest pain?\n4. Rise in temperature during evenings and nights?\n5. Mild fever?\n6. Sudden weight loss?\n7. Heavy fever?\n8. Runny nose?")
        print()
        #1
        print("Cough with increased sputum or blood?")
        os.system("espeak 'Do you suffer from cough with increased sputum or blood'")
        patient_sym=input()
        patient_sym=patient_sym.upper()
        print()
        if(patient_sym=="Y" or patient_sym=="S"):
            jkl.append('1')
            sym_list.append("Cough with increased sputum or blood")
        #2
        print("Nasal congestion?")
        os.system("espeak 'do you suffer from nasal congestion?'")
        patient_sym=input()
        patient_sym=patient_sym.upper()
        print()
        if(patient_sym=="Y" or patient_sym=="S"):
            jkl.append('2')
            sym_list.append("Nasal Congestion")
        #3
        print("Chest pain?")
        os.system("espeak 'Do you suffer from chest pain'")
        patient_sym=input()
        patient_sym=patient_sym.upper()
        print()
        if(patient_sym=="Y" or patient_sym=="S"):
            jkl.append('3')
            sym_list.append("Chest Pain")
        #4
        print("Rise in temperature during evenings and nights?")
        os.system("espeak 'Do you have sudden rise in temperature during evenings and nights?'")
        patient_sym=input()
        patient_sym=patient_sym.upper()
        print()
        if(patient_sym=="Y" or patient_sym=="S"):
            jkl.append('4')
            sym_list.append("Sudden rise in Temperature")
        #5
        print("Mild fever?")
        os.system("espeak 'Do you suffer from mild fever'")
        patient_sym=input()
        patient_sym=patient_sym.upper()
        print()
        if(patient_sym=="Y" or patient_sym=="S"):
            jkl.append('5')
            sym_list.append("Mild Fever")
        #6
        print("Sudden weight loss?")
        os.system("espeak 'Do you suffer from sudden weight loss'")
        patient_sym=input()
        patient_sym=patient_sym.upper()
        print()
        if(patient_sym=="Y" or patient_sym=="S"):
            jkl.append('6')
            sym_list.append("Sudden Weight Loss")
        #7
        print("Heavy fever?")
        os.system("espeak 'Do you suffer from heavy fever'")
        patient_sym=input()
        patient_sym=patient_sym.upper()
        print()
        if(patient_sym=="Y" or patient_sym=="S"):
            jkl.append('7')
            sym_list.append("Heavy Fever")
        #8
        print("Runny nose?")
        os.system("espeak 'Do you suffer from running nose?'")
        patient_sym=input()
        patient_sym=patient_sym.upper()
        print()
        if(patient_sym=="Y" or patient_sym=="S"):
            jkl.append('8')  
            sym_list.append("Running Nose")
        for i in jkl:
            if(i in ['1','3','4','6']):
                cnt1+=1
            if(i in ['2','5','7','8']):
                cnt2+=1
        if(cnt1>cnt2):
            dis="TUBERCULOSIS"
        else:
            dis="COMMON COLD"
        print()
        print("***************************")
        print()
        print("You are affected by %s"%dis)
        flag=1
        print()
        print("***************************")
        print()
if((('3' in kjj) or ('4'in kjj))and (flag==0)):
    jkl=[]
    print("1. Heart burn (or) Regurgitation?\n2. Blood in stool?\n3. Nausea?\n4. Itchiness around the anus?\n5. Severe Abdominal pain?\n6. Muscle cramp?")
    print()
    #1
    print("Heart burn (or) Regurgitation?")
    os.system("espeak 'Do you suffer from heart burn'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('1')
        sym_list.append("Heart Burn")
    #2
    print("Blood in stool?")
    os.system("espeak 'Do you suffer from blood in stool'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('2')
        sym_list.append("Blood in Stool")
    #3
    print("Nausea?")
    os.system("espeak 'Do you suffer from nausea'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('3')
        sym_list.append("Nausea")
    #4
    print("Itchiness around the anus?")
    os.system("espeak 'Do you suffer from itchiness around the anus'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('4')
        sym_list.append("Itchiness aroung the anus")
    #5
    print("Severe Abdominal pain?")
    os.system("espeak 'Do you suffer from severe abdominal pain'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('5')
        sym_list.append("Severe Abdominal Pain")
    #6
    print("Muscle cramp?")
    os.system("espeak 'Do you suffer from muscle cramp'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('6')
        sym_list.append("Muscle Cramp")
    for i in jkl:
        if(i in ['1','3','5','7']):
            cnt1+=1
        if(i in ['2','3','4','6']):
            cnt2+=1
    if(cnt1>cnt2):
        dis="GASTRIC ULCER"
    else:
        dis="WORM INFESTATION"
    print()
    print("***************************")
    print()
    print("You are affected by %s"%dis)
    flag=1
    print()
    print("***************************")
    print()
if((('5' in kjj) or ('6'in kjj))and (flag==0)):
    jkl=[]
    print("1. Extreme thirst?\n2. Tiredness?\n3. Dark coloured urine?\n4. Fast heart rate?\n5. Breathlessness?\n6. Confusion?\n7. Fainting episodes?")
    print()
    #1
    print("Extreme thirst?")
    os.system("espeak 'Do you suffer from extreme thirst'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('1')
        sym_list.append("Extreme Thirst")
    #2
    print("Tiredness?")
    os.system("espeak 'Do you suffer from tiredness'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('2')
        sym_list.append("Tiredness")
    #3
    print("Dark coloured urine?")
    os.system("espeak 'Do you suffer from dark coloured urine'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('3')
        sym_list.append("Dark coloured urine")
    #4
    print("Fast heart rate?")
    os.system("espeak 'Do you suffer from fast heart rate'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('4')
        sym_list.append("Fast Heart Rate")
    #5
    print("Breathlessness?")
    os.system("espeak 'Do you suffer from breathlessness'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('5')
        sym_list.append("Breathlessness")
    #6
    print("Confusion?")
    os.system("espeak 'Do you suffer from confusion'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('6')
        sym_list.append("Confusion")
    #7
    print("Fainting episodes?")
    os.system("espeak 'Do you suffer from fainting episodes'")
    patient_sym=input()
    patient_sym=patient_sym.upper()
    print()
    if(patient_sym=="Y" or patient_sym=="S"):
        jkl.append('7')
        sym_list.append("Fainting episodes")
    for i in jkl:
        if(i in ['1','2','3','6']):
            cnt1+=1
        if(i in ['2','4','5','7']):
            cnt2+=1
    if(cnt1>cnt2):
        dis="DEHYDRATION"
    else:
        dis="ANAEMIA"
    print()
    print("***************************")
    print()
    os.system("espeak 'Predicting the disease'")
    os.system("espeak 'Loading'")
    os.system("espeak 'approximately predicting the diseases '")
    print("You was affected by %s"%dis)
    flag=1
    print()
    print("***************************")
    print()
cliniconUpdateData(patient_ID,"SELECTED SYMPTOMS",sym_list)
with open(patient_ID+".doc","a") as f:
    print("SELECTED SYMPTOMS: ",file=f)
    for hjk in sym_list:
        print(hjk,file=f)
    print(40*"=",file=f)
os.system("espeak 'it is approximately predicted that you were affected by %s'"%dis)
cliniconUpdateData(patient_ID,"PREDICTED DISEASES",dis)
with open(patient_ID+".doc","a") as f:
    print("PREDICTED DISEASES: %s"%dis,file=f)
    print("\n")
print("Take the following medicines:")
os.system("espeak 'Take the following medicines'")
imgg=cv2.imread('12.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
print()
if(dis=="MALARIA"):
    print(" Tab. chloroquine\n(600mg) – Initially\n(300mg) - After 8 hours\n(300mg) – Once daily for the NEXT 2 DAYS.\n\n Tab. primaquine (15mg)\nONCE DAILY FOR 14 DAYS.")
    print()
    cliniconUpdateData(patient_ID,"MEDICINE PRESCRIBED","Tab. chloroquine\n(600mg) – Initially\n(300mg) - After 8 hours\n(300mg) – Once daily for the NEXT 2 DAYS.\n\n Tab. primaquine (15mg)\nONCE DAILY FOR 14 DAYS.")
    print("YOU WERE AFFECTED BY SERIOUS DISEASES\nPLEASE GO TO THE NEARBY PUBLIC HEALTH CARE CENTER.")
    os.system("espeak 'YOU WERE AFFECTED BY SERIOUS DISEASES PLEASE GO TO THE NEARBY PUBLIC HEALTH CARE CENTER.'")
    print("THE REPORT IS SENT TO THE MEDICAL FACILITY FOR IMMEDIATE ATTENTION")
    os.system("espeak 'THE REPORT IS SENT TO THE MEDICAL FACILITY FOR IMMEDIATE ATTENTION'")
    with open(patient_ID+".doc","a") as f:
        print("\n Tab. chloroquine\n(600mg) – Initially\n(300mg) - After 8 hours\n(300mg) – Once daily for the NEXT 2 DAYS.\n\n Tab. primaquine (15mg)\nONCE DAILY FOR 14 DAYS.",file=f)
        print("YOU WERE AFFECTED BY SERIOUS DISEASES\nPLEASE GO TO THE NEARBY PUBLIC HEALTH CARE CENTER.\n")
        print("THE REPORT IS SENT TO THE MEDICAL FACILITY FOR IMMEDIATE ATTENTION\n")
elif(dis=="TYPHOID FEVER"):
    print(" Tab. ciprofloxacin (750mg)\n(TWICE DAILY AFTER FOOD)\n(ONCE IN THE MORNING AND ONCE IN THE NIGHT FOR 10 DAYS)\n\n Tab. Paracetamol (500mg)\n(During the increase of fever)")
    print()
    cliniconUpdateData(patient_ID,"MEDICINE PRESCRIBED","Tab. ciprofloxacin (750mg)\n(TWICE DAILY AFTER FOOD)\n(ONCE IN THE MORNING AND ONCE IN THE NIGHT FOR 10 DAYS)\n\n Tab. Paracetamol (500mg)\n(During the increase of fever)")
    print("YOU WERE AFFECTED BY SERIOUS DISEASES\nPLEASE GO TO THE NEARBY PUBLIC HEALTH CARE CENTER.")
    os.system("espeak 'YOU WERE AFFECTED BY SERIOUS DISEASES PLEASE GO TO THE NEARBY PUBLIC HEALTH CARE CENTER.'")
    print("THE REPORT IS SENT TO THE MEDICAL FACILITY FOR IMMEDIATE ATTENTION")
    os.system("espeak 'THE REPORT IS SENT TO THE MEDICAL FACILITY FOR IMMEDIATE ATTENTION'")
    with open(patient_ID+".doc","a") as f:
        print("\n Tab. ciprofloxacin (750mg)\n(TWICE DAILY AFTER FOOD)\n(ONCE IN THE MORNING AND ONCE IN THE NIGHT FOR 10 DAYS)\n\n Tab. Paracetamol (500mg)\n(During the increase of fever)",file=f)
        print("YOU WERE AFFECTED BY SERIOUS DISEASES\nPLEASE GO TO THE NEARBY PUBLIC HEALTH CARE CENTER.\n")
        print("THE REPORT IS SENT TO THE MEDICAL FACILITY FOR IMMEDIATE ATTENTION\n")
elif(dis=="TUBERCULOSIS"):
    print(" Tab. isoniazid (300mg)\n Tab. rifampicin (600mg)\n Tab. pyrazinamide (1500mg)\n Tab. ethambutol (800mg)\n(ONCE DAILY FOR 2 MONTHS)\n\n Tab. isoniazid (300mg)\n Tab. rifampicin (600mg)\n(ONCE DAILY FOR THE NEXT FOUR MONTHS)")
    print()
    cliniconUpdateData(patient_ID,"MEDICINE PRESCRIBED","Tab. isoniazid (300mg)\n Tab. rifampicin (600mg)\n Tab. pyrazinamide (1500mg)\n Tab. ethambutol (800mg)\n(ONCE DAILY FOR 2 MONTHS)\n\n Tab. isoniazid (300mg)\n Tab. rifampicin (600mg)\n(ONCE DAILY FOR THE NEXT FOUR MONTHS)")
    print("YOU WERE AFFECTED BY SERIOUS DISEASES\nPLEASE GO TO THE NEARBY PUBLIC HEALTH CARE CENTER.")
    os.system("espeak 'YOU WERE AFFECTED BY SERIOUS DISEASES PLEASE GO TO THE NEARBY PUBLIC HEALTH CARE CENTER.'")
    print("THE REPORT IS SENT TO THE MEDICAL FACILITY FOR IMMEDIATE ATTENTION")
    os.system("espeak 'THE REPORT IS SENT TO THE MEDICAL FACILITY FOR IMMEDIATE ATTENTION'")
    with open(patient_ID+".doc","a") as f:
        print("\n Tab. isoniazid (300mg)\n Tab. rifampicin (600mg)\n Tab. pyrazinamide (1500mg)\n Tab. ethambutol (800mg)\n(ONCE DAILY FOR 2 MONTHS)\n\n Tab. isoniazid (300mg)\n Tab. rifampicin (600mg)\n(ONCE DAILY FOR THE NEXT FOUR MONTHS)",file=f)
        print("YOU WERE AFFECTED BY SERIOUS DISEASES\nPLEASE GO TO THE NEARBY PUBLIC HEALTH CARE CENTER.\n")
        print("THE REPORT IS SENT TO THE MEDICAL FACILITY FOR IMMEDIATE ATTENTION\n")
elif(dis=="COMMON COLD"):
    print(" Tab. cetirizine (10mg)\n(ONCE DAILY FOR 3 DAYS)\n\n Tab. paracetamol (500mg)\n(WHENEVER IT OCCURS)")
    cliniconUpdateData(patient_ID,"MEDICINE PRESCRIBED","Tab. cetirizine (10mg)\n(ONCE DAILY FOR 3 DAYS)\n\n Tab. paracetamol (500mg)\n(WHENEVER IT OCCURS)")
    with open(patient_ID+".doc","a") as f:
        print(" Tab. cetirizine (10mg)\n(ONCE DAILY FOR 3 DAYS)\n\n Tab. paracetamol (500mg)\n(WHENEVER IT OCCURS)",file=f)
elif(dis=="GASTRIC ULCER"):
    print(" Cap. Omeprazole (20mg)\n(TWICE DAILY FOR 7 DAYS)\n(30 MINUTES BEFORE FOOD)")
    cliniconUpdateData(patient_ID,"MEDICINE PRESCRIBED","Cap. Omeprazole (20mg)\n(TWICE DAILY FOR 7 DAYS)\n(30 MINUTES BEFORE FOOD)")
    with open(patient_ID+".doc","a") as f:
        print("\n Cap. Omeprazole (20mg)\n(TWICE DAILY FOR 7 DAYS)\n(30 MINUTES BEFORE FOOD)",file=f)
elif(dis=="WORM INFESTATION"):
    print(" Tab. albendazole (400mg)\nImmediately after diagnosis\n(TAKE ONE TABLET IMMEDIATELY AND THE NEXT TABLET AFTER A GAP OF TWO WEEKS)")
    cliniconUpdateData(patient_ID,"MEDICINE PRESCRIBED","Tab. albendazole (400mg)\nImmediately after diagnosis\n(TAKE ONE TABLET IMMEDIATELY AND THE NEXT TABLET AFTER A GAP OF TWO WEEKS)")
    with open(patient_ID+".doc","a") as f:
        print("\n Tab. albendazole (400mg)\nImmediately after diagnosis\n(TAKE ONE TABLET IMMEDIATELY AND THE NEXT TABLET AFTER A GAP OF TWO WEEKS)",file=f)
elif(dis=="DEHYDRATION"):
    print(" ORS (ORAL REHYDRATION SOLUTION)\nImmediately after diagnosis")
    cliniconUpdateData(patient_ID,"MEDICINE PRESCRIBED","ORS (ORAL REHYDRATION SOLUTION)\nImmediately after diagnosis")
    with open(patient_ID+".doc","a") as f:
        print("\n ORS (ORAL REHYDRATION SOLUTION)\nImmediately after diagnosis",file=f)
elif(dis=="ANAEMIA"):
    print(" Tab. ferrous sulphate (200mg)\n(TWICE DAILY FOR 1 MONTH)")
    cliniconUpdateData(patient_ID,"MEDICINE PRESCRIBED","Tab. ferrous sulphate (200mg)\n(TWICE DAILY FOR 1 MONTH)")
    with open(patient_ID+".doc","a") as f:
        print("\n Tab. ferrous sulphate (200mg)\n(TWICE DAILY FOR 1 MONTH)",file=f)
print("\n\n*** THANK YOU FOR VISITING CLINICON ***")
with open(patient_ID+".doc","a") as f:
    print(40*"=",file=f)
    print("\n*** THANK YOU FOR VISITING CLINICON ***",file=f)
    print(40*"=",file=f)
c_filename=patient_ID+".doc"
os.system("espeak 'Thank you for visiting clini con'")
imgg=cv2.imread('13.png')
cv2.imshow('CLINICON',imgg)
cv2.waitKey(2000)
cv2.destroyAllWindows()
os.system('libreoffice %s'%c_filename)

