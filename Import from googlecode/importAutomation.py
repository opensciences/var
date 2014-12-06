relativePath = "issues/"

import os, re, datetime

def extractSummary(fileContents):
    return re.search("^#summary ([^\n]+)\n", fileContents).group(1)

def extractAuthor(fileContents):
    return re.search(r"\|\| Donated by \[?[^ ]* ?([^\]]+)\]? \|\|", fileContents).group(1)

def genHeader(baseName, fileContents):
    summary = extractSummary(fileContents)
    author = extractAuthor(fileContents)
    return """---
title: """ + baseName + """
excerpt: """ + summary + """
layout: repo
author: """ + author + """
---
"""

def doDeletions(fileContents):
    return re.sub(r"#summary [^\n]+\n#labels [^\n]+\n\n<wiki:toc max_depth=\"2\" />", "", fileContents)

def changeHeaders(fileContents):
    return re.sub(r"\n= ([^\n]+) =\n", r"\n#\1\n", fileContents)

def reformatLinks(fileContents):
    return re.sub(r"\[([^ ]+) ([^\]]+)\]", r"[\2](\1)", fileContents)

def changeURLs(fileContents, relativePath):
    sub = re.sub("http://promisedata.googlecode.com/svn/trunk/[^/]+/", "https://terapromise.csc.ncsu.edu:8443/svn/repo/" + relativePath, fileContents)
    return re.sub("http://code.google.com/p/promisedata/source/browse/trunk/[^/]+/", "https://terapromise.csc.ncsu.edu:8443/svn/repo/" + relativePath, sub)

def removeExtraneousLinks(fileContents):
    return fileContents

def reformatTables(fileContents):
    sub = re.sub(r"When \|\| What", r"When \| What\r---- | ----", fileContents)
    return re.sub(r"\|\| ([^|]+) \|\| ([^|]+) \|\|", r"\1 | \2", sub)

def extractDateString(fileContents):
    result = re.search(r"\n\|\| *([^ |]+ [^ |]+ [^ |]+) *\|\| Donated by[^|]+\|\|\n", fileContents).group(1)
    return result

def dateAddedString(fileContents):
    dateString = extractDateString(fileContents)
    date = datetime.datetime.strptime(dateString, "%B %d, %Y").date()
    return date.strftime("%Y-%m-%d-")

directory =  "/Users/Carter/Documents/OpenSciences/opensciences.github.io/repo/" + relativePath + "_posts/"
writeDirPath = "/Users/Carter/Documents/OpenSciences/opensciences.github.io/repo/" + relativePath + "_posts/"


for subdir, dirs, files in os.walk(directory):
    for eachFileName in files:
        print(eachFileName)
        if eachFileName[-5:] != ".wiki":
            continue
        readFilePath = directory + eachFileName
        baseName = os.path.basename(readFilePath)[:-5]

        readObj = file(readFilePath, "r")
        fileContents = readObj.read()
        readObj.close()
        newFileName = dateAddedString(fileContents) + os.path.basename(readFilePath)[:-5] + ".md"
        newFilePath = directory + newFileName

        header = genHeader(baseName, fileContents)
        fileContents = doDeletions(fileContents)
        fileContents = changeHeaders(fileContents)
        fileContents = reformatLinks(fileContents)
        fileContents = changeURLs(fileContents, relativePath)
        fileContents = removeExtraneousLinks(fileContents)
        fileContents = reformatTables(fileContents)

        writeObj = file(newFilePath, "w")
        writeObj.write(header + fileContents)
        writeObj.close()
