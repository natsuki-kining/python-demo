# from 导入

from oop_07_modular_cat import Cat
from oop_07_modular_dog import say_hello # 导入指定工具

from oop_07_modular_cat import say_hello as say # 导入指定工具并重命名

from oop_07_modular_cat import * # 导入全部

say_hello()

cat = Cat();

print(cat)

say()
