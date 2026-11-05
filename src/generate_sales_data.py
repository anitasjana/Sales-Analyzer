import csv
import random
from datetime import date, timedelta
from pathlib import Path

DATA_DIR=Path("data")
OUTPUT_FILE=DATA_DIR/"sales_data.csv"

PRODUCTS = [
    {"product": "Mobile", "category": "Electronics", "price": 15000},
    {"product": "Laptop", "category": "Electronics", "price": 55000},
    {"product": "Headphones", "category": "Electronics", "price": 2500},
    {"product": "Shoes", "category": "Fashion", "price": 3000},
    {"product": "T-Shirt", "category": "Fashion", "price": 900},
    {"product": "Watch", "category": "Accessories", "price": 4500},
]

CITIES = ["Kolkata", "Mumbai", "Delhi", "Bangalore", "Chennai"]

def generate_sales_records(days: int=90) ->list[list]:
    """Generate realistic sample sales records."""
    rows=[]
    order_id=1000
    start_date=date(2026,1,1)
    
    for day_offset in range(days):
        current_date=start_date + timedelta(days=day_offset)
        
        for _ in range(random.randint(3,8)):
            item=random.choice(PRODUCTS)
            quantity=random.randint(1,5)
            
            rows.append([
                order_id,
                current_date.isoformat(),
                f"Customer_{order_id}",
                item["product"],
                item["category"],
                quantity,
                item["price"],
                random.choice(CITIES)
            ])
            order_id += 1
            
    return rows
    
def save_sales_records(rows:list[list], output_file: Path) -> None:
    """Save generated sales records to a CSV file."""
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open("w",newline="", encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow([
            "Order_ID", "Order_Date", "Customer_Name",
            "Product", "Category", "Quantity", "Price", "City",
        ])
        writer.writerows(rows)
        
def main() ->None:
    rows = generate_sales_records()
    save_sales_records(rows,OUTPUT_FILE)
    
    print(f"Created {len(rows)} sales records.")
    print(f"Sales data saved to : {OUTPUT_FILE}")
    
if __name__=="__main__":
    main()