#-------------------------------------------------------------------------------
# Purpose:       parsing data from a txt file having a form of:
#                author1 mentioned1,mentioned2,... timestamp text \n
#                to a form:
#                author1 mentioned1 timestamp\n
#                author1 mentioned2 timestamp\n
#                thus creating a single file without the text content in order to render
#                the matlab functions more efficient.
# Required libs: python-dateutil
# Author:        konkonst
#
# Created:       31/05/2013
# Copyright:     (c) ITI (CERTH) 2013
# Licence:       <apache licence 2.0>
#-------------------------------------------------------------------------------
import os,glob
import dateutil.parser
import time

# User sets json dataset and target folder
dataset_path = "E:/konkonst/retriever/crawler_temp"

if not os.path.exists(dataset_path+"/new"):
    os.makedirs(dataset_path+"/new")
#Parsing commences
my_txt=open(dataset_path+"/new/authors_mentions_time.txt","w")
for filename in glob.glob(dataset_path+"/*.txt"):
    print(filename)
    with open(filename,'r') as f:
        for line in f:
            read_line = line.strip()
            splitLine=read_line.split("\t")
            dt=dateutil.parser.parse(splitLine[2],fuzzy="True")
            mytime=int(time.mktime(dt.timetuple()))
            for mentions in splitLine[1].split(","):
                my_txt.write(splitLine[0]+"\t"+mentions+"\t"+str(mytime)+"\n") #author singlemention time
my_txt.close()
