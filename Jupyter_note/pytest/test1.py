

from owlready2 import *
import types

onto = get_ontology("ai201.owl").load()

with onto:
    class A (Thing):
        pass

x = ['abs', 'acs', 'ads']

for yb in x:
    with onto:
        NewClass = types.new_class(yb, (Thing,))
    # class yb (Thing):
    #     namespace = onto

#sync_reasoner()
onto.save(file = 'matcal.owl', format = 'rdfxml')

