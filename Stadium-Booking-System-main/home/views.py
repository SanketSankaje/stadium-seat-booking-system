# This file is used for actual functioning of a webpage
# Each function renders a page represented by funcions name and returns some context (date/values) to that webpage.

from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from home.models import Book
from .db1 import cur
import datetime
from home import db1

# --------------------------------------------------------------------------------------------------------

show = email = date = attendees = tier = tid = None

# --------------------------------------------------------------------------------------------------------

def index(response):
    """
        This is Index function and deals with Home webpage.
        The context return information for stadiums like tierwise remaining seats and prices.
    """

    x, xx = db1.get_seats('Sol Colosseum')
    y, yy = db1.get_seats('Domus Flau')

    print(x[0][0][0])
    context = {
        "a" : x[0][0][0],
        "b" : x[1][0][0],
        "c" : x[2][0][0],
        "d" : x[3][0][0],
        "e" : x[4][0][0],

        "aa" : xx[0][0][0],
        "bb" : xx[1][0][0],
        "cc" : xx[2][0][0],
        "dd" : xx[3][0][0],
        "ee" : xx[4][0][0],

        "a1" : y[0][0][0],
        "b1" : y[1][0][0],
        "c1" : y[2][0][0],
        "d1" : y[3][0][0],
        "e1" : y[4][0][0],

        "aa1" : yy[0][0][0],
        "bb1" : yy[1][0][0],
        "cc1" : yy[2][0][0],
        "dd1" : yy[3][0][0],
        "ee1" : yy[4][0][0]

    }
    return render(response, 'index.html', context)

# --------------------------------------------------------------------------------------------------------

def about(response):
    """ This Function renders About Us page """
    
    return render(response, 'about.html')

# --------------------------------------------------------------------------------------------------------

def book(response):
    """ This Function renders Booking information filling page. """

    return render(response, 'book.html')

# --------------------------------------------------------------------------------------------------------

def contact(response):
    """ This Function renders Contact Us page """
    
    return render(response, 'contact.html')

# --------------------------------------------------------------------------------------------------------

def ticket(response):
    """ This function render ticket page which shows Booked Ticket Information """

    if response.method == 'POST':                   # Get filled attributed from form on /book page
        show = response.POST.get('stadium')
        email = response.POST.get('email')
        date = response.POST.get('date')
        attendees = response.POST.get('attendee')
        tier = response.POST.get('seat')

        tid, price = db1.book_ticket(show, email, date, attendees, tier)    # Make Entry in database

        if tid == 0:
            context = {
                'a' : 'Seats cannot be booked'
            }
            return render(response, 'popup.html')

    # Return context to print Ticket
    context = {
        'id' : tid,
        'show' : show,
        'tier' : tier,
        'attendees' : attendees,
        'date' : date,
        'price' : price,
    }

    return render(response, 'ticket.html', context)

# --------------------------------------------------------------------------------------------------------

def cancel(response):
    """ This Function renders Ticket Cancellation Form page """
    
    return render(response, 'cancel.html')

# --------------------------------------------------------------------------------------------------------

def cancelled(response):
    """
        This Function generated report of cancelled ticket by taking in Ticket ID form /cancel page
    """

    # Get filled attributed from form on /cancel page
    if response.method == 'POST':
        email = response.POST.get('email')
        tid = response.POST.get('tid')
        # cmd=f"SELECT email,tid FROM Book WHERE tid={tid}"
        # cur.execute(cmd)
        # email1,tid1=cur.fetchall()[0]
        # if(email==email1 and tid==tid1):
        show, tier, price = db1.cancel_ticket(tid)
    #     else:
    #         context = {
    #             'a' : 'please enter correct details!..'
    #          }
    # return render(response, 'popup.html')


    if show == 0:
        return HttpResponse("Seats cannot be booked")
        
    # Return context to print as actual cancellation report on webpage
    context = {
        'id' : tid,
        'show' : show,
        'tier' : tier,
        'refund' : price
    }

    return render(response, 'cancelled.html', context)

# --------------------------------------------------------------------------------------------------------

def popup(response):
    context = {
        'a' : 'Seats cannot be booked'
    }
    return render(response, 'cancelled.html', context)

# ---------------------------------------------------------------------------------------------------------

def mybooking(response):
    if response.method=='POST':
        email1=response.post.get('email')
        id,show,date=db1.getmybookings(email1)
        context={
            'id':id,
            'show':show,
            'date':date
            }
    else:
        return render(response, 'mybooking.html')
    return render(response,'books.html',context)