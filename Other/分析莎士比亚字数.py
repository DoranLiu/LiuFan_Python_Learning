#!/usr/bin/python
# coding: utf-8
from pyspark import SparkContext, SparkConf
from operator import add
appName = "WordCount"
conf = SparkConf().setAppName(appName).setMaster("local")
sc = SparkContext(conf=conf)
# inputFiles表示输入文件
inputFiles = "/home/wordcount/shakespear/*"
stopWordFile = "/home/wordcount/stopword.txt"
outputFile = "/tmp/resultRDD"

targetList = list('\t\().,?[]!;|') + ['--']

def replaceAndSplit(s):
    for c in targetList:
        s = s.replace(c, " ")
    return s.split()

inputRDD = sc.textFile(inputFiles)
stopRDD = sc.textFile(stopWordFile)
stopList = stopRDD.map(lambda x: x.strip()).collect()

inputRDDv1 = inputRDD.flatMap(replaceAndSplit)
inputRDDv1.saveAsTextFile('/home/wordcount/outputRDD1')
inputRDDv2 = inputRDDv1.filter(lambda x: x not in stopList)
inputRDDv2.saveAsTextFile('/home/wordcount/outputRDD2')
inputRDDv3 = inputRDDv2.map(lambda x: (x,1))
inputRDDv3.saveAsTextFile('/home/wordcount/outputRDD3')
inputRDDv4 = inputRDDv3.reduceByKey(add)
inputRDDv4.saveAsTextFile('/home/wordcount/outputRDD4')
inputRDDv5 = inputRDDv4.map(lambda x: (x[1], x[0]))
inputRDDv5.saveAsTextFile('/home/wordcount/outputRDD5')
inputRDDv6 = inputRDDv5.sortByKey(ascending=False)
inputRDDv6.saveAsTextFile('/home/wordcount/outputRDD6')
inputRDDv7 = inputRDDv6.map(lambda x: (x[1], x[0])).keys()
inputRDDv7.saveAsTextFile('/home/wordcount/outputRDD7')
top100 = inputRDDv7.take(100)
result = sc.parallelize(top100)
result.saveAsTextFile(outputFile)