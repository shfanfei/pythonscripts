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
            print 'source = %s' % self.source
            print 'target = %s' % self.target
        finally:
            file_object.close()

    def copyFiles(self):
        for f in os.listdir(self.source):
            sf = os.path.join(self.source,f)
            tf = os.path.join(self.target,f)
            if os.path.isfile(sf):
                if not os.path.exists(self.target):
                    os.makedirs(self.target)
                if not os.path.exists(tf) or (os.path.exists(tf)
                        and (os.path.getsize(tf) != (os.path.getsize(sf)))):
                    open(tf,'wb').write(open(sf,'rb').read())
                    print 'copy file %s' % sf

if __name__ == '__main__':
    oper = FileOper()
    oper.readConfig()
    oper.copyFiles()
