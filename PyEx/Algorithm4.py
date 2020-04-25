# Алгоритм поиска в ширину
# на примере задачи о поиске среди знакомых продавца манго
def person_is_seller(name, seller_simbol):
    return name[-1] == seller_simbol #последняя буква в имени равна 'm' - вообще условие может быть любым

def search(name, seller_simbol):
    from _collections import deque

    graph = {} # инициализация хеш-таблицы с направленными графами
    graph["you"] = ["Alice", "Bob", "Claire"] # знакомые первого круга
    graph["Bob"] = ["Anuj", "Peggy"] # знакомые знакомого
    graph["Alice"] = ["Peggy"]
    graph["Claire"] = ["Tom", "Johnny"]
    graph["Anuj"] = []
    graph["Peggy"] = []
    graph["Tom"] = []
    graph["Johnny"] = []

    search_queue = deque() # инициализация очереди
    search_queue += graph[name] # в очередь добавлены все люди указанной персоны
    searched = [] # инициализация массива для хранения обработанных имен знакомых
    while search_queue: # пока очередь не пуста
        person = search_queue.popleft() # извлечение из очереди первого знакомого
        if not person in searched: # если ранее его не проверяли, то проверяем
            if person_is_seller(person, seller_simbol):
                print(person + " is a mango seller! ")
                return True
            else:
                search_queue += graph[person] # если знакомый не продавец манго, добавляем в очередь всех его знакомых
                searched.append(person) # запоминаем в массиве обработанного знакомого
    return False

search("you", "y")