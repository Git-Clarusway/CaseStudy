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
            user_id=names.index(name)
            surname=input('Please enter your surname : ').title()
            info=surnames[user_id],birth_months[user_id],birth_days[user_id],birth_years[user_id]
            if surname in info:
                u_date=input('Please enter your birthday (MM/DD/YYYY) ')
                u_month,u_day,u_year=u_date.split('/')
                if len(u_month+u_day+u_year) == 8:
                    if int(u_month) in info  and int(u_day) in info and int(u_year) in info:
                        print('You are a costumer')
                        break
                    else:    
                        print('You are not a costumer')
                else:
                    print('You have entered an incorrect value!')  
            else:
                print('You are not a costumer')              
        else:
             print('You are not a costumer')
    except:
        print('You have entered an incorrect value!') 