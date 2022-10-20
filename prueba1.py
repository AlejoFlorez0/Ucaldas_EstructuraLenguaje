gramatica1=["E -> T E'", "E' -> + T E' | λ", "T -> F T'", "T' -> * F T' | λ", 'F -> ( E ) | id']


# Lista primeros
primeros1=[{'name': 'E', 'firsts': "['(', 'id']"}, 
{'name': "E'", 'firsts': "['+', 'λ']"}, 
{'name': 'T', 'firsts': "['(', 'id']"}, 
{'name': "T'", 'firsts': "['*', 'λ']"}, 
{'name': 'F', 'firsts': "['(', 'id']"}]

# Lista Siguiente
siguientes1=[{'name': 'E', 'follows': "['(', 'id']"}, 
{'name': "E'", 'follows': "['+', 'λ']"}, 
{'name': 'T', 'follows': "['(', 'id']"}, 
{'name': "T'", 'follows': "['*', 'λ']"}, 
{'name': 'F', 'follows': "['(', 'id']"}]

def predictionSet(gramm,firsts,follows):

    predSet=[]
    for prod in gramm:
        coleccs = prod.split(" ")
        name=coleccs[0]
        
        for i in range(2,len(coleccs)):

            if i==2:

                if (coleccs[i]=='λ'):
                    for sig in follows:
                        if sig['name']==name:
                            predSet.append({
                            'name':name,
                            'predictionSet':sig['follows']    
                            })
                elif coleccs[i].isupper():
                    for prim in firsts:
                        if prim['name']==coleccs[i]:
                            predSet.append({
                            'name':name,
                            'predictionSet':prim['firsts']    
                            })
                            
                            print(f"para el sin | camino NO TERMINAL {predSet}")
                            #print(f"la grama {prod} // {coleccs[i]} prim {prim['name']}")
                elif not(coleccs[i].isupper()):
                    
                    predSet.append({
                            'name':name,
                            'predictionSet': [coleccs[i]] 
                            })

               
            elif coleccs[i]=='|':
                if (coleccs[i]!='λ'):
                    for sig in follows:
                        if sig['name']==name:
                            predSet.append({
                            'name':name,
                            'predictionSet':sig['follows']    
                            })
                elif coleccs[i+1].isupper():
                    for prim in firsts:
                        if prim['name']==coleccs[i+1]:
                            predSet.append({
                            'name':name,
                            'predictionSet':prim['firsts']    
                            })
                elif not(coleccs[i+1].isupper()):
                    predSet.append({
                            'name':name,
                            'predictionSet': [coleccs[i+1]] 
                            })
                break       
                         
    return predSet

def isll1(predictionList):
    result=[]
    for pred in predictionList:
        cont=0
        for pred1 in predictionList:
            if pred['name']==pred1['name']:
                if pred['predictionSet']==pred1['predictionSet']:
                    cont=1
        result.append(cont)
    for x in result:
        if x!=0:
            print("La gramatica no es LL1")
            break
        else:
            print("La gramatica es LL1")
preset=predictionSet(gramatica1,primeros1,siguientes1)
isll1(preset)
