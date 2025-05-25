class A:
    def mensaje(self):
        print("Desde A")

class B:
    def mensaje(self):
        print("Desde B")

class C(A, B):
    pass

obj = C()
obj.mensaje()