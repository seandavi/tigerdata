#!/usr/bin/env python3
import csv

outfile = open('signatures_fixed.csv','w')
writer = csv.writer(outfile)
with open('signatures.csv') as f:
     reader = csv.DictReader(f)
     for row in reader:
         for s1 in row['NCBI Taxonomy IDs'].split(','):
             s2 = s1.split('|')
             if(len(s2)>0):
                 writer.writerow([
                     row['Signature page name'],
                     row['Experiment'],
                     row['Source'],
                     row['Description'],
                     row['Abundance in Group 1'],
                     s2[-1]])
outfile.close()
