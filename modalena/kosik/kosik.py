

class Kosik():

    def __init__(self,request):
        self.session = request.session
        kosik = self.session.get('skey')
        if 'skey' not in request.session:
            kosik = self.session['skey'] = {}
        self.kosik = kosik

    def add(self,product):
        product_id = product.produkt_id

        if product_id not in self.kosik:
            self.kosik[product_id] = {'cena': product.cena}
        
        self.session.modified = True