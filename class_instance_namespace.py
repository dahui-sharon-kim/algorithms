class Foo:
    name = "Jane Doe"
    def func1():
        print("function 1")
    def func2(self):
        print(id(self)) # 이 self는 클래스 인스턴스
        print("function 2")

foo = Foo() # 클래스 인스턴스
# foo.func1() # 오류 발생
foo.func2()
print(id(foo))

# 파이썬의 클래스는 그 자체가 하나의 네임스페이스이기 때문에 인스턴스 생성 하지 않아도 클래스 내의 메서드를 직접 호출할 수 있다
Foo.func1()
Foo.func2(foo)


print(Foo.__dict__)