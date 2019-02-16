import re


def programTranslation(solution, args):
    argumentVariants = '|'.join(args)
    pattern = "(?<=[^0-9a-zA-Z$_])("+argumentVariants+")(?=[^0-9a-zA-Z$_])"
    repl = r"$\1"
    return re.sub(pattern, repl, solution)


solution = "function findSum(a, $cnt) {\t  var a0 = $a;\t  for (var _cnt = 0, _cnt < cnt; _cnt++)\t    " \
           "a0 += _cnt;\t  return a0;\t}"
args = ["a", "cnt"]

print(programTranslation(solution, args))


'''
As an avid user of CodeSignal, you find it frustrating that there are no debugging 
and recovery tasks in your favorite language, PHP. 
You decide to help the platform by translating solutions in JavaScript into PHP.

You quickly discover that this approach is quite convenient: sometimes all you have to do is substitute the function arguments by adding the $ sign in front of them. At first you do this manually, but soon realize that it won't get you far enough.

Now you need to implement a function that, given a solution written in JavaScript and its args, adds a $ sign in front of each args[i] (unless there is already a dollar sign present).

Given a solution in JavaScript and its args, return the almost-PHP solution.

Example

For

solution = 
    "function add($n, m) {\t
       return n + $m;\t
     }"

and args = ["n", "m"], the output should be

programTranslation(solution, args) =
    "function add($n, $m) {\t
       return $n + $m;\t
     }"
'''
