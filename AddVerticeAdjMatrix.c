#include <stdio.h>

void printNewMatrix(int adjMatrix[10][10], int *numVertices) {
    for (int i = 0; i < *numVertices; i++) {
        for (int j = 0; j < *numVertices; j++) {
            printf("%d ", adjMatrix[i][j]);
        }
        printf("\n");
    }
}


void addVertice(int adjMatrix[10][10], int *numVertices) {
    int i;
    for (i = 0; i < *numVertices; i++) {
        adjMatrix[i][*numVertices] = 0;
        adjMatrix[*numVertices][i] = 0;
    }
    (*numVertices)++;

    // Print the new matrix
    for (i = 0; i < *numVertices; i++) {
        for (int j = 0; j < *numVertices; j++) {
            printf("%d ", adjMatrix[i][j]);
        }
        printf("\n");
    }
}

void removeVertice(int adjMatrix[10][10], int *numVertices, int vertice) {
    if (vertice >= *numVertices || vertice < 0) {
        printf("Invalid vertex number.\n");
        return;
    }

    for (int i = vertice; i < *numVertices - 1; i++) {
        for (int j = 0; j < *numVertices; j++) {
            adjMatrix[i][j] = adjMatrix[i + 1][j];
        }
    }

    for (int i = vertice; i < *numVertices - 1; i++) {
        for (int j = 0; j < *numVertices; j++) {
            adjMatrix[j][i] = adjMatrix[j][i + 1];
        }
    }

    (*numVertices)--;

    // Print the new matrix
    for (int i = 0; i < *numVertices; i++) {
        for (int j = 0; j < *numVertices; j++) {
            printf("%d ", adjMatrix[i][j]);
        }
        printf("\n");
    }

}

void addEdge(int adjMatrix[10][10], int *numVertices, int vertice1, int vertice2) {
    adjMatrix[vertice1][vertice2] = 1;
    adjMatrix[vertice2][vertice1] = 1;

    for (int i = 0; i < *numVertices; i++) {
        for (int j = 0; j < *numVertices; j++) {
            printf("%d ", adjMatrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int adjMatrix[10][10] = {
        {0, 1, 0, 0, 0},
        {1, 0, 1, 1, 0},
        {0, 1, 0, 0, 0},
        {0, 1, 0, 0, 1},
        {0, 0, 0, 1, 0}
    };
    int numVertices = 5; // Initial number of vertices

    printf("Original matrix:\n");
    for (int i = 0; i < numVertices; i++) {
        for (int j = 0; j < numVertices; j++) {
            printf("%d ", adjMatrix[i][j]);
        }
        printf("\n");
    }

    printf("\nAdding a new vertex:\n");
    addVertice(adjMatrix, &numVertices);

    printf("\nRemoving vertex 2:\n");
    removeVertice(adjMatrix, &numVertices, 2);

    printf("\nAdd edge 4,3:\n");
    addEdge(adjMatrix, &numVertices, 4, 3);

    return 0;
}
