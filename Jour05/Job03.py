# fonction qui dessine un tapis
def tapisserie(n): 
	print("+" + "-" * (n+1) + "+") # dessine le haut du tapis
	for i in range(n+1): # pour chaque élément i de la liste L
		print("|" + "#" * (n-i) + " " + "#" * i + "|") # dessine les lignes intérieures du tapis
	print("+" + "-" * (n+1) + "+") # dessine le bas du tapis
  
tapisserie(10)