# 1. Adding an element to the Linked List.
#Start by creating a new method in our LinkedList class called "add_list_elements".
#This method should take in a list as an argument.
#Loop through each element in the list and convert it to a node.
#Add each node to the end of the linked list using the "add_node" method we already have in the class.

from Node import Node

class LinkedList:
    
    def __init__(self):
        self.head = None

    def add_node(self, value):
        node = Node(value)
        if not self.head:
          self.head = node
        else:
          current_node = self.head
          while current_node.right:
              previous_node = current_node
              current_node = current_node.right
              current_node.left = previous_node
          current_node.right = node

    def __iter__(self):
       current_node = self.head
       while current_node:
          yield current_node
          current_node = current_node.right

    def __repr__(self):
      return ' -> '.join(node.value for node in self)
      # nodes = []
      # for node in self:
      #   nodes.append(node.value)
      # return ' -> '.join(nodes)

    def insert_node(self, target, value):
       new_node = Node(value)
       if self.head:
          for node in self:
             if node.value == target:
                right_node = node.right
                node.right = new_node
                new_node.right = right_node
       else:
          print('Empty List')

    def remove_node(self, value):
        if value == self.head.value:
           self.head = self.head.right
        else:
           for node in self:
              if node.right:
                if node.right.value == value:
                  node.right = node.right.right
                  return
                
    def get_tail(self):
      #  for node in self:
      #     pass
      #  return node.value
      node = self.head
      while node.right:
         node = node.right
      return node.value

    def remove_tail(self):
      node = self.head
      if node.right:
        while node.right.right:
          node = node.right
        node.right = None

    def add_list_elements(self, list):
       for item in list:
          if list in list:
             self.add_node(item)
       return self.head

linked_list = LinkedList()
elements = [1,2,3,4,5]

linked_list.add_list_elements(elements)

print(linked_list)

# 2. Updating Pokemon
#Add a new attribute to our Pokemon class called "evolve_chain".
#This should be initialized as an empty LinkedList.
#Create a new method in our Pokemon class called "add_evolve_chain" and adds each pokemon to the "evolve_chain" linked list.
#This will be a new version of "evolve_pokemon" method.
#Updates to old method
#In the "add_evolve_chain" method, we need to take the current Pokemon and add it to the "evolve_chain" linked list using the "add_node" method we created earlier.
#Remove the "call_poke_api" call since we no longer need  to update our pokemon. Instead, we can use the "add_evolve_chain" method to add the evolution chain for a particular Pokemon.
#Finally, when we reach the last Pokemon in the chain, make sure to add it to the "evolve_chain" linked list before returning.

from requests import get
from LinkedList import LinkedList, Node

class Pokemon():
    
    def __init__(self, name):
        self.name = name
        self.abilities = []
        self.types = []
        self.weight = None
        self.image = None
        self.pokes = []
        self.evolve_chain = LinkedList        
            
    def get_evolution_chain(self):
        response = get(self.species_url)
        if response.status_code == 200:
            data = response.json()
        evolution_chain_url = data['evolution_chain']['url']
        evolution_chain = get(evolution_chain_url)
        if evolution_chain.status_code == 200:
            return evolution_chain.json()['chain']

    def add_evolve_chain(self, current_pokemon, evolution_chain):
        node = Node(current_pokemon)
        self.evolve_chain.add_node(node)
        if not evolution_chain['evolves_to']:
            print(f'This is the final form')
            return
        self.add_evolve_chain(evolution_chain['species']['name'], evolution_chain['evolves_to'][0])

    def evolve_pokemon(self, evolution_chain):
        if not evolution_chain['evolves_to']:
            print(f'This is the final from')
            return
        current_pokemon_in_chain = evolution_chain['species']['name']
        if current_pokemon_in_chain == self.name:
            self.add_evolve_chain(current_pokemon_in_chain, evolution_chain)
            self.evolve_pokemon(evolution_chain['evolves_to'][0])
            return
        else:
            return self.evolve_pokemon(evolution_chain['evolves_to'][0])
          
  cyndaquil = Pokemon("Cyndaquil", ["Fire"])
  typholosion = cyndaquil.evolve_pokemon()
  evolve_chain = cyndaquil.evolve_chain
  print(evolve_chain)
