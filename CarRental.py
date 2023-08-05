from datetime import date
import random
import os
import matplotlib.pyplot as plt

from random_car_creater import car_brands,car_models
from customer_list_1 import customer_list
import time as realtime

#CAR CLASS
class Car:
    def  __init__(self,car_name,car_model,car_year,car_price,car_daily_cost):
        self.car_name=car_name
        self.car_model=car_model
        self.car_year=car_year
        self.car_price=car_price
        self.car_daily_cost=car_daily_cost
        self.car_daily_rent=None

    def  __str__(self):
        print(f'car name:{self.car_name} car model:{self.car_model} car year:{self.car_year} car price:{self.car_price} car daily cost:{self.car_daily_cost}')

    def one_day_rent_price(self,rent_procent):
        self.car_daily_rent=self.car_price*rent_procent
        return self.car_daily_rent

#GARAGE CLASS

class Garage:
    def  __init__(self,garage_name,company_capital):
        self.garage_name=garage_name
        self.company_capital=company_capital
        self.cars_in_garage=[]
        self.cars_in_garage
        self.cars_rented=[]
        self.client_list=[]
        self.daily_rent_income=None
        self.total_rent_income=None 
        
    def  __str__(self):
        return f'Garage Name:{self.garage_name} Start Capital:{self.company_capital}'

    def display_cars_in_garage(self,sort_by='name'):
        garage_car_list=""
        if not self.cars_in_garage:
            return 'NO CAR IN THE GARAGE NOW'
        else:
            if sort_by=='price':
                sorted_cars=sorted(self.cars_in_garage,key=lambda car: car.car_price)
            elif sort_by=='year':
                sorted_cars=sorted(self.cars_in_garage,key=lambda car: car.car_year)
            elif sort_by=='name':
                sorted_cars=sorted(self.cars_in_garage,key=lambda car: car.car_name)
            else:
                sorted_cars=self.cars_in_garage
            
                
            for index,car in enumerate(self.cars_in_garage):
                garage_car_list+=f'{index+1}-{car.car_name} MODEL:{car.car_model} YEAR:{car.car_year} PRICE:{car.car_price} DAILY COST:{car.car_daily_cost}\n'
        header=f'{self.garage_name} CAR IN GARAGE\n--------------------\n'
        text_to_show=header+garage_car_list
        print(text_to_show)
        print('--------------------------------')
             
        


    def display_rented_cars(self):
        rented_car_list=""
        if not self.cars_rented:
            print('NO CAR RENTED YET')
            return 

        for index,car in enumerate(self.cars_rented):
            daily_rent_price=int(car[0].car_price)/30
            rented_car_list+=f'{index+1}-{car[0].car_name} MODEL:{car[0].car_model} YEAR: {car[0].car_year} PRICE: {car[0].car_price} RENT PRICE: {daily_rent_price}\n'
        header=f'{self.garage_name}: RENTED CARS\n'
        text_to_show=header+rented_car_list
        print(text_to_show)

    def buy_car_to_garage(self,car): #buy a car and update company capital
        if isinstance(car,Car):
            if car in self.cars_in_garage:
                print('this car already in the garage')
            else:
                self.cars_in_garage.append(car)
                self.company_capital=self.company_capital-car.car_price
                print('Cars in the Garage is updated')
                self.display_cars_in_garage()

    def sell_a_car_from_garage(self,car):
        if isinstance(car,Car):
            if car not in self.cars_in_garage:
                print('this car not in the garage')
            else:
                self.cars_in_garage.remove(car)
                self.company_capital=self.company_capital+car.car_price  #here car price should be 2nd hand later
                print('Car sold')
                self.display_cars_in_garage()

    def all_cars_fixed_daily_cost(self):
        all_cars_total_fixed_daily_cost=0
        for car in self.cars_in_garage:
            all_cars_total_fixed_daily_cost+=car.car_daily_cost
        #self.company_capital=self.company_capital-total_daily_cost
        return all_cars_total_fixed_daily_cost

    def rent_a_car(self,car,customer_rented,rent_duration):
        if car not in self.cars_in_garage:
            print('This car does not exist in the Garage')
            return
        else:
            self.cars_rented.append((car,customer_rented,rent_duration))
            self.cars_in_garage.remove(car)

            self.daily_rent_price=car.car_price/30 
            #daily_rent_price=car.car_price/30
            self.total_rent_price=self.daily_rent_price*rent_duration
            self.company_capital+=self.total_rent_price

    def return_car_to_garage(self,duration_passed=0):
        cars_to_return=[]
        updated_rented_cars=[]

        for car_tuple in self.cars_rented:
            car,customer_rented,rent_duration=car_tuple
            rent_duration-=duration_passed
            if rent_duration<=0:
                print(f'{car.car_name} in the garage again')
                cars_to_return.append(car_tuple)
                self.cars_in_garage.append(car)
            else:
                updated_rented_cars.append((car,customer_rented,rent_duration))
        self.cars_rented=updated_rented_cars
                        
    
    def monthly_personal_payment(self,no_of_workers,salary):
        total_personal_payment=no_of_workers*salary
        self.company_capital-=total_personal_payment
        print(f'total personal:{no_of_workers}\npaid monthly:{total_personal_payment}\nnow total capital:{self.company_capital}\n')

    def display_account(self):
        header=f'COMPANY : {self.garage_name}'
        header1='------LOG BOOK----------Time :{time(day_passed)}'
        print(header)

        text=f"""
Company Capital:{self.company_capital}
Income from Rented Cars:{self.total_rent_income}
------------------------------------------------
"""
        print(text)

    def update_capital(self):
        cars_cost=self.all_cars_fixed_daily_cost()
        total_cost=cars_cost
        self.company_capital-=total_cost
        
        return self.company_capital

