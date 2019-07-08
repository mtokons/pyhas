

from owlready2 import *
import types

onto = get_ontology("ai201.owl").load()


with onto:
    class IngredientTest (Thing):
        pass

#sync_reasoner()
onto.save(file = 'matcal.owl', format = 'rdfxml')

