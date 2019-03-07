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