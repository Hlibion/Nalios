import numpy as np


def sum_neighbors(mat, coord):
    coordx, coordy = coord
    if coordx == 0 or coordx == mat.shape[0]-1 or coordy == 0 or coordy == mat.shape[1]-1:
        #gérer les extrémités de la matrice
        neighbors = []
        if coordx !=0 and coordy !=0:
            neighbors.append(mat[coordx-1][coordy-1])
            neighbors.append(mat[coordx-1][coordy])
            neighbors.append(mat[coordx][coordy-1])
        if coordx != mat.shape[0]-1 and coordy != mat.shape[1]-1:
            neighbors.append(mat[coordx+1][coordy+1])
            neighbors.append(mat[coordx+1][coordy])
            neighbors.append(mat[coordx][coordy+1])
        #to continue
            
    else :
        neighbors = [
            mat[coordx-1][coordy-1],
            mat[coordx-1][coordy],
            mat[coordx-1][coordy+1],
            mat[coordx][coordy-1],
            mat[coordx][coordy+1],
            mat[coordx+1][coordy-1],
            mat[coordx+1][coordy],
            mat[coordx+1][coordy+1],
            ]
            
    return sum(map(sum, neighbors))

def game_of_life(matrix_cell):
    x,y = matrix_cell.shape
    new_mat = np.zeros((x,y))
    for cx in range(x):
        for cy in range(y):
            statutCell = matrix_cell[cx,cy]
            #faire la somme des voisins qui sont allumé (=1)
            sn = sum_neighbors(matrix_cell, (cx,cy))
            #si (somme == 1 ou somme ==0) ET le statut de la cellule est 1 --> cellule s'éteint
            if (sn == 0 or sn == 1) and statutCell == 1:
                new_mat[cx,cy]=0
            #si somme >= 4 ET le statut de la cellule est 1 --> cellule s'éteint
            if sn >= 4 and statutCell == 1:
                new_mat[cx,cy]=0
            #si (somme == 2 ou somme == 3) ET le statut de la cellule est 1 --> cellule reste allumée
            if (sn == 2 or sn == 3) and statutCell == 1:
                new_mat[cx,cy]=1
            #si somme == 3 ET statut de la cellule est 0 --> cellule s'allume
            if sn == 3 and statutCell == 0:
                new_mat[cx,cy]=1
            
        
    return new_mat
