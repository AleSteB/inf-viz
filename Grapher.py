# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:16:29 2024

@author: smaxbehr
"""

#pip install markdown
#pip install md-mermaid
# import subprocess
#https://github.com/floresbakker/OntoMermaid


"""
from python_mermaid.diagram import (
    MermaidDiagram,
    Node,
    Link
)

# Family members
meg = Node("Meg")
jo = Node("Jo")
beth = Node("Beth")
amy = Node("Amy")
robert = Node("Robert March")

the_march_family = [meg, jo, beth, amy, robert]

# Create links
family_links = [
    Link(robert, meg),
    Link(robert, jo),
    Link(robert, beth),
    Link(robert, amy),
]

chart = MermaidDiagram(
    title="Little Women",
    nodes=the_march_family,
    links=family_links
)

print(chart)
with open('mermaid.mmd',"w") as file:
    file.write(chart.string)

subprocess.run("mdpdf -o article.pdf README.md")
"""


from owlready2 import *

onto = get_ontology("reac4cat_with_examples.owl").load()

with onto:
    sync_reasoner(infer_property_values = True)
    onto.save("reac4cat_with_examples_inferred2.owl")

#onto2 = get_ontology("reac4cat_with_examples_inferred2.owl").load()

indv = onto.search_one(label = "Reaction_1")

mermaid_str = '```mermaid\n graph TD;\n'

def triple_to_mermaid(indv, mermaid_str):
   
    for prop in list(indv.get_properties()):
        if type(prop) == owlready2.prop.ObjectPropertyClass:
            pred_list = eval("indv.{}".format(prop.name))

            for obj in pred_list:
                add_str = "{}--{}-->{}\n".format(indv.label.first(),prop.label.first(),obj.label.first())
                mermaid_str += add_str
    return mermaid_str

mermaid_str = triple_to_mermaid(indv, mermaid_str)

for prop in list(indv.get_properties()):
    if type(prop) == owlready2.prop.ObjectPropertyClass:
        pred_list = eval("indv.{}".format(prop.name))
        for obj in pred_list:
            mermaid_str = triple_to_mermaid(obj, mermaid_str)

mermaid_str +='```'
with open('mermaid.md',"w") as file:
    file.write(mermaid_str)





