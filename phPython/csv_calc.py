# coding: utf-8
import sys
import numpy as np
# import pandas as pd

#---------------------------------
def calc_csv( myfile_path, cmd ):
    import codecs
    filecp = codecs.open(myfile, encoding = 'utf-8-sig')
    data = np.loadtxt(filecp , delimiter=',', skiprows=0)[:,1::2]
    if cmd == 1:
        ret = data.sum()
    elif cmd == 2:
        ret = data.mean()
    elif cmd == 3:
        ret = data.max()
    elif cmd == 4:
        ret = data.min()
    else:
        print("invalid command")
        ret = 0
    
    return ret
    # print(ret) 終わりだと第２引数でNoneが追加される

#---------------------------------
# argv[1] : file path
# argv[2] : command 1:sum, 2:average, 3:max, 4:min
if __name__ == '__main__':
    ary_argv = sys.argv
    myfile = ary_argv[1]
    cmd   = int(ary_argv[2])
    print(calc_csv(myfile, cmd))
    

# loadtxtより高機能なgenfromtxt
# csvが「BOM」つきUTFになっているため(先頭に3byteつく)読み込めない
# data1 = numpy.loadtxt("***.csv", delimiter=",", usecols=(0,2,4,6,8))でもできるよ