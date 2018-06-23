dict = {
    'Kenneth Eugene Iverson': 'APL',
    'Alfred Vaino Aho': 'AWK',
    'Jeremy Ashkenas': 'CoffeeScript',
    'Ohn Warner Backus': 'Fortran',
    'Don Woods': 'INTERCAL',
    'Roberto Ierusalimschy': 'Lua',
    'John McCarthy': 'Lisp',
    'Niklaus Emil Wirth': 'Pascal',
    'Dennis MacAlistair Ritchie': 'C',
    'Don Syme': 'F Sharp',
    'Bjarne Stroustrup': 'C++',
    'Walter Bright': 'D',
    'Barbara Liskov': 'Clu',
    'Seymour Papert': 'Logo',
    'Ole-Johan Dahl': 'Simula',
    'Rodrigo Barreto de Oliveira': 'Boo',
    'Rich Hickey': 'Clojure',
    'John Warner Backus': 'Fortran',
    'Guido van Rossum': 'Pyton',
    'Slava Pestrov': 'Factor',
    'James Gosling': 'Java',
    'Yukihiro Matsumoto': 'Ruby',
    'Paul Graham': 'Lisp',
    'Larry Wall': 'Perl',
    'Xavier Leroy': 'OCaml',
    'Jean David Ichbian': 'Ada',
    'Grace Hopper': 'Cobol',
    'Alan Curtis Kay': 'Smalltalk',
}

def sorting(dict):
    sort = sorted(dict.keys())
    for name in sort:
        print(name, "-", dict[name])
sorting(dict)

search = input('Enter a name: ')
def searching(dict):
    for names, value in dict.items():
        if names == search:
            print(search, 'Computer language: ', dict[names])
            break
        else:
            print('research')
searching(dict)
