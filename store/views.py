from django.shortcuts import render, get_object_or_404,redirect
from .models import  Category, Product ,Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
#from ecommerce.payments.forms import ShippingForm
#from ecommerce.payments.models import ShippingAddress
from django import forms
#from django.db.models import Q
import json
#rom ecommerce.templates.cart import Cart
"""
def search(request):
	# Determine if they filled out the form
	if request.method == "POST":
		searched = request.POST['searched']
		# Query The Products DB Model
		searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
		# Test for null
		if not searched:
			messages.success(request, "That Product Does Not Exist...Please try Again.")
			return render(request, "search.html", {})
		else:
			return render(request, "search.html", {'searched':searched})
	else:
		return render(request, "search.html", {})	
"""
"""
def update_info(request):
	if request.user.is_authenticated:
		# Get Current User
		current_user = Profile.objects.get(user__id=request.user.id)
		# Get Current User's Shipping Info
		shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
		
		# Get original User Form
		form = UserInfoForm(request.POST or None, instance=current_user)
		# Get User's Shipping Form
		shipping_form = ShippingForm(request.POST or None, instance=shipping_user)		
		if form.is_valid() or shipping_form.is_valid():
			# Save original form
			form.save()
			# Save shipping form
			shipping_form.save()

			messages.success(request, "Your Info Has Been Updated!!")
			return redirect('home')
		return render(request, "update_info.html", {'form':form, 'shipping_form':shipping_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')



def update_password(request):
	if request.user.is_authenticated:
		current_user = request.user
		# Did they fill out the form
		if request.method  == 'POST':
			form = ChangePasswordForm(current_user, request.POST)
			# Is the form valid
			if form.is_valid():
				form.save()
				messages.success(request, "Your Password Has Been Updated...")
				login(request, current_user)
				return redirect('update_user')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)
					return redirect('update_password')
		else:
			form = ChangePasswordForm(current_user)
			return render(request, "update_password.html", {'form':form})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
"""	
def update_user(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		user_form = UpdateUserForm(request.POST or None, instance=current_user)

		if user_form.is_valid():
			user_form.save()

			login(request, current_user)
			messages.success(request, "User Has Been Updated!!")
			return redirect('home')
		return render(request, "update_user.html", {'user_form':user_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')


def category_summary(request):
	categories = Category.objects.all()
	return render(request, 'category_summary.html', {"categories":categories})	

def category(request, foo):
	# Replace Hyphens with Spaces
	foo = foo.replace('-', ' ')
	# Grab the category from the url
	try:
		# Look Up The Category
		category = Category.objects.get(name=foo)
		products = Product.objects.filter(category=category)
		return render(request, 'category.html', {'products':products, 'category':category})
	except:
		messages.success(request, ("That Category Doesn't Exist..."))
		return redirect('store')


def product(request,pk):
	product = Product.objects.get(id=pk)
	return render(request, 'store/product.html', {'product':product})

def store(request):
    #categories = Category.objects.all()
    products = Product.objects.all()
    #context = {
        #'categories': categories,
        #'products': products,
    #}
    return render(request, 'store/store.html', {'products':products})

def about(request):
	return render(request, 'store/about.html', {})

def rings(request):
	return render(request, 'store/rings.html', {})

def earrings(request):
	return render(request, 'store/earrings.html', {})

def necklace(request):
	return render(request, 'store/necklace.html', {})

def login_user(request):
	#return render(request, 'store/login.html', {})

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			"""
			# Do some shopping cart stuff
			current_user = Profile.objects.get(user__id=request.user.id)
			# Get their saved cart from database
			saved_cart = current_user.old_cart
			# Convert database string to python dictionary
			if saved_cart:
				# Convert to dictionary using JSON
				converted_cart = json.loads(saved_cart)
				# Add the loaded cart dictionary to our session
				# Get the cart
				cart = Cart(request)
				# Loop thru the cart and add the items from the database
				for key,value in converted_cart.items():
					cart.db_add(product=key, quantity=value)
		"""
			messages.success(request, ("You Have Been Logged In!"))
			return redirect('store')
		else:
			messages.success(request, ("There was an error, please try again..."))
			return redirect('login')

	else:
		return render(request, 'store/login.html', {})


def logout_user(request):

	logout(request)
	messages.success(request, ("You have been logged out...Thanks for stopping by..."))
	return redirect('home')

def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Username Created - Please Fill Out Your User Info Below..."))
			return redirect('update_info')
		else:
			messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
			return redirect('register')
	else:
		return render(request, 'register.html', {'form':form})



@login_required
def profile(request):
    return render(request, 'store/profile.html')

@login_required
def profile_section(request, section):
    if section == 'Orders':
        return render(request, 'store/orders.html')
    elif section == 'Wishlist':
        return render(request, 'store/wishlist.html')
    elif section == 'Preferences':
        return render(request, 'store/preferences.html')
    else:
        return render(request, 'store/404.html')  # Or redirect to a 404 page

@login_required
def my_account(request):
    # Handle logic for user account details
    return render(request, 'my_account.html')

@login_required
def orders(request):
    # Handle logic for displaying user orders
    return render(request, 'orders.html')

@login_required
def wishlist(request):
    # Handle logic for displaying user wishlist
    return render(request, 'wishlist.html')
@login_required
def preferences(request):
    # Handle logic for user preferences
    return render(request, 'preferences.html')

