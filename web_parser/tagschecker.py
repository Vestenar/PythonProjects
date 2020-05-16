from DBcm import UseDatabase, DBConnectionError, DBCredentialsError, SQLError
from threading import Thread
import json

dbconfig_tags = {'host': '127.0.0.1',
                 'user': 'search',
                 'password': '1234',
                 'database': 'teamhook', }


def read_tags(tag):
    try:
        with UseDatabase(dbconfig_tags) as cursor:
            _SQL = """SELECT EXISTS(SELECT id FROM tags WHERE tag_name = %s)"""
            cursor.execute(_SQL, (tag,))
            return cursor.fetchall()[0][0]

    except DBConnectionError as err:  # в случае, когда ДБ не найдена
        print('Is DB accessible? Error: ', str(err))
    except DBCredentialsError as err:  # в случае неверных учетных данных к БД
        print('Problem with authorisation. ', str(err))
    except SQLError as err:
        print('Wrong query to DB? ', str(err))  # в случае неверного запроса к БД
    except Exception as err:  # во всех остальных случаях
        print('Something went wrong. Error: ', str(err))
    return 'Error'


tf_tags = ["фриланс", "энциклопедя", "стартап", "маркетинг", "создание сегмента", 'gifts', 'facebook',
           'social commerce', 'aggregator', 'e-commerce']
while tf_tags:
    tf_tag = json.dumps(tf_tags[:1], ensure_ascii=False)
    tf_tags = tf_tags[1:]
    if not read_tags(tf_tag):
        print(tf_tag, 'ready to add')
        with UseDatabase(dbconfig_tags) as cursor:
            _SQL = """insert into tags
                    (tag_name)
                    values
                    (%s)"""
            cursor.execute(_SQL, (tf_tag,),
                           )
