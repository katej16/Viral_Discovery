import pandas as pd
import numpy as np
import matplotlib as plt
import Bio
from Bio import Entrez
import xml.etree.ElementTree as ET

def get_tax(my_id):
    seq_handle =  Entrez.efetch(db='taxonomy', id=my_id, rettype="xml", retmode="text" )
    seq_contentsxml = seq_handle.read()
    seq_contentsxmlstr = str(seq_contentsxml)
    #print(seq_contentsxmlstr)
    xml_list = seq_contentsxmlstr.split('\\n')
    lineage = xml_list[16]
    lineage_lst = lineage.split(';')[1:7]
    lineage_title = ['Clade', 'Kingdom','Phylum','Class','Order','Family']
    zip_iterator = zip(lineage_lst, lineage_title)
    my_dict = dict(zip_iterator)
    return my_dict
