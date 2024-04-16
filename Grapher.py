# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:16:29 2024

@author: smaxbehr
"""

#pip install markdown
#pip install md-mermaid
# import subprocess
#https://github.com/floresbakker/OntoMermaid


from owlready2 import *


def triple_to_mermaid(indv, mermaid_str):
   
    for prop in list(indv.get_properties()):
        if type(prop) == owlready2.prop.ObjectPropertyClass:
            pred_list = eval("indv.{}".format(prop.name))

            for obj in pred_list:
                add_str = "{}--{}-->{}\n".format(indv.label.first(),prop.label.first(),obj.label.first())
                mermaid_str += add_str
    return mermaid_str

def md_from_onto_obj(indv, ontology_name):
    mermaid_str = '```mermaid\n graph TD;\n'
    
    mermaid_str = triple_to_mermaid(indv, mermaid_str)
    """
    for prop in list(indv.get_properties()):
        if type(prop) == owlready2.prop.ObjectPropertyClass:
            pred_list = eval("indv.{}".format(prop.name))
            for obj in pred_list:
                mermaid_str = triple_to_mermaid(obj, mermaid_str)
    """
    mermaid_str +='```'
    
    with open(ontology_name.replace(".owl",".md"),"w") as file:
        file.write(mermaid_str)


def onto_obj_to_md(ontology_name, obj_name):
    onto1 = owlready2.World()
    onto1 = get_ontology(ontology_name).load()
    indv1 = onto1.search_one(label = obj_name)
    md_from_onto_obj(indv1,ontology_name)


###################

ontology_name = "reac4cat_with_examples.owl"
ontology_name_inf = "reac4cat_with_examples_inferred.owl"

searched_name = "Reaction_1"

onto_obj_to_md(ontology_name,searched_name)
onto_obj_to_md(ontology_name_inf,searched_name)







