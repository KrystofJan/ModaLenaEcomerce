from aplikace.models import Produkt

class Kosik():

    def __init__(self,request):
        self.session = request.session
        kosik = self.session.get('skey')
        if 'skey' not in request.session:
            kosik = self.session['skey'] = {}
        self.kosik = kosik
        #self.item_count = 0
        #self.cena = 0

    def add(self,product):
        
        product_id = product.produkt_id
        if str(product_id) not in self.kosik:
            self.kosik[str(product_id)] = {'cena': float(product.cena),'pocet': 1}
        else:
            self.kosik[str(product_id)]['pocet'] += 1
        self.session.modified = True
        #self.item_count += 1
        #self.count_total_price()

    def __iter__(self):
        product_ids = self.kosik.keys()
        products = Produkt.products.filter(pk__in=product_ids)
        kosik = self.kosik.copy()

        for product in products:
            kosik[str(product.produkt_id)]['product'] = product
        for item in kosik.values():
            item['celkova_cena'] = item['cena'] * item['pocet']
            yield item


    def __len__(self):
        pocet = 0
        for k in self.kosik.keys():
            pocet += int(self.kosik[k]['pocet'])
        return pocet

    def count_total_price(self):
        price = 0
        for k in self.kosik.keys():
            price += self.kosik[k]['cena'] * self.kosik[k]['pocet']
        return float(price)

