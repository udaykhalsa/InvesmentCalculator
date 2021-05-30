import datetime

maturity_date = datetime.datetime(2021, 7, 31)

user_investment_date_input = input('Enter the date of investment in the format dd-mm-yyyy\n')

user_investment_date = datetime.datetime.now()
user_investment_date_day = user_investment_date_input[:2]
user_investment_date_month = user_investment_date_input[3:5]
user_investment_date_year = user_investment_date_input[6:]

user_investment_date = user_investment_date.replace(year=int(user_investment_date_year), month=int(user_investment_date_month), day=int(user_investment_date_day))
future_investment_date = user_investment_date +  datetime.timedelta(days=7)
past_investment_date = user_investment_date -  datetime.timedelta(days=7)

print(user_investment_date)


def investment_calculator():
    day_difference = maturity_date - user_investment_date
    past_day_difference = maturity_date - past_investment_date
    future_day_difference = maturity_date - future_investment_date
    
    print(future_day_difference)

    interest_pd_percent = 15/365

    earning_pd = 850000*interest_pd_percent

    investment_made = earning_pd * day_difference.days
    future_investment_made = earning_pd * future_day_difference.days
    past_investment_made = earning_pd * past_day_difference.days                                                                                                                                                                                                                             

    return investment_made, future_investment_made, past_investment_made


if user_investment_date > maturity_date:
    print('Investment cant be done beyond the date of maturity')
else:
    investment = investment_calculator()

print(f'User invests {investment[0]} will give 850000 on {maturity_date}')
print(f'User invests {investment[1]} 7 days from today will give 850000 on {maturity_date}')
print(f'User invests {investment[2]} 7 days ago from today would give 850000 on {maturity_date}')

