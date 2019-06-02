# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pyscreenshot as pys
from django.shortcuts import render, HttpResponse
from django.template import RequestContext
# Create your views here.

def user_home(request):
    try:
        return render(request, 'p2/filee.html')
    except:
        print('error')


def BCA_quiz(request):
    try:
        print("hey")
        if request.method == 'POST':
            #con = {}
            print("hey2")
            uu = request.POST['user']
            email = request.POST['email']
            print(uu)
            print("hey3")
            # print(user)
            request.session['username'] = uu
            request.session['email'] = email
            userid = request.session['username']
            email = request.session['email']
            if userid:
                print userid
                return render(request, 'p2/BCA_quiz.html')
            else:
                print("error")
        else:
            print("error1")
    except:
        print('error2')



def quiz(request):
    try:
        i = 0
        file = open("output.txt","a")
        print("fmskngs")
        if request.method == 'POST':
            print("ffwfwfwwf")
            the_userid = request.session['username']
            email = request.session['email']
            if the_userid:
            #con = {}
                print("hey2")
                qus1 = request.POST['qus1']
                qus2 = request.POST['qus2']
                # print(qus1)
                # print(qus2)
                qus3 = request.POST['qus3']
                qus4 = request.POST['qus4']
                qus5 = request.POST['qus5']
                qus6 = request.POST['qus6']
                qus7 = request.POST['qus7']
                qus8 = request.POST['qus8']
                qus9 = request.POST['qus9']
                qus10 = request.POST['qus10']
                qus11 = request.POST['qus11']
                qus12 = request.POST['qus12']
                qus13 = request.POST['qus13']
                qus14 = request.POST['qus14']
                qus15 = request.POST['qus15']
                qus16 = request.POST['qus16']
                qus17 = request.POST['qus17']
                qus18 = request.POST['qus18']
                qus19 = request.POST['qus19']
                qus20 = request.POST['qus20']
                print("hey")
                print(qus1)
                print(qus2)
                print(qus3)
                print(qus4)
                print(qus5)
                print(qus6)
                print(qus7)
                print(qus8)
                print(qus9)
                print(qus10)
                print(qus11)
                print(qus12)
                print(qus13)
                print(qus14)
                print(qus15)
                print(qus16)
                print(qus17)
                print(qus18)
                print(qus19)
                print(qus20)
                if qus1 == "hexadecimal":
                    i += 1
                else:
                    i += 0
                print(i)
                
            
                if qus2 == "Efficient in accessing an entry":
                    i += 1
                else:
                    i +=0
                print(i)

                if qus3 == "Soft computing represents a real paradigm shift in the way in which systems are deployed":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus4 == "Immersive":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus5 == "The number of subscripts determines the dimension of the array":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus6 == "Function":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus7 == "CppBuzz.com11":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus8 == "PIP":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus9 == "A linear search requires a sorted list.":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus10 == "d e b f g c a":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus11 == "ptr is a pointer to an array of 10 integers":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus12 == "50 km":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus13 == "1200":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus14 == "Rs. 1020":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus15 == "50400":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus16 == "4":
                    i += 1
                else:
                    i += 0
                print(i)

                if qus17 == "10 min":
                    i += 1
                else:
                    i +=0
                print(i)

                if qus18 == "5040":
                    i += 1
                else:
                    i +=0
                print(i)

                if qus19 == "None of these":
                    i += 1
                else:
                    i +=0
                print(i)

                if qus20 == "dus lap ugli":
                    i += 1
                else:
                    i +=0
                print(i)


                output = i
                print(email)
                print(output)
                file.write(the_userid + " , " + email + " , " + str(output) + " \n ")
                
                # file_content = file.read()
                # fl = f.readlines()
                # ll.append(the_userid)
                context = {
                    'message': the_userid,
                }

                return render(request, 'p2/submitted.html', context)
            
            else:
                print("error")    
                # user = request.POST.get('username')
                # print user
                # print("kjkfd")
                # print("hey3")
                # print(user)
                # request.session['username'] = user
                # userid = request.session['username']
                # if userid:
                #return render(request, 'p2/filee.html')
        else:
            print("error1")
    except:
        print('error2')
    


