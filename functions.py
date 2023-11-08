cats = []

def find_cat_by_id(cat_id):
    return next(cat for cat in cats if cat['id'] == cat_id)



