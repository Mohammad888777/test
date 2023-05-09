from kavenegar import * 
from datetime import datetime

def send_otp(phone_number,code):
    try:
        api = KavenegarAPI('5A4579655330475A4F6674624D4151676C54346A374C536D56464339375344673051774B5659543055546F3D') 
        params = {
              'sender' : '1000596446', 
              'receptor': phone_number, 
              'message' :f"{code}  کد تایید "
              } 
    
        response = api.sms_send( params) 

        print(response)
    except Exception as e:
        print(e)





def findTimeDiffrence(time_1,time_2):
    
    # time_1_to_jalili=datetime2jalali(time_1)
    fmt = '%H:%M:%S'
    time_1_to_str=time_1.strftime(fmt)

    s1=""
    for i in time_1_to_str:
        if i == ".":
            break
        else:
            s1+=i
    s1=s1.replace(":","")

    time_2_to_str=time_2.time().strftime(fmt)
    time_2_to_str=time_2_to_str.replace(":","")

    time1=datetime.strptime(s1,"%H%M%S")
    time2=datetime.strptime(time_2_to_str,"%H%M%S")

    return time1-time2