from pprint import pprint
with open ('rec.txt', 'rt') as f:
    cook_book = {}
    for line in f:
        name = line.strip()
        count = f.readline().strip()
        rec = []
        for line in range(int(count)):
            text = f.readline().split(' | ')
            rec.append({'ingredient_name': text[0],
            'quantity': int(text[1]),
            'measure': text[2]})
        cook_book[name] = rec
        f.readline()

            
    def get_shop_list_by_dishes(dishes, person_count):
        if dishes == name:
            for ingridient in dishes:
                for person_count in ingridient:
                    rec['quantity'] = rec['quantity'] * person_count 
                print(rec)
            else:
                return 'Нет такого блюда'
    pprint(cook_book)    
    print(get_shop_list_by_dishes(['Фахитос'], 4)) 



