import datetime

maturity_date = datetime.datetime(2021, 7, 31)

user_investment_date_input = input('Enter the date of investment in the format dd-mm-yyyy\n')

user_investment_date = datetime.datetime.now()
user_investment_date_day = user_investment_date_input[:2]
user_investment_date_month = user_investment_date_input[3:5]
user_investment_date_year = user_investment_date_input[6:]

user_investment_date = user_investment_date.replace(year=int(user_investment_date_year), month=int(user_investment_date_month), day=int(user_investment_date_day))

print(user_investment_date)


def investment_calculator():
    day_difference = maturity_date - user_investment_date
    day_difference = day_difference.days

    interest_pd_percent = 15/365

    earning_pd = 850000*interest_pd_percent

    investment_made = earning_pd *  day_difference                                                                                                                                                                                                                                               

    return investment_made


if user_investment_date > maturity_date:
    print('Investment cant be done beyond the date of maturity')
else:
    investment = investment_calculator()

print(investment)
