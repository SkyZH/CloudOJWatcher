ojconfig = {
    "host" : "oj.localhost",
    "requestpath" : "/oj/watcherapi",
    "apikey" : "asdfhlsaeilcasdlhuf",
    "judger" : "Judger Name"
}

dataPath = {
    'probPath': './data/prob/',
    'execPath': './data/exec/',
    'codePath': './data/code/',
    'tempPath': './data/temp/'
}

langCompile = {
    0: "g++ -x c++ -Wall -lm -DONLINE_JUDGE --static --std=c++98 -fno-asm %(src)s -o %(target)s",
    1: "gcc -x c -Wall -DONLINE_JUDGE --static --std=c99 -fno-asm %(src)s -lm -o %(target)s",
    2: "g++ -x c++ -Wall -lm -DONLINE_JUDGE --static --std=c++11 -fno-asm %(src)s -o %(target)s",
    3: "",
    4: "",
    5: "",
    6: "fpc -O2 -dONLINE_JUDGE %(src)s -o%(target)s",
    7: "",
    8: "",
    9: "",
    10: "",
    11: ""
}

langRun = {
    0: "%(target)s",
    1: "%(target)s",
    2: "%(target)s",
    3: "",
    4: "",
    5: "",
    6: "%(target)s",
    7: "",
    8: "",
    9: "",
    10: "",
    11: ""
}