#CLASS END---------------------------------------------------------------------- 

def display_inventory(garage,day_passed):

    print(f'{day_passed}.Days: Company Capital:{garage.company_capital}')
    print(f'Cars daily fixed cost:{garage.all_cars_fixed_daily_cost()}')
    garage.display_cars_in_garage(sort_by='name')
    garage.display_rented_cars()

def car_creater(garage,car_amount):
    car_list=[]
    for i in range(car_amount):
        car_name=random.choice(car_brands)
        car_model=random.choice(car_models)
        car_year=random.randint(1970,2022)
        car_price=random.randint(8000,25000)
        car_daily_cost=round(car_price*0.001,1)
        car_list.append((car_name,car_model,car_year,car_price,car_daily_cost))
    return car_list

def rent_a_car(garage):
    garage.display_cars_in_garage()
    while True:
        try:
            index_car_to_rent=int(input('Car Number ?'))
            if index_car_to_rent<1 or index_car_to_rent>len(garage.cars_in_garage):
                raise ValueError
            break
        except ValueError:
            print('invalid selection')
    who_want_to_rent=input('Client Name:')
    borrow_duration=int(input('Duration ?'))
    garage.rent_a_car(garage.cars_in_garage[index_car_to_rent-1],who_want_to_rent,borrow_duration)
    

def drop_customer(garage):
    who_want_to_rent=random.choice(customer_list)
    borrow_duration=random.randint(1,10)
    his_favorite_car=random.choice(garage.cars_in_garage)
    
    text=f"""
    {who_want_to_rent} came to the company and
    wants to rent {his_favorite_car.car_name}
    for {borrow_duration} days."""
    print(text)
    garage.rent_a_car(his_favorite_car, who_want_to_rent, borrow_duration)

def start_up(garage,start_amount):
    startup_cars=[]
    total_car_cost=0

    for car in car_creater(garage,start_amount):
        
        startup_car=Car(*car)
        startup_cars.append(startup_car)
        garage.cars_in_garage.append(startup_car)
        total_car_cost=total_car_cost+startup_car.car_price

    total_fixed_daily_cost=garage.all_cars_fixed_daily_cost()
    total_start_cost=total_car_cost+total_fixed_daily_cost
    garage.company_capital=garage.company_capital-total_start_cost

    return startup_cars

def buy_car(garage,cars_amount):
    cls_screen()
    available_cars=[]
    available_car_amount=random.randint(1,cars_amount)
    for car in car_creater(garage,available_car_amount):
        available_cars.append(Car(*car))
    for index,car in enumerate(available_cars):
        print(f'        {index}-{car.car_name},{car.car_model},{car.car_year},{car.car_price},{car.car_daily_cost}')

    while True:
        try:
            selection=int(input('Enter the index of the car'))
            if selection<0 or selection>=len(available_cars):
                print('Enter a valid selection')
            else:
                break
        except ValueError:
            print('Enter Valid selection')
    selected_car=available_cars[selection]

    decision=input('are you sure for purchase ? ').strip()
    if decision=='y':
        garage.buy_car_to_garage(selected_car)

def sell_a_car(garage):
    garage.display_cars_in_garage()
    car_index=int(input('which car will be sold ?'))
    if car_index<=0 or car_index>len(garage.cars_in_garage):
        print('invalid index')
    else:
        garage.sell_a_car_from_garage(garage.cars_in_garage[car_index-1])

