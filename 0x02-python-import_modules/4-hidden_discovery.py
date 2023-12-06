#!/usr/bin/python3
if __name__ == '__main__':
    import imp
    filename_pyc = 'hidden_4.pyc'
    for i in dir(filename_pyc):
        if i[0] != '_':
            print("{}".format(i))
