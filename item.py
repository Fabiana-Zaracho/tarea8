# Al incluir este módulo, podrás manipular las instancias de Item que posees.


from item import Item
from tabulate import tabulate
from itertools import groupby

def items_list(self):   # Retorna todas las instancias de Item que posee (es decir, de las que es propietario).

    items = [item for item in Item.item_all() if item.owner == self]
    return items

def pick_items(self, number, quantity):   # Devuelve la instancia de Item correspondiente al número especificado, junto con la cantidad especificada, que posee.

    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]

def show_items(self):   # Imprime en forma de tabla el estado del inventario de las instancias de Item que posee, con columnas ["Número", "Nombre del producto", "Precio", "Cantidad"].

    table_data = []
    for stock in _stock(self):
        table_data.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
    print(tabulate(table_data, headers=["Número", "Nombre del producto", "Precio", "Cantidad"], tablefmt="grid"))    # Imprimir los resultados en formato de tabla utilizando el módulo tabulate.


def _stock(self):   # Retorna el estado del inventario de las instancias de Item que posee.

    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(item_ls, key=lambda m: m.name):   # Clasifica las instancias de Item que devuelven el mismo valor con Item#name.

        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append({"number": index, "label": {"name": item[0].name, "price": item[0].price}, "items": item})   # itemsの中には、分類されたItemインスタンスが格納されます。
    return stock
