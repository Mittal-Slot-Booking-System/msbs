from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from .models import Transaction
from django.views.decorators.csrf import csrf_exempt
import base64,hashlib,requests,json
import datetime
import reportlab
from reportlab.pdfgen import canvas
APIEndpoint="/pg/v1/pay"
SaltKey="099eb0cd-02cf-4e2a-8aca-3e6c6aff0399"
SaltIndex="###1"
url="https://api-preprod.phonepe.com/apis/merchant-simulator/pg/v1/pay"
@csrf_exempt
def pay(request):
    if request.method=='POST':
        Payload={}
        Payload["merchantId"]="MERCHANTUAT"
        time=str(datetime.datetime.now().isoformat().replace("-","_").replace(":","_").replace(".","_"))
        merchantTransactionId=str(request.user.username)+str(datetime.datetime.now().isoformat().replace("-","_").replace(":","_").replace(".","_"))
        merchantUserID='MSBS'+str(request.user.username)
        Payload["merchantTransactionId"]=merchantTransactionId
        Payload["merchantUserId"]=merchantUserID
        Payload["amount"]=200000
        Payload["redirectUrl"]="http://127.0.0.1:8000/pay/callback/"
        Payload["redirectMode"]="POST"
        Payload["callbackUrl"]="https://webhook.site/callback-url"
        Payload["mobileNumber"]="9999999999"
        Payload["paymentInstrument"]={"type": "PAY_PAGE"}
        toencodestring=json.dumps(Payload)
        string_bytes=toencodestring.encode("utf-8")
        base64_bytes=base64.b64encode(string_bytes)
        request=base64_bytes.decode("utf-8")
        tosha256=request+APIEndpoint+SaltKey
        sha256string=hashlib.sha256(tosha256.encode('utf-8')).hexdigest()
        checksum=sha256string+SaltIndex
        print(merchantTransactionId,checksum,request)
        transaction_made=Transaction(time=time,amount=200000,checksum_before=checksum,transactionID=merchantTransactionId,userID=merchantUserID)
        transaction_made.save()
        payload={"request":request}
        headers={
            "accept":"application/json",
            "Content-Type":"application/json",
            "X-VERIFY":checksum
        }
        response=requests.post(url,json=payload,headers=headers)
        p=response.text.index('"url":')
        p+=7
        s=''
        while response.text[p]!='"':
            s+=response.text[p]
            p+=1
        return redirect(s)
    else:
        return render(request,'payments\pay.html')
def callback(request):
    if request.method=='POST':
        print(request.POST)
        print(request.POST['checksum'])
        responsecode=request.POST['code']
        merchantID=request.POST['merchantId']
        transactionID=request.POST['transactionId']
        checksum=request.POST['checksum']
        statusurl="https://api-preprod.phonepe.com/apis/pg-sandbox/pg/v1/status/"+str(merchantID)+'/'+str(transactionID)
        headers={}
        headers["accept"]="application/json"
        headers["Content-Type"]="application/json"
        tosha256='/pg/v1/status/'+str(merchantID)+'/'+str(transactionID)+SaltKey
        sha256string=hashlib.sha256(tosha256.encode('utf-8')).hexdigest()
        checksum=sha256string+SaltIndex
        headers["X-VERIFY"]=checksum
        headers["X-MERCHANT-ID"]=merchantID
        response = requests.get(statusurl, headers=headers)
        print(type(response))
        p=response.text.index('"code":')
        p+=8
        s=''
        while response.text[p]!='"':
            s+=response.text[p]
            p+=1
        if s=="PAYMENT_SUCCESS":
            response=json.loads(response.text)
            print(type(response))
            context={}
            context['code']=1
            context['success']=response["success"]
            context['message']=response["message"]
            context['transactionID']=response["data"]["merchantTransactionId"]
            context['paymentType']=response['data']['paymentInstrument']['type']
            context['pgtransactionID']=response['data']['paymentInstrument']['pgServiceTransactionId']
            transaction=Transaction.objects.get(transactionID=context['transactionID'])
            transaction.PGtransactionID=context['pgtransactionID']
            transaction.save()
            print(transaction)
            return render(request,'payments\callback.html',context)
