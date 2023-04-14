from pprint import pprint
from parser import XlsxParser
from db_engine import DBEngine

file_path = "Приложение_к_заданию_бек_разработчика.xlsx"
parser = XlsxParser(file_path=file_path)

parser.parse_xlsx()

db_engine = DBEngine(data=parser.data_rows, sqlite_db_path=':memory:')
db_engine.fill_db()

fact_total_qliq_grouped_by_date = db_engine.get_total_q_grouped_by_date(period_str='fact', data_type_str='Qliq')
fact_total_qoil_grouped_by_date = db_engine.get_total_q_grouped_by_date(period_str='fact', data_type_str='Qoil')
forecast_total_qliq_grouped_by_date = db_engine.get_total_q_grouped_by_date(period_str='forecast', data_type_str='Qliq')
forecast_total_qoil_grouped_by_date = db_engine.get_total_q_grouped_by_date(period_str='forecast', data_type_str='Qoil')

pprint('Расчетный TOTAL по Qliq фактический: ')
pprint(fact_total_qliq_grouped_by_date)
pprint('Расчетный TOTAL по Qoil фактический: ')
pprint(fact_total_qoil_grouped_by_date)
pprint('Расчетный TOTAL по Qliq прогнозируемый: ')
pprint(forecast_total_qliq_grouped_by_date)
pprint('Расчетный TOTAL по Qoil прогнозируемый: ')
pprint(forecast_total_qoil_grouped_by_date)
