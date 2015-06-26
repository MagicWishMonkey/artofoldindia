from aoi.categories.categories import Categories
from aoi.categories.category import Category


Categories.__table_name__ = "categories"
Categories.__cache_config__["ttl"] = 120
Categories.__model__ = Category

Categories.__select_query__ = """
SELECT
  id,
  label,
  parent_id
FROM categories;
""".strip()

Categories.__lookup_query__ = """
SELECT id FROM categories WHERE label=@label;
""".strip()
