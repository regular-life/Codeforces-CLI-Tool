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

from utils.getCompiler import *

def getQuestionID(pathToCode):
    n = len(pathToCode)
    mx = 0
    for i in range(n):
        if pathToCode[i] == '/':
            mx = i
            
    questionID = pathToCode[mx + 1:]
    n = len(questionID)
    for i in range(n):
        if questionID[i] == '.':
            compiler = getCompiler(questionID, i)
            questionID = questionID[:i]
            break
    return questionID, compiler