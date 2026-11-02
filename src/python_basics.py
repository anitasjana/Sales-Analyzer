def calculate_revenue(quantity,price):
    return quantity*price


def main():
    project_name="Sales Analyzer"
    products=["Mobile","Laptop","BMW","Byke","IPhone"]
    
    sale ={
        
        "order_id":101,
        "product":"Mobile",
        "quantity" : 2,
        "price":15000,
        "city":"Kolkata",
    }
    
    print(f"Product Name : {project_name}")
    print(f"Available Products : {products}")
    
    for product in products:
        print(f"product : {product}")
        
    revenue = calculate_revenue(sale["quantity"],sale["price"])
    print(f"Revenew for {sale['product']} : {revenue:.2f}")
    
    if(revenue>20000):
        print("Status: High-value sale")
    else:
        print("Status: Normal sale")
    
    
    
if __name__=="__main__":
    main()