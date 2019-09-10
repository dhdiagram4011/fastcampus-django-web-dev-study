from django.conf import settings
from shop.models import Product

class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID) #여기저기서 불러다가 쓸 수 있기 때문에
        if not cart:
            cart = self.session[settings.CART_ID]  = {}
        self.cart = cart

    def __len__(self):
        #len() 메서드를 사용하기 위하여
        #count = 0
        #for item in self.cart.values()
        #    count = count+item['quantity']
        #return count
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids) #카트에 포함되어 있는 제품의 정보만 보여줌

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['total_price'] = item['price'] * item['quantity']

            yield item

    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0 , 'price':product_id}

        if is_update: #장바구니에서 상품을 수정하면 업데이트
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()


    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True #장고에서 세션을 알아서 저장해줌

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del(self.cart[product_id])
            self.save()

    def clear(self):
        self.cart = {}
        self.save()

    def get_product_total(self):
        return sum(item['price']*item['quantity'] for item in self.cart.values())


