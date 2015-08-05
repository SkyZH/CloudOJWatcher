ojconfig = {
    "host" : "192.168.0.105",
    "requestpath" : "/oj/watcherapi",
    "apikey" : "bhbeSbpt2NTt5SOfyTrdeG4Vxa1PIr1ONgx7lxO18G2kPrjBuG"
}

dataPath = {
    'probPath': './data/prob/',
    'execPath': './data/exec/',
    'codePath': './data/code/',
    'tempPath': './data/temp/'
}

langCompile = {
    0: "g++ -x c++ -O2 -Wall -lm -DONLINE_JUDGE --static --std=c++98 -fno-asm %(src)s -o %(target)s",
    1: "gcc -x c -O2 -Wall -lm -DONLINE_JUDGE --static --std=c99 -fno-asm %(src)s -o %(target)s",
    2: "g++ -x c++ -O2 -Wall -lm -DONLINE_JUDGE --static --std=c++11 -fno-asm %(src)s -o %(target)s",
    6: "fpc -O2 -dONLINE_JUDGE %(src)s -o%(target)s",
    4: "",
    5: "",
    3: "",
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
    6: "%(target)s",
    4: "",
    5: "",
    3: "",
    7: "",
    8: "",
    9: "",
    10: "",
    11: ""
}

langMap = {
    "Pending" : 0,
    "Compiling" : 1,
    "Accepted" : 2,
    "Wrong Answer": 3,
    "Memory Limit Excceed" : 4,
    "Time Limit Excceed" : 5,
    "Runtime Error" : 6,
    "Compile Error" : 7,
    "Running" : 8,
    "Unknown" : 9,
    "Presentation Error" : 10,
    "Output Limit Excceed" : 11,
    "System Error" : 12
}
