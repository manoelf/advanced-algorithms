#https://www.urionlinejudge.com.br/judge/en/problems/view/1049

subphylum = raw_input()
phylum = raw_input()
feeding = raw_input()

animals = {}
types = {}

types['carnivoro'] = 'aguia'
types['onivoro'] = 'pomba'
animals['ave'] = types

types = {}
types['onivoro'] = 'homem'
types['herbivoro'] = 'vaca'
animals['mamifero'] = types

types = {}
types['hematofago'] = 'pulga'
types['herbivoro'] = 'lagata'
animals['inseto'] = types

types = {}
types['onivoro'] = 'minhoca'
types['hematofago'] = 'sanguessuga'
animals['anelideo'] = types

print animals[phylum][feeding]

