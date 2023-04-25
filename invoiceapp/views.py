from django.shortcuts import render
from django.http import HttpResponse
from .models import Invoice,Items
import datetime
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
import os





# Create your views here.
def index(request):
    if request.method=="POST":
        print(request)
        sellername = request.POST.get('sellername','')
        selleraddress = request.POST.get('selleraddress','')
        sellerphone = request.POST.get('sellerphone','')
        buyername = request.POST.get('buyername','')
        buyeraddress = request.POST.get('buyeraddress','')
        buyerphone = request.POST.get('buyerphone','')
        totalproducts = request.POST.get('totalproducts',1)
        invoice = Invoice(seller_name=sellername,seller_address=selleraddress,seller_phone=sellerphone,buyer_name=buyername,buyer_address=buyeraddress,buyer_phone=buyerphone,totalproducts=totalproducts,invoice_date=datetime.date.today())
        invoice.save()
    return render(request,'invoiceapp/index.html')


def makeinvoice(request):
    invoice = Invoice.objects.last()
    num_item = invoice.totalproducts
    items_ =[i for i in range(num_item)]
    if request.method=="POST":
        print(request)
        totalamount = 0
        prices = []
        items = []
        for i in range(len(items_)):
            product = request.POST.get('product'+str(i),'')
            quan = request.POST.get('quantity'+str(i),'')
            price = request.POST.get('price'+str(i),'') 
            if quan and price:
               totalamount += int(float(quan))*int(float(price))
            items.append(product)
            prices.append(price)
        print(items)   
        item = Items(items=items,price=prices,total=totalamount)
        item.save()
    return render(request,'invoiceapp/makeinvoice.html',{'total_items':items_})

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def GenerateInvoice(request):
    invoice = Invoice.objects.last()
    item = Items.objects.last() 
    print(item.total)
    print(item.price)
    print(item.items)  
    data = {
            'invoice_id' : invoice.invoice_id,
            'invoice_date': invoice.invoice_date,
            'seller_name': invoice.seller_name,
            'seller_add' : invoice.seller_address,
            'seller_phone': invoice.seller_phone,
            'buyer_name': invoice.buyer_name,
            'buyer_add' : invoice.buyer_address,
            'buyer_phone': invoice.buyer_phone,
            'items' : item.items,
            'price': item.price,
            'total' : item.total,
        }
    # return render(request,'invoiceapp/invoice.html',data)
    pdf = render_to_pdf('invoiceapp/invoice.html', data)
    # item.delete()
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %(data['invoice_id'])
        content = "inline; filename='%s'" %(filename)
        content = "attachment; filename=%s" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")