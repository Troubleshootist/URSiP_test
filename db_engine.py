import sqlite3
from models import DataRow
from random import randint
from datetime import date

with open('init_db.sql', 'r') as init_db_script:
    sql_file = init_db_script.read()


class DBEngine:
    def __init__(self, data: [DataRow], sqlite_db_path):
        self.data = data

        self.con = sqlite3.connect(sqlite_db_path)
        self.cur = self.con.cursor()
        self.cur.executescript(sql_file)

    def fill_db(self):
        for data_row in self.data:
            self.__enter_row_to_db(data_row)

    def __enter_row_to_db(self, data_row: DataRow):

        self.__add_info(table_name='company', field_name='name', data=data_row.company.company_name)
        self.__add_info(table_name='period', field_name='period', data=data_row.period.period)
        self.__add_info(table_name='data_type', field_name='type', data=data_row.data_type.data_type)
        self.__add_data(data_row)

    def __add_info(self, table_name, field_name, data):
        info_in_db = self.cur.execute(f'SELECT * FROM {table_name} WHERE {field_name}="{data}"').fetchone()
        if not info_in_db:
            self.cur.execute(f"""
                        INSERT INTO {table_name} VALUES (?, ?)
                    """, (None, data))
            self.con.commit()

    def __add_data(self, data_row):
        entry_date = date(2023, 4, randint(1, 30))
        company_id = self.__get_id_by_parameter(parameter='name', data=data_row.company.company_name,
                                                table_name='company')
        period_id = self.__get_id_by_parameter(parameter='period', data=data_row.period.period, table_name='period')
        data_type_id = self.__get_id_by_parameter(parameter='type', data=data_row.data_type.data_type,
                                                  table_name='data_type')
        self.cur.execute(f"""
            INSERT into dataset VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (None, company_id, period_id, data_type_id, data_row.data['data1'], data_row.data['data2'],
              entry_date.strftime('%d/%m/%Y')))
        self.con.commit()

    def __get_id_by_parameter(self, parameter, data, table_name):
        return self.cur.execute(f"""SELECT id FROM {table_name} WHERE {parameter}=(?)""", (data,)).fetchone()[0]

    def get_total_q_grouped_by_date(self, period_str, data_type_str):
        period_id = self.__get_id_by_parameter(parameter='period', data=period_str, table_name='period')
        data_type_id = self.__get_id_by_parameter(parameter='type', data=data_type_str, table_name='data_type')

        aggregate = self.cur.execute(f"""
            SELECT TOTAL(data1), TOTAL(data2), date from dataset 
            WHERE period_id = {period_id} AND data_type_id = {data_type_id}
            GROUP BY date;
        """)
        return aggregate.fetchall()
