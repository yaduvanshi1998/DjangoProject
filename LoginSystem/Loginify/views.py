from django.shortcuts import render, HttpResponse, redirect
from .models import UserDetails
from django.contrib import messages
from Loginify.serializer import UserDetailsSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# ---------------------- login method --------------------------------

@csrf_exempt # this csfr_exempt must be used when we are not using html, and testing api thorugh postman
def login(request):
    try:
        if request.method=="POST":
            email = request.POST.get("Email")
            password = request.POST.get("Password")
            if not UserDetails.objects.filter(Email=email, Password=password).exists():
                error = messages.error(request, "Enter the correct credentials")
                return render(request, "login.html", {'error': error})
            else:
                success = messages.success(request, "you have been successfully logged in!")
                return render(request, "base.html", {'message': success})
    except Exception as e:
        return render(request, 'login.html', {'error': str(e)})

    return render(request,"login.html")


# ------------- nodrmal signup method without serializer ---------------------

# def signup(request):
#     try:
#         if request.method == "POST":
#             username = request.POST.get('username')
#             email = request.POST.get('email')
#             password = request.POST.get('password')

#             if UserDetails.objects.filter(Email=email).exists():  # Check if user with this email already exists
#                 print("Error: user with this email already exists!")
#                 messages.error(request, "User with this email already exists!")
#                 return redirect('signup')

#             data = UserDetails(Username=username, Email=email, Password=password) # Save new user
#             data.save()
#             print("Success: User registered successfully!")
#             messages.success(request, "User registered successfully!")
#             return redirect('login')  # Use the name of your login view, not a file path
#     except Exception as e:
#         return render(request, 'signup.html', {'error': str(e)})

#     return render(request, 'signup.html')


# ------------------------ signup method with serializer ----------------------

@csrf_exempt # this csfr_exempt must be used when we are not using html, and testing api thorugh postman
def signup(request):
    try:
        if request.method == "POST":
            serialized_data = UserDetailsSerializer(data=request.POST.dict())

            if serialized_data.is_valid():
                serialized_data.save()
                messages.success(request,  "User registered successfully!")
                return redirect('login')
            else:
                # Error from a specific field (e.g., 'Username' or 'Email')
                if 'Username' in serialized_data.errors:
                    messages.error(request, serialized_data.errors['Username'][0])
                    return render(request, 'signup.html', {'error': serialized_data.errors['Username'][0]})
                elif 'Email' in serialized_data.errors:
                    messages.error(request, serialized_data.errors['Email'][0])
                    return render(request, 'signup.html', {'error': serialized_data.errors['Email'][0]})
                else:
                    messages.error(request, "Invalid input")
                    return render(request, 'signup.html', {'error': "Invalid input"})
    except Exception as e:
        return render(request, 'signup.html', {'error': str(e)})

    return render(request, 'signup.html')


def get_all_userdetails(request):
    try:
        if request.method=="GET":
            data = UserDetails.objects.all() # Queryset O/P
            serialized_data = UserDetailsSerializer(data, many=True) # serialized O/P
            return JsonResponse(serialized_data.data, safe=False, status=200) # status=200  ----- success
        else:
            return JsonResponse({'error': 'Only GET requests are allowed'}, status=405) # status=405 --- method not allowed
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500) # status=500 --- internal server error
