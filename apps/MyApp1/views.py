from django.shortcuts import render

# Create your views here.

# This the first screen which has login form of Agent
def LoginViewMethod(request):
    # print('Agent Login form calling...')
    formData = {
        'AgentId':'0101AI',
        'LoginId':'asdfasdf',
        'Password':'asdfasdf',
    }
    return render(request, 'Login.html', formData)
