import pytest
import datetime

from typing import Dict

from src.functions.generate_schedule import generate_schedule


class TestSchedule:
    def is_equal(self, schedules, correct_principal, correct_interest, test_number):
        for period in schedules:
            schedule = schedules[period]

            #Результат
            principal_payment = schedule["principal_payment"]
            interest_payment = schedule["interest_payment"]

            assert principal_payment == -correct_principal[period - 1], f"Period: {period}. Not equal. Test: {test_number}"
            assert interest_payment == -correct_interest[period - 1], f"Period: {period}. Not equal. Test: {test_number}"


    def test_generating_1(self):
        #Условия
        principal = 1000000
        interest = 12
        term = 24
        current_datatime = datetime.datetime.now()

        #Корректные значения
        principal_payment_correct = [
            -37073.47, -37444.21, -37818.65, 
            -38196.84, -38578.8, -38964.59, 
            -39354.24, -39747.78, -40145.26, 
            -40546.71, -40952.18, -41361.7, 
            -41775.32, -42193.07, -42615.0, 
            -43041.15, -43471.56, -43906.28, 
            -44345.34, -44788.79, -45236.68, 
            -45689.05, -46145.94, -46607.4
        ]


        interest_payment_correct = [
            -10000.0, -9629.27, -9254.82, 
            -8876.64, -8494.67, -8108.88, 
            -7719.23, -7325.69, -6928.21, 
            -6526.76, -6121.29, -5711.77, 
            -5298.16, -4880.4, -4458.47, 
            -4032.32, -3601.91, -3167.19, 
            -2728.13, -2284.68, -1836.79, 
            -1384.42, -927.53, -466.07
        ]

        schedules: Dict = generate_schedule(term=term,activate_data=current_datatime, interest=interest, principal=principal)

        assert len(schedules) == term, f":Count of payments: {len(schedules)}. Term is {term}"

        self.is_equal(schedules, principal_payment_correct, interest_payment_correct, 1)


    def test_generating_2(self):
        #Условия
        principal = 10000
        interest = 90
        term = 8
        current_datatime = datetime.datetime.now()

        #Корректные значения
        principal_payment_correct= [
            -957.27, -1029.07, -1106.25,
            -1189.21, -1278.4, -1374.29,
            -1477.36, -1588.16
        ]

        interest_payment_correct = [
            -750.0, -678.2, -601.02, 
            -518.06, -428.87, -332.99, 
            -229.91, -119.11
        ]

        schedules: Dict = generate_schedule(term=term,activate_data=current_datatime, interest=interest, principal=principal)

        assert len(schedules) == term, f":Count of payments: {len(schedules)}. Term is {term}"

        self.is_equal(schedules, principal_payment_correct, interest_payment_correct, 2)


    def test_generating_3(self):
        #Условия
        principal = 500000
        interest = 22
        term = 36
        current_datatime = datetime.datetime.now()

        #Корректные значения
        principal_payment_correct = [
            -9928.56, -10110.58, -10295.94, 
            -10484.7, -10676.92, -10872.67, 
            -11072.0, -11274.99, -11481.69, 
            -11692.19, -11906.55, -12124.83, 
            -12347.12, -12573.49, -12804.0, 
            -13038.74, -13277.78, -13521.21, 
            -13769.1, -14021.53, -14278.59, 
            -14540.37, -14806.94, -15078.4, 
            -15354.84, -15636.35, -15923.01, 
            -16214.93, -16512.21, -16814.93, 
            -17123.21, -17437.13, -17756.81, 
            -18082.35, -18413.86, -18751.45
        ]

        interest_payment_correct = [
            -9166.67, -8984.64, -8799.28, 
            -8610.52, -8418.3, -8222.56, 
            -8023.23, -7820.24, -7613.53, 
            -7403.04, -7188.68, -6970.39, 
            -6748.1, -6521.74, -6291.23, 
            -6056.49, -5817.44, -5574.02, 
            -5326.13, -5073.69, -4816.63, 
            -4554.86, -4288.28, -4016.82, 
            -3740.39, -3458.88, -3172.21, 
            -2880.29, -2583.02, -2280.3, 
            -1972.02, -1658.1, -1338.42, 
            -1012.87, -681.36, -343.78
        ]

        schedules: Dict = generate_schedule(term=term,activate_data=current_datatime, interest=interest, principal=principal)

        assert len(schedules) == term, f":Count of payments: {len(schedules)}. Term is {term}"

        self.is_equal(schedules, principal_payment_correct, interest_payment_correct, 3)
