from dataclasses import dataclass
@dataclass
class Classroom:
    name:str
    attribute:dict[int, str]
class1 = Classroom('1-A', {1:'Taro'})
class1.attribute[2] = 'Jiro'
print(class1)
class1.attribute.update({
    3:'Hana',
    4:'Risa',
    5:'Tom',
    6:'Bob'
})
print(class1)
