from openpyxl import load_workbook
from openpyxl.cell import Cell
from models import *

DATA_TYPE_QLIQ = 'Qliq'
DATA_TYPE_QOIL = 'Qoil'


class XlsxParser:
    data_rows = []

    def __init__(self, file_path):
        self.file = file_path

    def parse_xlsx(self):
        wb = load_workbook(self.file)
        ws = wb.active
        for row in ws.iter_rows(min_row=4):
            company = Company(row[1].value)
            for cell in row:
                if 1 < cell.col_idx < 6:
                    self.__parse_cell(Period('fact'), cell, company, row)
                else:
                    self.__parse_cell(Period('forecast'), cell, company, row)

    def __parse_cell(self, period: Period, cell: Cell, company: Company, row: tuple):
        if cell.col_idx == 3:
            self.__append_data_row(period, company, DataType(DATA_TYPE_QLIQ), cell, row)
        elif cell.col_idx == 5:
            self.__append_data_row(period, company, DataType(DATA_TYPE_QOIL), cell, row)
        elif cell.col_idx == 7:
            self.__append_data_row(period, company, DataType(DATA_TYPE_QLIQ), cell, row)
        elif cell.col_idx == 9:
            self.__append_data_row(period, company, DataType(DATA_TYPE_QOIL), cell, row)

    def __append_data_row(self, period: Period, company: Company, data_type: DataType, cell: Cell, row: tuple):
        self.data_rows.append(DataRow(
            period=period,
            company=company,
            data_type=data_type,
            data={
                'data1': cell.value,
                'data2': row[cell.col_idx].value
            }
        ))
