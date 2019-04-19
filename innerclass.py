
class Emp:

    class __Inner:
        def __init__(self,id,nm):
            self.empId=id
            self.empName=nm

        def __str__(self):
            return f'{self.empId}{self.empName}'

    empInstance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.empInstance == None:
            cls.empInstance = cls.__Inner(args[1],args[2])
            print('============',cls.empInstance)
        return cls.empInstance

    def __setattr__(self, key, value):
        if key=='empId':
            self.empInstance.empId=value
        elif key == 'empName':
            self.empInstance.empName=value

    def __getattr__(self, item):
        if item=='empId':
            return self.empInstance.empId
        elif item=='empName':
            return self.empInstance.empName

e1 = Emp(1,"A")
e2 = Emp(2,"B")
e3 = Emp(2,"B")
e4 = Emp(2,"B")
print('============', Emp.empInstance)

e1.empId=5
e2.empName='g'  # e2.setAttribute("empName",10)
print(e1.__dict__)
print(e2.__dict__)
print('============', Emp.empInstance)

print(id(e1))
print(id(e2))
print(id(e3))
print(id(e4))

print(Emp.empInstance.empName)

e1.empName='KK'
print(e1)

'''------------------Overwriting __new__ method of object class-----------------------'''
#
# class Product():
#
#     __instanceRef = None
# #
#     @classmethod
#     def __new__(cls,*args):
#         if cls.__instanceRef == None:
#             cls.__instanceRef = object.__new__(cls)
#         cls.__instanceRef.prodId=args[1]
#         cls.__instanceRef.prodName=args[2]
#         return cls.__instanceRef
#
#     def __str__(self):
#         return f'{self.__instanceRef.prodId}  {self.__instanceRef.prodName}'
#
# p1 = Product(1,"Mobile1")
# print(p1.__dict__)
#
# p2 = Product(2,"Mobile2")
# p3 = Product("Mobile3",3)
# #
#
# print(id(p1))
# print(id(p2))
# print(id(p3))
#
# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)
#
#


'''

'''
'''
class A:
    _aDict = {}
    def __init__(self):
        self.__dict__ = A._aDict

class B(A):

    def __init__(self,id):
        super().__init__()
        self.value=id


n1=B    (1)
print(n1.__dict__)
n2=B(10)
print(n2.__dict__)
print(id(n1))
print(id(n2))


class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg
    def __str__(self): return self.val

x = Singleton('sausage')
print(x)
y = Singleton('eggs')
print(y)
z = Singleton('spam')
print(z)
print(x)
print(y)

print(id('z'))
print(id('x'))
print(id('y'))

'''
'''


class A:

    def __init__(self,id):
        self.num=id

a = A(10)

a.num2 = 20  #a.__setattr__("num2",20) contrct of setter if variable already exist then update else it will Add.
print(a.__dict__)
a.__delattr__("num")
print(a.__dict__)
a1=A(50)
print(a1.__dict__)
a1.__delattr__("num")
print(a1.__dict__)

print(id(a))
print(id(a1))
'''
'''

class Emp:
    class _Inner:
        def __init__(self, nm, id):
            self.value = nm
            self.num = id


    instance = None  # class level -- Emp class --- InnerClassObject -- Value Attribute

    def __init__(self, nm, id):
        if Emp.instance == None:
            print('Inside if Block')
            print(Emp.instance)
            Emp.instance = Emp._Inner(nm, id)
        else:
            print('Inside else Block')
            Emp.instance.value = nm
            Emp.instance.num = id

    def __str__(self):
        return f'{Emp.instance.value}, {Emp.instance.num}'


e1 = Emp("Amit", 10)
print(e1)

e2 = Emp("Yogesh", 20)
print(e2)

e3 = Emp("Amol", 30)
print(e3)

print(id(e1))
print(id(e2))
print(id(e3))
'''
'''
class OnlyOne(object):

    class __OnlyOne:
        def __init__(self):
            print('inside init================')
            self.val = None
        def __str__(self):
            print('inside str================')

            return self.val
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not OnlyOne.instance:
            print('inside if================')
            print( OnlyOne.instance)


            OnlyOne.instance = OnlyOne.__OnlyOne()
        return OnlyOne.instance


    def __getattr__(self, name):
        print('inside getter================')
        return getattr(self.instance, name)

    def __setattr__(self, name):
        print('inside setter================')
        return setattr(self.instance, name)

x = OnlyOne()
print(x.val)
x.val = 'sausage'
print(x)
print(id(x))


y = OnlyOne()
y.val = 'eggs'
print(y)
print(id(y))


z = OnlyOne()
z.val = 'spam'
print(id(z))
print(z)


print(x)
print(y)
print(z)


print(id(x))
print(id(y))
print(id(z))

'''
'''
class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if OnlyOne.instance==None:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)

x = OnlyOne('sausage')
print(x.__dict__)
y = OnlyOne('eggs')
print(y.__dict__)
z = OnlyOne('spam')
print(z.__dict__)

print(id(x))
print(id(y))
print(id(z))

'''