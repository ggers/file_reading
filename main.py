cook_book = {
  'яйчница': [
    {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
    ],
  'стейк': [
    {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
    {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
    ],
  'салат': [
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
    {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
    ]
  }

# логика программы.
# 1. подключить файл с данными и пройти его циклом по срокам
# 2. первая строка превращается в название блюда запоминается
# 3. вторая строка запоминает количество ингридиентов ingridient_count для внутреннего цикла ингридиентов
# 4. внутренний цикл через while перебирает и считывает ингридиенты через разделитель
# 5. создаем список словарей для ингридиентов каждого блюда методом append()
# 6. вешаем в итоговjм словаре список значений на ключ - название ингридиента методом update()
# 7. на выходе получаем аналогичный исходному трехуровневый словарь cook_book{}
# 8. крутим пустую строку с помощью readline()
# 9. остальной код остаётся без изменений

cook_book1 = {}

def create_cook_book_from_file (filename="data01.txt"):
  with open("data01.txt", encoding= "utf-8") as f:
    for line in f:
      dish_name = line(strip()
      ingridient_count = int(readline())
      while i < ingridient_count:
        ingridients = readline().strip()
        ingridients_splitted = ingridients.split(|)
        ingridient_list.append([{'ingridient_name': ingridients_splitted[0]}, {'quantity': ingridients_splitted[1]}, {'measure': ingridients_splitted[2]}]}
        i+=1
        cook_book1.update({dish_name: ingridient_list})
     f.readline()
  return True

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()
