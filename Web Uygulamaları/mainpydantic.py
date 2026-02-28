# İçeri giren verinin, beklediğiniz tipte ve formatta olup olmadığını kontrol eder.

from pydantic import BaseModel

class ProductPydantic(BaseModel):
    name:str
    price:float
    in_stock:bool

if __name__=='__main__':
    external_data={
        "name":"Laptop",
        "price":50.00,
        "in_stock":True
    }
    product=ProductPydantic(
        name=external_data.get("name"),
        price=external_data.get("price"),
        in_stock=external_data.get("in_stock")
    )
print(type(product.name))
print(type(product.price))
print(type(product.in_stock))