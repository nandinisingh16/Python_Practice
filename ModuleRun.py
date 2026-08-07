import Python.ModuleExm as ModuleExm

print("area of the circle whose radius is 22 ")
print(round(ModuleExm.areaCir(22),2))

def func1():
    x=24
    def func2():
        print("circumcenter of circle with radiius",x,ModuleExm.areaCir(x))
    func2()
func1()

