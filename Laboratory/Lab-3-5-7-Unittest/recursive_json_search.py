from test_data import *
def json_search(key,input_object):
    """
    Поиск ключа в объекте JSON, ничего не возвращается, если ключ не найден
    key : "keyword" для поиска, с учетом регистра
    input_object : JSON объект, который нужно разобрать, в данном случае test_data.py
    inner_function() фактически выполняет рекурсивный поиск
    возвращает список пар key:value
    """
    ret_val=[]
    def inner_function(key,input_object):
        if isinstance(input_object, dict): # Словарь для обхода
            for k, v in input_object.items(): # поиск ключа в словаре
                if k == key:
                    temp={k:v}
                    ret_val.append(temp)
                if isinstance(v, dict): # значение является другим словарём, поэтому повторим поиск в нём
                    inner_function(key,v)
                elif isinstance(v, list):
                    for item in v:
                        if not isinstance(item, (str,int)): # если это словарь или список также повторим поиск
                            inner_function(key,item)
        else: # Обход списка, поскольку некоторые API возвращают объект JSON в виде списка
            for val in input_object:
                if not isinstance(val, (str,int)):
                    inner_function(key,val)
    inner_function(key,input_object)
    return ret_val
print(json_search("issueSummary",data))
