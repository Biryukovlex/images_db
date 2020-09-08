# -*- coding: utf-8 -*-
import sqlite3
import sys
import os.path
from os import listdir

def get_pic(abs_path):
	print("\n" + "That's what in the directory  " + abs_path + ":")
	dir_files = os.listdir(abs_path)
	print(dir_files)
	print("\n")

# Функция создания или открытия существующей базы данных
def create_or_open_db(db_file):
	db_is_new = not os.path.exists(db_file)
	conn = sqlite3.connect(db_file)
	c = conn.cursor()
	if db_is_new:
		print('Creating new database...\n')
		c.execute("""CREATE TABLE IF NOT EXISTS images_data(
				name TEXT,
				picture BLOB
				)
		""")
	else:
		print('Database already exists!\n')
		return(conn)

# Функция загрузки изображения в бинарном режиме в базу данных
def insert_pic(db_file, filename):
	conn = sqlite3.connect(db_file)
	with open(filename, 'rb') as f:
		ablob = f.read()
		pic_name = os.path.basename(filename)
		print("Uploading " + pic_name + "...")
		# Конвертируем данные
		binary = sqlite3.Binary(ablob)
		conn.execute("INSERT INTO images_data VALUES (?, ?)", (pic_name, binary))
		conn.commit()
		print('New pic was committed successfully!\n')
		conn.close()

# Функция выгрузки изображения в текущую директорию и конвертации в нормальный вид
def extract_pic(db_file, pic_id):
	print("Extracting file...")
	conn = sqlite3.connect(db_file)
	c = conn.cursor()
	c.execute("SELECT * FROM images_data WHERE rowid = (?)", pic_id)
	name, picture = c.fetchone()
	with open(name, 'wb') as output:
		output.write(picture)
	print("The file " + name + " was placed in the current directory\n")
	conn.close()

# Запрос на показ всех файлов из БД
def show_all(db_file):
	print ("Here is your base:\n")
	conn = sqlite3.connect(db_file)
	conn.text_factory = str
	c = conn.cursor()
	c.execute("SELECT rowid, * FROM images_data ORDER BY rowid")
	items = c.fetchall()
	for item in items:
		print(item)
	conn.commit()
	print("That's all we have in the base now :)")
	conn.close()