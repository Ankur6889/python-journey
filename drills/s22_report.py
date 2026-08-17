"""
One function that accepts ANY call.

    report(...) must accept any number of positional arguments and any
    keyword arguments, in any mix, without knowing their names in advance.

    It returns a 2-item tuple:
        (all positionals, in order  ,  all keywords as name->value)

Examples of calls it must survive:
    report(1, 2, x=3)        ->  ((1, 2), {"x": 3})
    report()                 ->  ?    (you decide what falls out)
    report(a=1, b=2)         ->  ((), {"a": 1, "b": 2})
"""


def report(*args,**kwargs):
    return args,kwargs 
