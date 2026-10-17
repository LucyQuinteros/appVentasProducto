from pydantic import BaseModel, ConfigDict
from typing import Optional

# Base compartida
class ProductBase(BaseModel):
    name: str
    price: float
    stock: int
    image_url: Optional[str] = None

# Datos requeridos al crear un producto (POST)
class ProductCreate(ProductBase):
    pass

# Formato de respuesta que envía la API (incluye el id asignado por Supabase)
class ProductResponse(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

    