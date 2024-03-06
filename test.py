from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float = field(default=100, metadata={"unit": "USD", "description": "Price in US dollars"})

# 访问字段的默认值
default_price = Product.__dataclass_fields__['price'].default
print(default_price)  # 输出: 100

# 访问字段的 metadata
field_info = Product.__dataclass_fields__['price'].metadata
print(field_info['description'])  # 输出: Price in US dollars
