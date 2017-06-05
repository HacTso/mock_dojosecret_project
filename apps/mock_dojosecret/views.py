from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Secret
from django.db.models import Count
# Create your views here.
def index(request):
	context = {
		"user" : User.objects.all()
	}
	# print "hello"
	# u1 = User.objects.get(id=1)
	# print context['username']
	# print user
	return render(request, 'mock_dojosecret/index.html', context)

def register_process(request):
	# print "hello, reg"
	postData = {
		'username' : request.POST['username'], 
		'email' : request.POST['email'], 
		'password' : request.POST['password'], 
		'confirm_password' : request.POST['confirm_password']
		}
	# print postData
	user = User.objects.register(postData)
	# print user
	if 'error' in user:
		messages.info(request, user['error'])
		return redirect('/')

	if 'loginUser' in user:
		request.session['id'] = user['loginUser'].id
		# print request.session['id']
		# print user['loginUser'].username
    	request.session['name'] = user['loginUser'].username
    	# print request.session['name']
    	return redirect('/secrets')

    

def login_process(request):
    postData = { 
        'email' : request.POST['email'], 
        'password' : request.POST['password'] 
    }
    # print postData
    user = User.objects.login(postData)
    # print user
    if 'error' in user:
        messages.info(request, user['error'])
        return redirect('/')

    if 'loginUser' in user:
        request.session['id'] = user['loginUser'].id
        request.session['name'] = user['loginUser'].username
    	return redirect('/secrets')
        # return render(request, 'mock_dojosecret/secrets.html')
    	# print "successful"
    	# return redirect('/')
        # print request.session['id']
        # print request.session['name']

def secrets_process(request):
	print "step 1"
	new_secret = Secret.objects.secret_validation(request.POST['secret_text'], request.session['id'])
	print "step 4", new_secret
	if 'error' in new_secret:
		messages.info(request, new_secret['error'])
		# print "step 5", new_secret['error']
		return redirect('/secrets')
	# messages.error(request, new_secret['error'])
	return redirect('/secrets')

def secrets(request):
	if checkForLogin(request):
		secretHistory = Secret.objects.all().order_by('-id')
		secret_record = {
			"secrets" : secretHistory,
			"loginUser" : User.objects.get(id = request.session['id']) 
		}
		print "step 6"
		return render(request, 'mock_dojosecret/secrets.html', secret_record)
	else:
		return redirect('/')


def show_popular(request):
	return render(request, 'mock_dojosecret/popular.html')

def logout(request):
	request.session.clear()
	# try:
	# 	del request.session['id']
	# except KeyError:
	# 	pass
	return redirect('/')

def checkForLogin(request):
	if 'id' not in request.session:
		messages.error(request, "Please login to view the requested page", exta_tags="register_process")
		return False
	return True




















