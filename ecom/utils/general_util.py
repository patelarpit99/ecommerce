from ecom.datastore import db,redis_store
from ecom.models import ProductCategory, ProductSubcategory

def get_category_map():
    category_map = redis_store.get('category_map')
    if category_map :
        category_map = eval(category_map)
    else:

        sql = "select c.name,sc.name,sc.id from product_subcategories sc inner join  product_categories c on sc.product_category_id = c.id;"
        result = db.engine.execute(sql)
        category_map = {}
        for row in result:
            if row[0] in category_map:
                category_map[row[0]].append({'name':row[1],'id':row[2]})
            else:
                category_map[row[0]] = [{'name':row[1],'id':row[2]}]


        CACHE_EXPIRATION_SECONDS = 10000
        redis_store.setex('category_map', CACHE_EXPIRATION_SECONDS, str(category_map))
    return category_map

def subcat_product_map():
    subcategory_product_map = redis_store.get('subcategory_product_map')
    if subcategory_product_map :
        subcategory_product_map = eval(subcategory_product_map)
    else:
        sql = "select sc.name,p.name,p.image,p.id,p.price  from product_subcategories sc inner join products p on p.product_subcategory_id = sc.id group by sc.name, p.name, p.image,p.id,p.price;"
        result = db.engine.execute(sql)
        subcategory_product_map = {}
        for row in result:
            if row[0] in subcategory_product_map:
                subcategory_product_map[row[0]].append({'name':row[1],'image':row[2],'id':row[3],'price':row[4]})
            else:
                subcategory_product_map[row[0]] = [{'name':row[1],'image':row[2],'id':row[3],'price':row[4]}]


        CACHE_EXPIRATION_SECONDS = 10000
        redis_store.setex('subcategory_product_map', CACHE_EXPIRATION_SECONDS, str(subcategory_product_map))
    return subcategory_product_map