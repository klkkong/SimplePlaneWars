# Python面向对象编程--PlaneWars

## Python面向对象

### 封装
* 类和对象的关系：类只有一个，对象可以有很多个。（飞机图纸和飞机的关系）
* 代码中self的含义：哪一个对象调用的方法，self就是哪一个对象的**引用**
* 创建对象时，解释器会自动做两件事：为对象分配内存和调用对象的初始化方法
* 初始化方法：`__init__(self)`
   * 负责创建类属性
   * 负责接收形参：`tom=Cat('Tom')`
* 私有属性和私有方法
   * 定义：在属性名或方法名之前，加两个下划线就变成了私有
   * 私有的含义：在C++的类中，有权限public关键字，public指的是两方面权限：一是由对象在类外直接调用方法；二是在类的内部，由其他方法调用。在Python中，也是如此，私有方法指的是第二种权限。
   * Python中的私有并不是真正的私有：
```
# 假设ClassA中含有私有方法__age
obj=ClassA()
obj.__age  # error: no such attribute

obj._ClassA__age  # pass
```
   

### 继承


## Pygame







