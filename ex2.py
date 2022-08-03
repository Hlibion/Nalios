import numpy as np


def sum_neighbors(mat, coord):
    coordx, coordy = coord
    shapex = mat.shape[0]-1
    shapey = mat.shape[1]-1
    neighbors = []
    if coordx==0 and coordy==0:
        neighbors.append(mat[coordx+1][coordy])
        neighbors.append(mat[coordx+1][coordy+1])
        neighbors.append(mat[coordx][coordy+1])
    elif coordx==0 and coordy==shapey:
        neighbors.append(mat[coordx+1][coordy])
        neighbors.append(mat[coordx+1][coordy-1])
        neighbors.append(mat[coordx][coordy-1])
    elif coordx==shapex and coordy==0:
        neighbors.append(mat[coordx-1][coordy])
        neighbors.append(mat[coordx-1][coordy+1])
        neighbors.append(mat[coordx-1][coordy])
    elif coordx==shapex and coordy==shapey:
        neighbors.append(mat[coordx-1][coordy])
        neighbors.append(mat[coordx-1][coordy-1])
        neighbors.append(mat[coordx][coordy-1])
    elif coordx==0 and 0<coordy<shapey :
        neighbors.append(mat[coordx][coordy-1])
        neighbors.append(mat[coordx][coordy+1])
        neighbors.append(mat[coordx+1][coordy-1])
        neighbors.append(mat[coordx+1][coordy])
        neighbors.append(mat[coordx+1][coordy+1])
    elif coordx==shapex and 0<coordy<shapey:
        neighbors.append(mat[coordx][coordy-1])
        neighbors.append(mat[coordx][coordy+1])
        neighbors.append(mat[coordx-1][coordy-1])
        neighbors.append(mat[coordx-1][coordy])
        neighbors.append(mat[coordx-1][coordy+1])
    elif 0<coordx<shapex and coordy==0:
        neighbors.append(mat[coordx-1][coordy])
        neighbors.append(mat[coordx+1][coordy])
        neighbors.append(mat[coordx-1][coordy+1])
        neighbors.append(mat[coordx][coordy+1])
        neighbors.append(mat[coordx+1][coordy+1])
    elif 0<coordx<shapex and coordy==shapey:
        neighbors.append(mat[coordx-1][coordy])
        neighbors.append(mat[coordx+1][coordy])
        neighbors.append(mat[coordx-1][coordy-1])
        neighbors.append(mat[coordx][coordy-1])
        neighbors.append(mat[coordx+1][coordy-1])
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
    return np.sum(neighbors)

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

def game_of_life_n_it(n_it, mat):
    for i in range(n_it):
        mat = game_of_life(mat)
    return mat
