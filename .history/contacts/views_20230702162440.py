from django.shortcuts import render

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        
        contact = Contact(listing=listing, listing_id = listing_id, name = name, email = email,
        phone=phone, message=message, user_id=user_id)
