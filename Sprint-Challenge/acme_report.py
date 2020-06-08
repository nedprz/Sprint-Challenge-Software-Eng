

from acme import Product
from random import randint
from random import uniform
from random import sample
import numpy as np

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']






def generate_products(num=30):
    l = []
    for x in range (0,num):
        l.append(Product(name = f'{sample(ADJECTIVES, 1)[0]} {sample(NOUNS,1)[0]}', price = randint(5,100) , weight =randint(5,100) , flammability = uniform(0,2.5)))
    return l

def inventory_report(l):
    price_total = 0
    weight_total = 0
    flammability_total = 0
    names = []
    for x in range (0,len(l)):
        price_total += l[x].price
        weight_total += l[x].weight
        flammability_total += l[x].flammability
        names.append(l[x].name)
    price_avg=int(price_total/len(l))
    weight_avg = weight_total/len(l)
    flammability_avg = flammability_total/len(l)

    #return "price average: "+ price_avg + "weight average: " + weight_avg + "flammability average: " + flammability_avg
    return f"Average Price: {price_avg} | Average Weight: {weight_avg} | Average Flammability: {flammability_avg}  | unique: {len(np.unique(names))} | count: {len(l)}"

if __name__ == '__main__':
    inventory_report(generate_products())