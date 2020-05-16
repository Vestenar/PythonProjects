# -*- coding: utf-8 -*-
import sys
import time
import json
from authorization import login, send_message
from parser import parse
from DBcm import UseDatabase, DBConnectionError, DBCredentialsError, SQLError
from threading import Thread


dbconfig_projects = {'host': '127.0.0.1',
                     'user': 'search',
                     'password': '1234',
                     'database': 'teamhook', }

dbconfig_tags = {'host': '127.0.0.1',
                 'user': 'search',
                 'password': '1234',
                 'database': 'teamhook', }


def fill_data(tf_title, tf_text, tf_tags):
    def read_tags(tag):
        try:
            with UseDatabase(dbconfig_tags) as cursor:
                _SQL = """SELECT EXISTS(
                            SELECT id FROM tags
                            WHERE tag_name = %s)"""
                cursor.execute(_SQL, (tag,))
                return cursor.fetchall()[0][0]

        except DBConnectionError as err:  # ДБ не найдена
            print('Is DB accessible? Error: ', str(err))
        except DBCredentialsError as err:  # неверные учетные данные к БД
            print('Problem with authorisation. ', str(err))
        except SQLError as err:
            print('Wrong query to DB? ', str(err))  # неверный запрос к БД
        except Exception as err:  # все остальные ошибки
            print('Something went wrong. Error: ', str(err))
        return 'Error'

    with UseDatabase(dbconfig_projects) as cursor:
        _SQL = """insert into projects
                    (title, description, text, user_id, created_at, status)
                    values
                    (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (tf_title,
                              'Введите Ваше краткое описание',
                              tf_text,
                              '5',
                              time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                              'Active'
                              ))

    while tf_tags:
        tf_tag = json.dumps(tf_tags[:1], ensure_ascii=False)
        tf_tags = tf_tags[1:]
        if not read_tags(tf_tag):
            with UseDatabase(dbconfig_tags) as cursor:
                _SQL = """insert into tags
                            (tag_name)
                            values
                            (%s)"""
                cursor.execute(_SQL, (tf_tag,),
                               )


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('USAGE: >>> python tfparser.py <from_index> <to_index>')
        # TODO убрать start|stop
        start_index = 2993
        stop_index = 2994
    else:
        start_index = int(sys.argv[1])
        stop_index = int(sys.argv[2])
    login()
    for index in range(start_index, stop_index + 1):
        time.sleep(0.5)
        data_to_db, author = parse(index)
        print(data_to_db)
        if not data_to_db: continue

        try:
            writedb_thread = Thread(target=fill_data, args=data_to_db)
            writedb_thread.start()
        except Exception as err:  # exception на ошибки подключения к БД при записи
            print('*****Something went wrong while request to BD: ', str(err))

        # TODO реализовать рассылку сообщений, вероятно с применением процесса
        # if author['link'] == 'leptodon':
        #     send_message(author['link'])

        endline = "#" * 80
        print(endline, '\n')
