from flask import Flask, render_template, request, session, copy_current_request_context
from search import search
from DBcm import UseDatabase, DBConnectionError, DBCredentialsError, SQLError
from checker import check_logged_in
from threading import Thread
from time import sleep

app = Flask(__name__)
app.secret_key = 'supersecret'
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'search',
                          'password': '1234',
                          'database': 'searchlogDB', }


@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(search(phrase, letters))
    @copy_current_request_context
    def log_request(req, res):
        sleep(10)
        try:
            with UseDatabase(app.config['dbconfig']) as cursor:
                _SQL = """insert into log
                        (phrase, letters, ip, browser_string, results)
                        values
                        (%s, %s, %s, %s, %s)"""
                cursor.execute(_SQL, (req.form['phrase'],
                                      req.form['letters'],
                                      req.remote_addr,
                                      req.user_agent.browser,
                                      res,))
        except Exception as err:
            print('Some trouble with inserting to DB: ', str(err))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:                    # exception на ошибки подключения к БД при записи
        print('*****Something went wrong while request to BD: ', str(err))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html',
                           the_title='Welcome to search web app')


@app.route('/viewlog')
@check_logged_in
def viewlog():
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select id, phrase, letters, ip, browser_string, results, ts
                    from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ('ID', 'Phrase', 'Letters', 'Remote Address', 'User agent', 'Results', 'Timestamp')
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents,)
    except DBConnectionError as err:            # в случае, когда ДБ не найдена
        print('Is DB accessible? Error: ', str(err))
    except DBCredentialsError as err:           # в случае неверных учетных данных к БД
        print('Problem with authorisation. ', str(err))
    except SQLError as err:
        print('Wrong query to DB? ', str(err))  # в случае неверного запроса к БД
    except Exception as err:                    # во всех остальных случаях
        print('Something went wrong. Error: ', str(err))
    return 'Error'

@app.route('/login')
def login():
    session['logged_in'] = True
    return 'Logged in successfully'


@app.route('/logout')
def logout():
    session.pop('logged_in')
    return 'Logged out'


if __name__ == '__main__':
    app.run(debug=True)
