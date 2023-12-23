from utils.compilerToCode import *

def getCompiler(questionID, i):
    compile = questionID[i + 1:]
    if (compile == "cpp"):
        return compilerToCode["GNU G++20 11.2.0 (64 bit, winlibs)"]
    elif (compile == "c"):
        return compilerToCode["GNU GCC C11 5.1.0"]
    elif (compile == "java"):
        return compilerToCode["Java 17 64bit"]
    elif (compile == "py"):
        return compilerToCode["Python 3.8.10"]
    elif (compile == "cs"):
        return compilerToCode["C# 10, .NET SDK 6.0"]
    elif (compile == "js"):
        return compilerToCode["Node.js 15.8.0 (64bit)"]
    elif (compile == "kt"):
        return compilerToCode["Kotlin 1.7.20"]
    elif (compile == "rs"):
        return compilerToCode["Rust 1.72.0 (2021)"]
    elif (compile == "go"):
        return compilerToCode["Go 1.19.5"]
    elif (compile == "scala"):
        return compilerToCode["Scala 2.12.8"]
    elif (compile == "hs"):
        return compilerToCode["Haskell GHC 8.10.1"]
    elif (compile == "d"):
        return compilerToCode["D DMD32 v2.105.0"]
    elif (compile == "pas"):
        return compilerToCode["Free Pascal 3.2.2"]
    else:
        # throw error
        print("Invalid file extension")
        exit(0)