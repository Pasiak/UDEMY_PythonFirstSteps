#LAB

import datetime
import os


data_input_catalog = r'c:\temp\data_input'
data_output_catalog = r'c:\temp\data_output'
today = datetime.date.today()
today_output_catalog = os.path.join(data_output_catalog,today.strftime("%Y-%m-%d"))
print(today_output_catalog)

is_input_catalog_ok = os.path.isdir(data_input_catalog)
print(is_input_catalog_ok)

is_output_catalog_ok = os.path.isdir(data_output_catalog)
print(is_output_catalog_ok)

is_today_output_catalog_ok  = os.path.isdir(today_output_catalog) and os.path.isfile(today_output_catalog)
print(is_today_output_catalog_ok )

if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print('Conditions met! We can continue!')
else:
    print('No catalogs')
    print('Input catalog status:',is_input_catalog_ok)
    print('Output catalog status:',is_output_catalog_ok)
    print('Today catalog status:',is_today_output_catalog_ok)
