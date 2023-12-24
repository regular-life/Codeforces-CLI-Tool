"""
Copyright (C) 2023 yash

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

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