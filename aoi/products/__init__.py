from aoi.products.products import Products
from aoi.products.product import Product

Products.__table_name__ = "member"
Products.__cache_config__["ttl"] = 120


Products.__select_query__ = """
SELECT
  id,
  label,
  description
FROM products;
""".strip()

Products.__lookup_query__ = """
SELECT id FROM products WHERE label=@label;
""".strip()
