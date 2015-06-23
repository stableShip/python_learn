# coding=utf-8
__author__ = 'JIE'


class Test():
    __privateVaule = "privateVaule"

    publicValue = 0

    # def __init__(self, privateValue, publiceValue):
    #     self.publicValue = publiceValue
    #     self.__privateVaule = privateValue

    def __test(self):
        print("private function")

    def public(self):
        print("public function")

    def getPrivateValue(self):
        return self.__privateVaule;

    @staticmethod
    def staticTest():
        print "static"

    @classmethod
    def classDefTest(self):
        print("classDefTest")

# print Test().publicValue

# print Test().getPrivateValue()

# print Test(1, 2).getPrivateValue()

Test.staticTest()

Test.classDefTest()
