from dataclasses import dataclass
@dataclass
class Image:
    name:int
    img:tuple[int,int,int]
img1 = Image('cat', (256,256,3))
print(img1)
