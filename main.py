from datetime import datetime
import time
import pymongo
import os

myclient = pymongo.MongoClient("mongodb://root:12345@localhost:27017/")

mydb = myclient['logger']


mycol = mydb[os.path.basename(__file__)]

def logger(f):
    
    def wrapper(*args, **kwargs):
        global mycol
        start = time.time()
        print(args, end='\n ------------------- \n')
        print(kwargs)
        print('working time', datetime.now())
        try:
            
            result = f(*args, **kwargs)
            isledi = True
        except Exception as e:
            isledi = False
            result = str(e)
        stop = time.time()
        dt  = stop - start
        print('func name', f.__name__, 'Proses muddeti', dt)
        log = {
            'func_name': f.__name__,
            'args': args,
            'kwargs': kwargs,
            'working_time': datetime.now(),
            'process_time': dt,
            'is_worked': isledi,
            'result': result,
        }
        mycol.insert_one(log)
        return result
    return wrapper

@logger
def divide(a, b):
    return a/b

@logger
def sum(a, b):
    return a+b

a = input('Birinci ededi daxil edin:')
b = input('Ikinci ededi daxil edin:')

if a.isdigit() and b.isdigit():
    print('Nisbet:', divide(int(a),int(b)))
    print('Cemi:', sum(int(a),int(b)))
else:
    print('Herif daxil etmeyin')
