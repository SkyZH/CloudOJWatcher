import config
import oj
import random
import subprocess
import codecs
import os
import sys
import ojrunnerwin
import ojrunnerlinux
import status

class Judger:
    def __init__(self, client, sid, pid, lang):
        self.client = client
        self.sid = sid
        self.pid = pid
        self.lang = lang
        self.runner = ojrunnerlinux.Runner()

    def compile(self, srcPath, outPath):
        return self.runner.compile(self, srcPath, outPath)

    def judge(self, srcPath, outPath, inFile, ansFile, memlimit, timelimit):
        return self.runner.judge(self, srcPath, outPath, inFile, ansFile, memlimit, timelimit)

    def run(self):
        srcPath = "%s/%s/%s_%d.code" % (sys.path[0], config.dataPath["codePath"], self.sid, random.randint(0, 65536))
        outPath = "%s/%s/%s_%d.exe" % (sys.path[0], config.dataPath["execPath"], self.sid, random.randint(0, 65536))
        self.saveCode(srcPath)
        retdata = "Judged by %s\n=========\n" %(config.ojconfig["judger"])

        print("    Compiling...")
        retVal, retData = self.compile(srcPath, outPath)
        if(retVal != 0):
            self.putRet("%s%s" % (retdata, retData.decode()))
            self.putStatus(7, 0, 0)
            return 0
        else:
            self.putStatus(8, 0, 0)

        print("    Getting Data...")

        prob_data = self.getDataList(self.pid)
        datalist = prob_data["datalist"]

        for key in datalist:
            if self.hasData(key, datalist[key], "in") == False:
                dat = self.getData(key, "in")
                self.saveData(key, datalist[key], "in", dat)
            if self.hasData(key, datalist[key], "out") == False:
                dat = self.getData(key, "out")
                self.saveData(key, datalist[key], "out", dat)

        print("    Judging...")
        retval = 2
        mem = 0
        time = 0
        jcount = 0

        _sorted_data_list = sorted(datalist, key=lambda d:int(d), reverse = False)

        for _key in _sorted_data_list:
            key = str(_key)
            retval, _mem, _time = self.judge(srcPath, outPath, self.__getDataPath(key, datalist[key], "in"),
              self.__getDataPath(key, datalist[key], "out"), prob_data["memlimit"], prob_data["timelimit"])
            jcount += 1
            mem += _mem
            time += _time
            retdata = retdata + "%s on Test %s | Time %d ms    Memory %d KB\n" % (status.langMap[retval], datalist[key].ljust(30), _time, _mem)
            self.putRet(retdata)
            if(retval != 2):
                self.putStatus(retval, mem / jcount, time / jcount)
                break
        if(retval == 2):
            self.putStatus(retval, mem / jcount, time / jcount)
        print("Complete")
        return 0

    def saveCode(self, path):
        code = self.client.GetCode(self.sid)
        fp = codecs.open(path, 'a', 'utf-8')
        fp.write(code.decode('utf-8'))
        fp.close()

    def putRet(self, ret):
        self.client.PutRet(self.sid, ret.encode())

    def putStatus(self, retcode, mem, time):
        self.client.PutStatus(self.sid, retcode, mem, time)

    def getDataList(self, pid):
        return self.client.GetDataList(pid)

    def getData(self, pdid, ext):
        return self.client.GetData(pdid, ext)

    def __getDataPath(self, pdid, name, ext):
        return "%s/%s/%s_%s.%s" % (sys.path[0], config.dataPath["probPath"], str(pdid), name, ext)

    def saveData(self, pdid, name, ext, data):
        fp = open(self.__getDataPath(pdid, name, ext), 'w')
        fp.write(data.decode())
        fp.close()

    def hasData(self, pdid, name, ext):
        return os.path.exists(self.__getDataPath(pdid, name, ext))

    def readData(self, path):
        fp = open(path, 'rU')
        __dat = fp.read().encode()
        fp.close()
        return __dat
