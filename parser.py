from openpyxl import load_workbook
from openpyxl.cell import Cell
from models import *


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
                    period = Period('fact')
                    if cell.col_idx == 3:
                        data_type = DataType('Qliq')
                        self.__append_data_row(period, company, data_type, cell, row)
                    elif cell.col_idx == 5:
                        data_type = DataType('Qoil')
                        self.__append_data_row(period, company, data_type, cell, row)
                else:
                    period = Period('forecast')
                    if cell.col_idx == 7:
                        data_type = DataType('Qliq')
                        self.__append_data_row(period, company, data_type, cell, row)
                    elif cell.col_idx == 9:
                        data_type = DataType('Qoil')
                        self.__append_data_row(period, company, data_type, cell, row)

        # data_row = DataRow(period=Period('fact'), )

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
