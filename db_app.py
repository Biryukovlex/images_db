# -*- coding: utf-8 -*-
# это простое приложение, которое создает базу данных для хранения изображений в формате BLOB на SQLite3 
# и предоставляет простой интерфейс для базовых операций с базой: 
# (создание базы, добавление новой картинки в базу, извелечение картинки по id, показать все содержимое базы)
import imagedb

db_name = 'images1.db' # напишите навазние базы данных
# Вызов функций
imagedb.get_pic('/path/to/the/directory') # путь к папке, содержимое которой можно распечатать
imagedb.create_or_open_db(db_name) # создание новой базы данных или подключение к существующей (возвращает переменную con). В скобках указать имя базы данных
filename = "/path/to/the/file.jpg" # путь к файлу, который будет загружен в базу
imagedb.insert_pic(db_name, filename) # в скобках указать имя базы данных и переменную, содержащую путь к файлу filename
imagedb.extract_pic(db_name, '1') # в скобках указать имя базы данных и индекс файла, который нужно выгрузить (если индекс больше, чем кол-во файлов в базе, то будет ошибка :)
imagedb.show_all(db_name) # в скобках указать имя базы данных