unit_convert = {
                'teaspoon': 5.0,   # milliliters
                'tablespoon': 15.0,
                'cup': 240.0,
                'pint': 480.0,
                'quart': 960.0,
                'gallon': 3785.0,
                'ounce': 28.0, # gram
                'pound': 454.0,
                'pinch': 3.0  # intuitive definition
                }

def simple_ingr_parser(s, ingredient, countable=False):
    ingr_lists = s.lower().split("-")
    ind = -1
    for ingr in ingr_lists:
        ind = ingr.find(ingredient)
        if ind >= 0:
            ingr_line = ingr
            break;
    if ind == -1:
        return 0.0
    pre_words = ingr_line.split()
    amount = 0.0
    word = 0
    while word < len(pre_words):
        tmp = get_amount(pre_words[word])
        if tmp <=0:
            break
        else:
            amount = amount + tmp
        word = word + 1
    if amount <= 0:
        #print("unrecognized amount: %s" % (ingr_line))
        return -1.0
    if countable:     # such as 1 onion
        return amount
    if word >= len(pre_words):
        print("No unit string found")
        return 0.0
    unit_str = " ".join(pre_words[word:])
    for unit, val in unit_convert.items():
        if unit_str.find(unit) >= 0:
                return amount*val
    #print("unrecognized unit: %s " % (unit_str))
    return -1.0;
    
def get_amount(num):
    if not num[0].isdigit():
        return -1
    if num.find('/') < 0:
        return float(num)
    else:
        divs = num.split('/')
        return float(divs[0]) / float(divs[1])