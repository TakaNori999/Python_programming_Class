from dataclasses import dataclass
@dataclass
class Classroom:
    name:str
    member:list[str]
class1 = Classroom('1-A', ['Taro'])
class1.member.append('Jiro')
print(class1)
add1 = ['Hana', 'Risa', 'Tom', 'Bob']
class1.member.extend(add1)
print(class1)