def start_new_company():
    intro_text="""

            Welcome to Car Rent Simulation. First you need to pick up a name for your garage
            what should be your company Name ? or just enter for automatic name
            enter your company name
            """

    
    name=input(intro_text)
    if name=="":
        name='CREATIVE LTD'
    capital=200000
    my_garage=Garage(name,capital)
    car_start_up=int(input('            how many cars do you want as start up ?'))
    start_up(my_garage,car_start_up)
    cls_screen()
    return my_garage


def time(day_passed):
    dict_time = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
    year = 2023 + day_passed // 365
    month_num = (day_passed % 365) // 30 + 1
    if month_num > 12:
        month_num = month_num % 12
    month = dict_time[f'{month_num:02}']
    return f'{day_passed % 30}-{month}-{year}'   

def cls_screen():
    os.system('cls' if os.name=='nt' else 'clear')
    return


def show_garage_cars_in_treeview(garage):
    rows=[]
    for index,car in enumerate(garage.cars_in_garage):
        rows=[index,car.car_name,car.car_model,car.car_year,car.car_price,car.car_daily_cost]
        garage_cars_tree.insert("","end",text="",values=rows)
        
        
        
        
#initialzing program----------------------------------------
my_garage=start_new_company()
no_of_workers=int(input('            how many people will work in your company ?'))


day_passed=1

track_capital=[my_garage.company_capital]
track_days=[day_passed]
salary=1000

menu="""
menu
------------------
        1-pass a day
        2-buy a car to garage
        3-list company cars
        4-change workers number
        5-Display Account
        6-Rent a Car
        7-Display Rented Cars
        8-automatic day pass (0 for the fastest)
        9-show profit and income in graphic
        10- sell a car
        11- change number of workers
        12- reset graphic
        0- Exit
"""
#main loop------------------------------------





while True:

    if day_passed%365==0:
        salary=salary+(salary*0.1)
        print(f'salaries increased and now : {salary}')
    if day_passed%30==0:
        my_garage.monthly_personal_payment(no_of_workers,salary)
    drop_time=int(random.randint(0,4))
    if drop_time==2:
        drop_customer(my_garage)
        
    print(menu)
    user_selection=input('selection').strip()

    if user_selection=='1' or user_selection=='':
        cls_screen()
        day_passed+=1
        my_garage.all_cars_fixed_daily_cost()
        my_garage.update_capital()
        display_inventory(my_garage,day_passed)
        print(time(day_passed))
        my_garage.return_car_to_garage(1)
        track_capital.append(my_garage.company_capital)
        track_days.append(day_passed)

    elif user_selection=='2':
        buy_car(my_garage,4)

    elif user_selection=='3':
        display_inventory(my_garage,day_passed)
        

    elif user_selection=='4':
        pass

    elif user_selection=='5':
        my_garage.display_account()

    elif user_selection=='6':
        rent_a_car(my_garage)

    elif user_selection=='7':
         my_garage.display_rented_cars()

    elif user_selection=='8':
        auto_days=int(input('       how many days you want automatic day pass ?'))
        sleep_time_str=input('fast or slow 1...10 0 for fastest')
        try:
            sleep_time=int(sleep_time_str)

        except ValueError:
            sleep_time=0
            
        for i in range(auto_days):
            #cls_screen()
            day_passed+=1
            my_garage.all_cars_fixed_daily_cost()
            my_garage.update_capital()
            if day_passed%30==0:
                my_garage.monthly_personal_payment(no_of_workers,salary)
            if day_passed%365==0:
                salary=salary+(salary*0.1)
                print(f'salaries increased and now : {salary}')
            #display_inventory(my_garage,day_passed)
            print(time(day_passed))
            my_garage.return_car_to_garage(1)
            drop_time=int(random.randint(0,4))
            if drop_time==2:
                drop_customer(my_garage)
            track_capital.append(my_garage.company_capital)
            track_days.append(day_passed)
            realtime.sleep(sleep_time)
        display_inventory(my_garage,day_passed)

    elif user_selection=='9':
        plt.plot(track_days,track_capital)
        plt.show()

    elif user_selection=='10':
        sell_a_car(my_garage)
        
    elif user_selection=='11':
        update_no_of_workers=int(input(f'now {no_of_workers} people work. What is new no?'))
        no_of_workers=update_no_of_workers

    elif user_selection=='12':
        track_capital=[]
        track_days=[]

    elif user_selection=='0':
        break
    else:
        print('invalid Selection')


