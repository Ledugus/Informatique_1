class A :

  def m1(self) :
      print("A 1")

  def m2(self) :
      print("A 2")

  def m3(self) :
      self.m1()   # appel à la méthode m1 sur la même instance

  def nom(self) :
      return "A"

class B(A) :

  def m2(self):
      print("B 2")

class C(A):

    def m1(self) :
        print("C 1")

    def nom(self):
        return "C"

class D(C) :

    def m2(self) :
        print("D 2")


a = A()
print(a.nom())
a.m1()
a.m2()
a.m3()
b = B()
print(b.nom())
b.m1()
b.m2()
b.m3()
c = C()
print(c.nom())
c.m1()
c.m2()
c.m3()
d = D()
print(d.nom())
d.m1()
d.m2()
d.m3()

class E :

    def m(self) :
        print("E 1")

    def n(self) :
        print("E 2")

    def p(self) :
        self.n()   # appel à la méthode n sur la même instance

class F(E) :

   def q(self) :
       print("F 1")

   def n(self) :
       super().n() # appeler la méthode définie sur la classe mère
       print("F 2")

   def r(self) :
        self.m() # appel à la méthode m sur la même instance
f = F()
f.q()
f.m()
f.r()
f.n()
f.p()
 