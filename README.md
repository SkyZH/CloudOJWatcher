# CloudOJ Watcher
CloudOJ's Status Watcher, take the place of SNGOJWatcher

## License

CloudOJ's Status Watcher is under Apache License.

## CloudOJ

See CloudOJ [HERE](https://github.com/SkyZH/CloudOJ)

## Feedback

    print("iSkyZH%sgmail.com" % ("@"));
    print("iSkyZH%s163.com" % ("@"));

## Usage

0. git clone ...
1. Create config.py (or `<Watcher>/config/__init__.py`)
2. Install Compilers (gcc g++ fpc)
3. Edit apikey in CloudOJ's config.ini
4. Run `python3 main.py' (or Supervisor)

## Installation

On Linux:

    git clone git@github.com:lodevil/Lo-runner.git
    cd Lo-runner
    python3 setup.py install

Then python will automatically build Lo-runner and then install it.

You may also need gcc, g++ and fpc for complete compiler support.

Watcher now don't supprt Windows platform.

## config.py Example

    ojconfig = {
        "host" : "localhost",
        "requestpath" : "/oj/watcherapi",
        "apikey" : "abcdefgasdklfjasenrhaushjfkjasblvkjdasvd"
    }

    dataPath = {
        'probPath': './data/prob/',
        'execPath': './data/exec/',
        'codePath': './data/code/',
        'tempPath': './data/temp/'
    }

    langCompile = {
        0: "g++ -x c++ -O2 -Wall -lm -DONLINE_JUDGE --static --std=c++98 -fno-asm %(src)s -o %(target)s",
        1: "gcc -x c -O2 -Wall -DONLINE_JUDGE --static --std=c99 -fno-asm %(src)s -lm -o %(target)s",
        2: "g++ -x c++ -O2 -Wall -lm -DONLINE_JUDGE --static --std=c++11 -fno-asm %(src)s -o %(target)s",
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
