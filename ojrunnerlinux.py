import lorun
import os
import codecs
import random
import subprocess
import config
import sys

RESULT_MAP = [
    2, 10, 5, 4, 3, 6, 11, 7, 12
]

class Runner:
    def __init__(self):
        return

    def compile(self, judger, srcPath, outPath):
        cmd = config.langCompile[judger.lang] % {'root': sys.path[0], 'src': srcPath, 'target': outPath}
        p = subprocess.Popen(cmd, shell = True,
          stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.STDOUT)
        retval = p.wait()
        return (retval, p.stdout.read())

    def judge(self, judger, srcPath, outPath, inFile, ansFile, memlimit, timelimit):
        cmd = config.langRun[judger.lang] % {'src': srcPath, 'target': outPath}
        fout_path = "".join([sys.path[0], "/", "%s/%d.out" % (config.dataPath["tempPath"], random.randint(0, 65536))])
        
        if os.path.exists(fout_path):
            os.remove(fout_path)

        fin = open(inFile, 'rU')
        fout = open(fout_path, 'w')
        runcfg = {
            'args': cmd.split(" "),
            'fd_in': fin.fileno(),
            'fd_out': fout.fileno(),
            'timelimit': int(timelimit),
            'memorylimit': int(memlimit)
        }

        rst = lorun.run(runcfg)
        fin.close()
        fout.close()

        if rst['result'] == 0:
            fans = open(ansFile, 'rU')
            fout = open(fout_path, 'rU')
            crst = lorun.check(fans.fileno(), fout.fileno())
            fout.close()
            fans.close()
            return (RESULT_MAP[crst], int(rst['memoryused']), int(rst['timeused']))

        return (RESULT_MAP[rst['result']], 0, 0)
