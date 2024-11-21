animal_dict = {
    'vertebrado': {
        'mamifero': {
            'onivoro': 'homem',
            'herbivoro': 'vaca',
        },
        'ave': {
            'carnivoro': 'aguia',
            'onivoro': 'pomba',
        }
    },
    'invertebrado': {
        'anelideo': {
            'onivoro': 'minhoca',
            'hematofago': 'sanguessuga'
        },
        'inseto': {
            'hematofago': 'pulga',
            'herbivoro': 'lagarta'
        }
    }
}

word1 = input().strip()
word2 = input().strip()
word3 = input().strip()

animal = animal_dict[word1][word2][word3]
print(animal)
