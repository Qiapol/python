def animal_ability(animal):
    animal.voice()
    animal.walking()

class Duck():
    def voice(self):
        print('ガーガー')
    def walking(self):
        print('アヒルがお尻をフリフリ歩きます')

class Elephant():
    def voice(self):
        print('パオーン')
    def walking(self):
        print('像がゆったりと歩きます')

class Horse():
    def voice(self):
        print('ヒヒーン')
    def walking(self):
        print('馬がパカパカと歩きます')

duck = Duck()
animal_ability(duck)

elephant = Elephant()
animal_ability(elephant)

horse = Horse()
animal_ability(horse)