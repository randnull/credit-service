import datetime
import numpy_financial as npf

from typing import Dict
import datetime


def generate_schedule(term: int, activate_data: datetime.datetime, interest: int, principal: int) -> Dict:
    credit_schedule = dict()
    month_interest = interest / 1200.0

    for period in range(1, term + 1):
        time_period = period * 30

        payment_date = activate_data + datetime.timedelta(days=time_period)

        principal_payment = round(float(npf.ppmt(month_interest, period, term, principal)), 2)

        interest_payment = round(float(npf.ipmt(month_interest, period, term, principal)), 2)

        schedule_data = {
            "payment_date": payment_date,
            "principal_payment": -principal_payment,
            "interest_payment": -interest_payment,
        }

        credit_schedule[period] = schedule_data

    return credit_schedule
