from enum import Enum


class Period:
    def __init__(self, period):
        self.period = period


class Company:
    def __init__(self, company_name):
        self.company_name = company_name


class DataType:
    def __init__(self, data_type):
        self.data_type = data_type


class DataRow:

    def __init__(self, period: Period, company: Company, data_type: DataType, data: dict):
        self.period = period
        self.company = company
        self.data_type = data_type
        self.data = data
