stock_productos=[10,25,26,4,31,6,3]
for i in range(len(stock_productos)):
    print(f"Producto {i+1}: {stock_productos[i]} unidades")
    
productos_bajos = [i+1 for i, stock in enumerate(stock_productos) if stock < 20]

print(f"Los productos {productos_bajos} tienen menos de 20 unidades en stock")

print(f"Existen {len(stock_productos)} productos en stock")