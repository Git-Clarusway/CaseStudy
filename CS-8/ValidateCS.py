# Customer should be checked for customer's name, 
# customer's username, and customer's birthday.
# users database - a particular index corresponds to a specific user

# users database - a particular index corresponds to a specific user
names = ["James", "John", "Emma"]
surnames = ["Oliver", "Smith", "Brown"]
birth_days = [15, 22, 8]
birth_months = [3, 6, 12]
birth_years = [1984, 1994, 2001]

while True:
    try:
        name=input('Please enter your name : ').title()
        if name in names: 
            surname=input('Please enter your surname : ').title()
        if surname in surnames:
            b_date=input('Please enter your birthday (MM/DD/YYYY) ')
            b_month,b_day,b_year=b_date.split('/')
            if len(b_month+b_day+b_year) == 8:
                if (int(b_month) in birth_months) and  (int(b_day) in birth_days) and (int(b_year) in birth_years):
                    print('You are a customer!')
                    break
            else:
                print('You have entered an incorrect value!')
        else:        
            print('You are not a customer ')
    except:
        print('You have entered an incorrect value!')
