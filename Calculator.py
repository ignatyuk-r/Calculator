import datetime as dt

class Calc():
    
    def add_record(self, in_value, in_date = dt.datetime.now().date() ):
        self.records.append((in_value,in_date))
        
    
    def __init__(self, limit):
        self.records=[]
        self.limit = limit

    def get_today_stats(self):
        today = dt.datetime.now().date()
#        print(self.records)
        sum = 0
        for num in self.records:
            if num[1] == today:
                sum+=num[0]
        return sum

    def get_week_stats(self):
        today = dt.datetime.now().date()
        _, week_num, _ = today.isocalendar()
#        print(self.records)
        sum = 0
        for num in self.records:
            _, week_num2, _ = num[1].isocalendar()
            if  week_num2 ==  week_num:
                sum+=num[0]
        return sum

    def remained(self):
        return self.limit - self.get_today_stats()

c = Calc(100)
c.add_record(10)
c.add_record(20)
print(c.get_week_stats())

print(f'total {c.get_today_stats()}')
print(f'remained =  {c.remained()}')

date_format = '%d.%m.%Y'
moment = dt.datetime.strptime('07.02.2021', date_format)
print(moment)


day = moment.date
print(day)


now = dt.datetime.now()
print(now)


print(now.date())


# class Record:
#     def add_record():
#         amount = []
    
#     date = now.date()


# class Calculator:
#     limit = 1000
#     Record

#     def get_today_stats():
#         for i in amount:
#             pass

# #    def get_week_stats():
# #        pass

#     # def get_remained():
#     #     pass


# class Calories_Calculator(Calculator):
#     def get_calories_remained():
#         if get_today_stats() < limit :
#             print(f'ты можешь съесть ещё {limit - get_today_stats} кКал')
#         else:
#             print('хватит есть!')


# class Cash_Calculator(Calculator):
#     def __init__(self, rub):
#         self.RUB = rub
#         self.USD_RATE = rub * 0.013
#         self.EUR_RATE = rub * 0.011
        
#         def get_today_cash_remained():
#             if get_today_stats() < limit :
#                 print(f'на сегодня осталось{round(limit - get_today_stats, 2)}')
#             if get_today_stats() == limit:
#                 print('деньги закончились((')
#             if get_today_stats() > limit:
#                 print(f'деньги закончились, а твой долг:{round(get_today_stats - limit, 2)}')




