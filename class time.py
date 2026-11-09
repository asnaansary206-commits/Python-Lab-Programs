class time:
    def __init__(self,hour,minite,second):
        self.__hour=time
        self.__minite=minite
        self.__second=second
    def __add__(self,other):
        sec=self.__second+other._second
        minute=self.__minite+other.__minute+sec//60
        hour=self.__hour+other+minute//60
        sec=sec%60
        minute=minute%60
        return time(hour,minute,sec)
    def __display(self):
        print(self.__hour."."self.__second)
    t1=time(2,45,50)
    t2=time(1,30,30
    t3=t1+t2
    print("first time:")
    t1.


