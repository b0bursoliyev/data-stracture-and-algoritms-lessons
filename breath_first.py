from collections import deque

def search(start, target):
    search_deque = deque()
    search_deque += graph[start]
    searched = set()

    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person == target:
                print(f"{target} ni topdik")
                return True
            else:
                search_deque += graph[person]
                searched.add(person)
    return False

graph = {
    'ali': ['bekzod', 'suhrob', 'jamshid', 'tolib', 'xusniddin'],
    'bekzod': ['xalovat', 'davlatyor', 'umid'],
    'suhrob': ['kamol', 'sanjar', 'otabek'],
    'jamshid': ['oybek', 'merdon', 'botir'],
    'tolib': ['lola', 'maftuna', 'laylo'],
    'xusniddin': ['abduholiq', 'valijon'],
    'xalovat': [],
    'davlatyor': [],
    'umid': [],
    'kamol': [],
    'sanjar': [],
    'otabek': [],
    'oybek': [],
    'merdon': [],
    'botir': [],
    'lola': [],
    'maftuna': [],
    'laylo': [],
    'abduholiq': [],
    'valijon': []
}

print(search('ali', 'merdon'))
