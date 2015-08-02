import config
import subprocess
import sys
import random

class Runner:
    def __init__(self):
        return

    def compile(self, judger, srcPath, outPath):
        cmd = config.langCompile[judger.lang] % {'src': srcPath, 'target': outPath}
        p = subprocess.Popen(cmd, shell = True,
          stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.STDOUT)
        retval = p.wait()
        return (retval, p.stdout.read())

    def judge(self, judger, srcPath, outPath, inFile, ansFile, memlimit, timelimit):
        cmd = "".join([sys.path[0], "/", config.langRun[judger.lang] % {'src': srcPath, 'target': outPath}])
        p = subprocess.Popen(cmd, shell = True,
          stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        retVal = 9
        try:
            out, err = p.communicate(input = judger.readData(inFile), timeout = int(timelimit) / 1000)
        except subprocess.TimeoutExpired:
            p.kill()
            retVal = 5
        if(retVal == 9):
            if(p.returncode != 0):
                retVal = 6
            else:
                retVal = 2
        return retVal
