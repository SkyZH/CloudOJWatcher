import lorun
import os
import codecs
import random
import subprocess


RESULT_MAP = [
    2, 10, 5, 4, 3, 6, 11, 7, 12
]

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
        fout_path = "".join([sys.path[0], "/", "%s/%d.out" % (config.dataPath["tempPath"], random.randint(0, 65536)))
        fin = codecs.open(inFile, 'r', 'utf-8')
        fout = codecs.open(fout_path, 'w', 'utf-8')

        runcfg = {
            'args':[cmd],
            'fd_in':fin.fileno(),
            'fd_out':fout.fileno(),
            'timelimit': timelimit,
            'memorylimit':memlimit
        }

        rst = lorun.run(runcfg)
        fin.close()
        ftemp.close()

        if rst['result'] == 0:
            fans = codecs.open(ansFile, 'r', 'utf-8')
            fout = codecs.open(fout_path, 'r', 'utf-8')
            crst = lorun.check(fans.fileno(), fout.fileno())
            fout.close()
            fans.close()
            if crst != 0:
                return RESULT_MAP[crst]

        if os.path.exists(fout_path):
            os.remove(fout_path)

        return rst
