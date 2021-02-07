#calculator project

import datetime as dt


date_format = '%d.%m.%Y'
moment = dt.datetime.strptime('07.02.2021', date_format)
print(moment)
now = dt.datetime.now()
print(now)


class Calculator():
    
    def add_record(self, in_value, in_date = dt.datetime.now().date() ):
        self.records.append((in_value,in_date))
            
    def __init__(self, limit):
        self.records=[]
        self.limit = limit

    def get_today_stats(self):
        today = dt.datetime.now().date()
        sum = 0
        for num in self.records:
            if num[1] == today:
                sum+=num[0]
        return sum

    def get_week_stats(self):
        today = dt.datetime.now().date()
        _, week_num, _ = today.isocalendar()
        sum = 0
        for num in self.records:
            _, week_num2, _ = num[1].isocalendar()
            if  week_num2 ==  week_num:
                sum+=num[0]
        return sum

    def remained(self):
        return self.limit - self.get_today_stats()


class Calories_Calculator(Calculator):

    def get_calories_remained(self):
        if self.get_today_stats() < self.limit :
            print(f'ты можешь съесть ещё {remained()} кКал')
        else:
            print('хватит есть!')


class Cash_Calculator(Calculator):

    def __init__(self, rub):
        self.RUB = rub
        self.USD_RATE = rub * 0.013
        self.EUR_RATE = rub * 0.011
        
        def get_today_cash_remained(self):
            if self.get_today_stats() < self.limit :
                print(f'на сегодня осталось{remained()}')
            if self.get_today_stats() == self.limit:
                print('деньги закончились((')
            if self.get_today_stats() > self.limit:
                print(f'деньги закончились, а твой долг:{remained() * (-1)}')


# c = Calc(100)
# c.add_record(10)
# c.add_record(30)
# print(c.get_week_stats())

# print(f'total {c.get_today_stats()}')
# print(f'remained =  {c.remained()}')
# print (get_today_cash_remained())
