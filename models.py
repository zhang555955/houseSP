#coding:utf-8

import peewee

db = peewee.SqliteDatabase("house.db")

class House(peewee.Model):
    houseName = peewee.CharField(max_length = 64)
    houseUrl = peewee.CharField(max_length=64)
    houseUser = peewee.CharField(max_length=64)
    userPF = peewee.CharField(max_length=64)
    lookNum = peewee.CharField(max_length=64)

    class Meta:
        database = db

if __name__ == "__main__":
    House().create_table()