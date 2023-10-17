import re

# Открываем SQL-файл для чтения
with open('cost_postgre.sql', 'r') as file:
    sql_content = file.read()

# Удаляем символы "[" и "]"
sql_content = sql_content.replace('data_gko2023','gko_data2023').replace('data','gko_data').replace('[main].', '').replace('[', '').replace(']', '').replace('rowid,','')

# Заменяем "ID" на "id", "KN" на "kn" и "KC" на "kc"
sql_content = sql_content.replace('ID', 'id').replace('KN', 'kn').replace('KC', 'kc').replace('DocType', 'doc_type').replace('DocNum', 'doc_num').replace('DocDate', 'doc_date').replace('DocName', 'doc_name').replace('URL', 'url').replace('DateTime', 'date_time').replace('Author', 'author').replace('Comment', 'comment').replace('DateFound', 'date_found').replace('Status', 'status').replace('DateStart', 'date_start').replace('DatePlacement', 'date_placement').replace('SKC', 'skc').replace('TPU', 'tpu').replace('Area', 'area').replace('CodeKU', 'code_ku').replace('NameKU', 'name_ku').replace('Commun', 'commun').replace('Model', 'model')
sql_content = re.sub(r'VALUES\((\d+), \1,', r'VALUES(\1,', sql_content)

# Записываем обновленный SQL-код обратно в файл
with open('your_sql_file_updated.sql', 'w') as file:
    file.write(sql_content)

print("Файл успешно обновлен.")

