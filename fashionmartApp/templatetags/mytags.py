from django.shortcuts import redirect
from django import template
from fashionmartApp.models import Checkout,CheckoutProduct

register = template.Library()

@register.filter(name='checkoutProduct')
def checkoutProduct(checkoutid):
    try:
        checkout = Checkout.objects.get(id=checkoutid)
        cp = CheckoutProduct.objects.filter(checkout=checkout)
        c = []
        for item in cp:
            x = {'name':item.p.name,'maincategory':item.p.maincategory,'subcategory':item.p.subcategory,'brand':item.p.brand,'color':item.p.color,'size':item.p.size,'price':item.p.finalprice,'qty':item.qty,'total':item.total,'pic':item.p.pic1.url}
            c.append(x)
        return c
    except:
        return redirect('/cart')
    

@register.filter(name='paymentStatus')
def paymentStatus(op):
    if(op==0):
        return "Pending"
    else:
        return "Done"
    

@register.filter(name='paymentMode')
def paymentMode(op):
    if(op==0):
        return "COD"
    else:
        return "Net Banking"
    

@register.filter(name='orderStatus')
def orderStatus(op):
    if(op==0):
        return "Order Placed"
    elif(op==1):
        return "Not Packed"
    elif(op==2):
        return "Packed"
    elif(op==3):
        return "Ready to Ship"
    elif(op==4):
        return "Shipped"
    elif(op==5):
        return "Out For Delevery"
    elif(op==6):
        return "Delivered"
    else:
        return "Cancelled"