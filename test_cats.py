import functions

mock_cats = (

    {'id': 1, 'name': 'Garfield', 'age': 40},
    {'id': 2, 'name': 'Heathcliff', 'age': 45}
    )

def test_find_cat_by_name(monkeypatch):
    monkeypatch.setattr(functions, 'cats', mock_cats)
    cat = functions.find_cat_by_id(1)
    assert cat['name'] == 'Garfield'