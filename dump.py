import pandas as pd
from tqdm import tqdm
import re

def convert_to_int(value):
    return int(float(value))

def remove_special_characters(value):
    return re.sub(r'[^A-Za-z0-9]+', '', value)

df = pd.read_csv('./Chicago_Crimes_2012_to_2017.csv')
file = open('./insert_script.sql', 'w')

# TIPO TABLE
primary_types = list()
for index, row in tqdm(df.iterrows(), total=df.shape[0], desc='Creating tipo table inserts'):
    have_null_value = row.isnull().values.any()
    if not have_null_value:
        line = ""
        primary_type = remove_special_characters(row['Primary Type'])
        if primary_type in primary_types:
            continue

        line += ("INSERT INTO TIPO (tipoPrimario) " \
                "VALUES ("
                f'"{primary_type}"'
                ");\n")
        file.write(line)
        primary_types.append(primary_type)

# LOCALIZACAO TABLE
locations = list()
for index, row in tqdm(df.iterrows(), total=df.shape[0], desc='Creating location table inserts'):
    have_null_value = row.isnull().values.any()
    if not have_null_value:
        line = ""
        location = remove_special_characters(row['Location'])
        if location in locations:
            continue

        locationDescription = remove_special_characters(row['Location Description'])

        line += ("INSERT INTO LOCALIZACAO (localizacao, descricaoLocal) " \
                "VALUES ("
                f'"{location}",'
                f'"{locationDescription}"'
                ");\n")
        file.write(line)
        locations.append(location)

# CASO TABLE
case_ids_list = list()
for index, row in tqdm(df.iterrows(), total=df.shape[0], desc='Creating case table inserts'):
    have_null_value = row.isnull().values.any()
    if not have_null_value:
        line = ""
        case_id = int(row['ID'])
        if case_id in case_ids_list:
            continue

        case_date = remove_special_characters(row['Date'])
        case_number = remove_special_characters(row['Case Number'])
        case_description = remove_special_characters(row['Description'])
        case_arrest = row['Arrest']
        case_iucr = remove_special_characters(row['IUCR'])
        case_pimary_type = remove_special_characters(row['Primary Type'])
        case_location = remove_special_characters(row['Location'])

        line += ("INSERT INTO CASO (idCaso, dataCaso, numeroCaso, descricao, preso, iucr, tipoPrimario, localizacao) " \
                "VALUES ("
                f'{case_id},'
                f'"{case_date}",'
                f'"{case_number}",'
                f'"{case_description}",'
                f'"{case_arrest}",'
                f'"{case_iucr}",'
                f'"{case_pimary_type}",'
                f'"{case_location}"'
                ");\n")
        file.write(line)
        case_ids_list.append(case_id)