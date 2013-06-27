# coding=utf-8
"""
用于同步2个不同文件夹下的文件
从config.txt配置文件中读取源目录和目标目录
"""
import os

class FileOper:
    #同步目标目录
    target = ''
    #同步原目录
    source = ''

    #读取配置文件
    def readConfig(self):
        file_object = open('config.txt')
        dic = {}
        try:
            for line in file_object:
                d = line.rstrip('\n').split(':')
                dic[str(d[0])] = d[1]
            self.source = dic['source_dir']
            self.target = dic['target_dir']
            print 'source = %s,target = %s' % (self.source,self.target)
        finally:
            file_object.close()


class DirCompare:
    def compare(self,source,target):
        print os.listdir(source)
        ss = [ s for s in os.listdir(source) if
                os.path.isfile(os.path.join(os.curdir,s))]
        print ss


if __name__ == '__main__':
    oper = FileOper()
    oper.readConfig()
    compare = DirCompare()
    compare.compare(oper.source,oper.target)

