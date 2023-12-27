class Cart():
    def __init__(self, request):
        self.session = request.session
        
        #obtener la clave de sesión actual si existe
        cart = self.session.get('session_key')
        
        #Si el usuario es nuevo, ¡sin clave de sesión! crea ahora
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
            
        #Nos aseguramos que el carrito este disponible en todas las paginas
        self.cart = cart    
        
    def add(self, product):
        product_id = str(product.id)
        
        #Logica
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}    
            
        self.session.modified = True    