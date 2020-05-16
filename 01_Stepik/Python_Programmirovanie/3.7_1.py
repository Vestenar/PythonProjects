'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд
с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
'''
tabl = [input().split( ';' ) for i in range( int( input() ) )]
team = []
for i in range( len( tabl ) ):
    if tabl[i][0] not in team:
        team.append( tabl[i][0] )
    if tabl[i][2] not in team:
        team.append( tabl[i][2] )

for i in range( int( len( team ) ) ):
    igr = 0
    pobed = 0
    nich = 0
    porazh = 0
    och = 0
    for j in range( int( len( tabl ) ) ):
        if team[i] in tabl[j]:
            igr += 1
            if (team[i] == tabl[j][0] and tabl[j][1] > tabl[j][3]) or (
                    team[i] == tabl[j][2] and tabl[j][1] < tabl[j][3]):
                pobed += 1
                och += 3
            elif tabl[j][1] == tabl[j][3]:
                nich += 1
                och += 1
            else:
                porazh += 1

    print(
        team[i] + ':' + str( igr ) + ' ' + str( pobed ) + ' ' + str( nich ) + ' ' + str( porazh ) + ' ' + str( och ) )

'''
35
Франция;1;Румыния;1
Албания;0;Швейцария;1
Уэльс;2;Словакия;1
Англия;1;Россия;1
Турция;0;Хорватия;1
Польша;1;Северная Ирландия;0
Германия;2;Украина;0
Испания;1;Чехия;0
Бельгия;0;Италия;2
Австрия;0;Венгрия;2
Португалия;1;Исландия;1
Россия;1;Словакия;2
Румыния;1;Швейцария;1
Франция;2;Албания;0
Англия;2;Уэльс;1
Украина;0;Северная Ирландия;2
Германия;0;Польша;0
Италия;1;Швеция;0
Чехия;2;Хорватия;2
Испания;3;Турция;0
Бельгия;3;Ирландия;0
Исландия;1;Венгрия;1
Португалия;0;Австрия;0
Швейцария;0;Франция;0
Румыния;0;Албания;1
Словакия;0;Англия;0
Россия;0;Уэльс;3
Северная Ирландия;0;Германия;1
Украина;0;Польша;1
Хорватия;0;Испания;1
Чехия;0;Турция;2
Венгрия;0;Португалия;3
Исландия;2;Австрия;1
Швеция;1;Бельгия;1
Италия;2;Ирландия;1

'''