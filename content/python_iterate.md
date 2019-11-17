Title: Python中的迭代器、生成器
Date: 2019-11-17 11:10
Category: article

`from collections import Iterable, Iterator`

### 1. 可迭代(iterable)对象
  参考[官网链接](https://docs.python.org/zh-cn/3/glossary.html#term-iterable)

```python
class I:
    def __init__(self, v):
        self.v = v

    def __iter__(self):
        return iter([self.v])  # 返回的应该是迭代器对象

i = I(2)
print(isinstance(i, Iterable), isinstance(i, Iterator)) # True False
print(iter(i)) # <list_iterator object at 0x00000000021C8358>

class I:
    def __init__(self, v):
        self.v = v

    def __getitem__(self, item):
        if item > self.v:
            raise IndexError
        return item


i = I(2)
print(isinstance(i, Iterable), isinstance(i, Iterator)) # False False
print(iter(i)) # <iterator object at 0x0000000001DFCD30>
```

### 2. 迭代器(iterator)
  参考[官网链接](https://docs.python.org/zh-cn/3/glossary.html#term-iterator)
```python
class I:
    def __init__(self, v):
        self.v = v

    def __iter__(self):
        return self

    def __next__(self):
        if self.v < 10:
            self.v += 1
            return self.v
        raise StopIteration

i = I(2)
print(isinstance(i, Iterable), isinstance(i, Iterator))  # True True
print(iter(i)) # <__main__.I object at 0x00000000021E0898>
```

### 3. 生成器(generator)
  参考[官网链接](https://docs.python.org/zh-cn/3/glossary.html#term-generator-iterator)
```python
class I:
    def __init__(self, v):
        self.v = v

    def __iter__(self):
        yield 1


i = I(2)
print(isinstance(i, Iterable), isinstance(i, Iterator)) # True False
print(iter(i)) # <generator object I.__iter__ at 0x00000000022204C0>
```


### 4. 总结
1. 只要实现了__iter__方法或者__getitem__方法, 就是iterable, 但Iterable只检测__iter__方法是否实现, 参见[官网链接](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Iterable)。推荐使用iter是否返回迭代器判断可否可迭代。
2. __getitem__方法的返回有特殊要求, 参见[官网链接](https://docs.python.org/3/reference/datamodel.html?highlight=__getitem__#object.__getitem__)。
3. 实现了__iter__和__next__方法就是一个iterator。参见[pep234](https://www.python.org/dev/peps/pep-0234/)。
4. generator是返回一个generator iterator的函数。与普通函数的不同在于函数中包含 yield 表达式。

### 5. 其他参考
1. [Python可迭代与迭代器](http://baijiahao.baidu.com/s?id=1605521786183411929&wfr=spider&for=pc)
1. [迭代器](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143178254193589df9c612d2449618ea460e7a672a366000)