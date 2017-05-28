//http://pt.wikihow.com/Criar-um-Programa-Simples-em-C%2B%2B
#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;
int size, ope, num;
int binary_search(int *matrix, int init, int end, int num, int result)
{
    int mid = (init + end) / 2;
    
    if (init > end){
        return result;
    } else if (matrix[mid] == num ){
        result = mid;
        return binary_search(matrix, init, mid -1, num, result);
    } else if (matrix[mid] > num) {
        return binary_search(matrix, init, mid -1, num, result);
    } else {
        return binary_search(matrix, mid + 1, end, num, result);
    }
}

int main ()
{
    scanf("%d %d", &size, &ope);
    int array[size];
    for (int i = 0; i < size; i++){
        scanf("%d", &array[i]);
    }
    
    for (int i = 0; i < ope; i++){
        scanf("%d", &num);
        printf("%d\n", binary_search(array, 0, size - 1, num, -1));
    }
  
}

 
