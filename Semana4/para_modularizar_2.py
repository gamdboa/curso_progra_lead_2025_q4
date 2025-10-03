def generateInvoice(customer_id):
    # obtener datos de la BD
    customer = get_customer_from_db(customer_id) #asuma que existen...
    orders = get_orders_for_customer(customer_id) # o simulelo de alguna orma
    
    # Calculatotales
    total = sum(order["price"] * order["quantity"] for order in orders)
    tax = total * 0.13
    grand_total = total + tax
    
    # salida
    invoice = f"Customer: {customer['name']}\n"
    for order in orders:
        invoice += f"{order['item']} x {order['quantity']} = ${order['price'] * order['quantity']}\n"
    invoice += f"Total: ${grand_total}\n"

    # guardar a archivo
    with open(f"{customer_id}_invoice.txt", "w") as f:
        f.write(invoice)