#ich glaube der import ist das einzig wichtige aus dem script hier
#weil man mit dem in ubuntu befehle ausfuehren kann
import os

n = raw_input("How many pdbs? ")
comp = "complexes/2.pdb" #raw_input("Please enter Address to Reference Complex? ")
Chain = raw_input("Please enter Name of the bigger chain? ")
n = int(n) 

for a in xrange(0,n) :
    ref = ""
    address = "./2pdb/"
    address += str(a);
    address += ".pdb";
    #building the command argument
    ref += "./build/tools/rmsd "
    ref += comp
    ref += " "
    ref += address
    ref += " "
    ref += Chain
    #befehl ausführen
    os.system(ref)
