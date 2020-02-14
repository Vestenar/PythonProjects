# coding=utf-8
'''
# HE!!!!!!!
#
# запускает дочерний процесс/программу, соединяет свои потоки stdin/stdout
# с потоками stdout/stdin дочернего процесса -- операции чтения и записи на
# стороне родительского процесса отображаются на стандартные потоки ввода-вывода
# дочерней программы; напоминает соединение потоков с помощью модуля subprocess;
#
'''

import os, sys

def spawn(prog, *args):
    stdinFd = sys.stdin.fileno()
    stdoutFd = sys.stdout.fileno()

    parentStdin, childStdout = os.pipe()
    childStdin, parentStdout = os.pipe()
    pid = os.fork()
    if pid:
        os.close(childStdout)
        os.close(childStdin)
        os.dup2(parentStdin, stdinFd)
        os.dup2(parentStdout, stdoutFd)

    else:
        os.close(parentStdin)
        os.close(parentStdout)
        os.dup2(childStdin, stdinFd)
        os.dup2(childStdout, stdoutFd)
        args = (prog,) + args
        os.execvp(prog, args)
        assert False, 'execvp failed!'


if __name__ == '__main__':
    mypid = os.getpid()
    spawn('python', 'pipes-testchild.py', 'spam')       # породить дочернюю программу

    print('Hello 1 from parent', mypid)                 # to child's stdin
    sys.stdout.flush()                                  # subvert stdio buffering
    reply = input()                                     # from child's stdout
    sys.stderr.write('Parent got: "%s"\n' % reply)      # stderr not tied to pipe!

    print('Hello 2 from parent', mypid)
    sys.stdout.flush()
    reply = sys.stdin.readline()
    sys.stderr.write('Parent got: "%s"\n' % reply[:-1])