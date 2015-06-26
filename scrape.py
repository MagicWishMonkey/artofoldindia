# -*- coding: utf-8 -*-
from selenium import webdriver
from fuze import toolkit, util


driver = webdriver.Chrome()


def scrape_category(category):
    uri = "http://www.artofoldindia.com/product-category/%s" % category
    driver.get(uri)

    breadcrumb = driver.find_element_by_id("breadcrumb")
    breadcrumb = breadcrumb.find_elements_by_tag_name("a")
    breadcrumb = breadcrumb[1]
    breadcrumb = breadcrumb.text
    category = "%s/%s" % (breadcrumb.strip().lower(), category.strip().lower())

    product_entries = []
    products = driver.find_element_by_class_name("products")
    products = products.find_elements_by_tag_name("li")
    products = [{"category": category, "url": product.find_element_by_tag_name("a").get_attribute("href")} for product in products]
    product_entries.extend(products)

    while True:
        try:
            next = driver.find_element_by_class_name("nav-next")
            next = next.find_element_by_tag_name("a")
        except:
            next = None

        if next is None:
            break

        href = next.get_attribute("href")
        if href is None:
            break

        driver.get(href)
        products = driver.find_element_by_class_name("products")
        products = products.find_elements_by_tag_name("li")
        products = [{"category": category, "url": product.find_element_by_tag_name("a").get_attribute("href")} for product in products]
        product_entries.extend(products)

    return product_entries


def scrape_product(product):
    # product["url"] = "http://www.artofoldindia.com/shop/horse-on-stand/"
    name = product["url"].split("/")
    name = name[len(name) - 2] if name[len(name) - 1] == "" else name[len(name) - 1]
    product["name"] = name

    driver.get(product["url"])
    title = driver.find_element_by_class_name("product_title")
    product["title"] = title.text

    sku = driver.find_element_by_class_name("sku")
    product["sku"] = sku.text.split(":")[1].strip()

    try:
        price = driver.find_element_by_class_name("price").text
        if len(price.strip()) > 1:
            product["price"] = price.strip()
    except:
        pass

    try:
        quantity = driver.find_element_by_class_name("stock").text
        if len(quantity.strip()) > 1:
            quantity = quantity.strip()
            if quantity.find(u"–") > -1:
                quantity = quantity.split(u"–")[1]
            quantity = quantity.strip().split(" ")[0]
            if quantity.isdigit() is True:
                product["quantity"] = int(quantity)
    except:
        pass

    description = driver.find_element_by_id("tab-description")
    parts = description.find_elements_by_tag_name("p")
    description = []
    for part in parts:
        if part.text.lower().startswith("made in india"):
            continue
        description.append(part.text)

    product["description"] = "\n".join(description)


    try:
        driver.find_element_by_class_name("tabs").find_elements_by_tag_name("li")[1].click()
        product["attributes"] = {}
        attributes = driver.find_element_by_class_name("shop_attributes")
        attributes = attributes.find_elements_by_tag_name("tr")
        for x, attribute in enumerate(attributes):
            key = attribute.find_element_by_tag_name("th")
            try:
                key = key.find_element_by_tag_name("p")
            except:
                pass
            key = key.text

            val = attribute.find_element_by_tag_name("td")
            try:
                val = val.find_element_by_tag_name("p")
            except:
                pass
            val = val.text
            if not key:
                continue

            product["attributes"][key] = val
    except:
        pass

    photos = []
    images = driver.find_element_by_class_name("images")
    default = images.find_element_by_tag_name("a")
    default = default.get_attribute("href")
    photos.append(default)

    thumbnails = driver.find_element_by_class_name("thumbnails")
    thumbnails = thumbnails.find_elements_by_tag_name("a")
    for thumbnail in thumbnails:
        try:
            thumbnail = thumbnail.get_attribute("href")
            photos.append(thumbnail)
        except:
            pass

    product["images"] = photos
    return product

categories = [
    "lighting",
    "mirrors",
    "misc-accessories",
    "rugs",
    "antiques",
    "doors",
    "celing",
    "columns",
    "arches",
    "misc",
    "seating",
    "tables",
    "armoires",
    "trunks",
    "consoles"
]

# catalogue = []
# for category in categories:
#     products = scrape_category(category)
#     catalogue.extend(products)
# products = toolkit.json(catalogue, indent=2)
# util.file("/Work/personal/artofoldindia/products.json").write_text(products)


products = toolkit.unjson(util.file("/Work/personal/artofoldindia/products.json").read_text())
for product in products:
    if product.get("name", None) is not None:
        continue

    try:
        product = scrape_product(product)
        util.file("/Work/personal/artofoldindia/products.json").write_text(toolkit.json(products))
        # print toolkit.json(product, indent=2)
    except Exception, ex:
        print product["url"]
        message = "ERROR SCRAPING PRODUCT: %s -> %s" % (product["url"], ex.message)
        print message

print ""