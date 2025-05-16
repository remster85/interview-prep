#https://www.hackerrank.com/challenges/magic-square-forming/problem

using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'formingMagicSquare' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY s as parameter.
     */

  // Method to generate permutations of a list
    public static IEnumerable<IEnumerable<T>> GetPermutations<T>(IEnumerable<T> list, int length)
    {
        if (length == 1) return list.Select(t => new T[] { t });

        return GetPermutations(list, length - 1)
            .SelectMany(t => list.Where(e => !t.Contains(e)),
                        (t1, t2) => t1.Concat(new T[] { t2 }));
    }

    // Method to form a 3x3 matrix from a permutation
    public static int[,] FormMatrix(IEnumerable<int> perm)
    {
        var matrix = new int[3, 3];
        var enumerator = perm.GetEnumerator();
        
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                enumerator.MoveNext();
                matrix[i, j] = enumerator.Current;
            }
        }
        return matrix;
    }
    
    public static Boolean isValidMatrix(int[,] matrix){
        
        int sumDiagonalLR = 0;
        int sumDiagonalRL = 0;
        for(int i=0; i<=2; i++){
            int sumRow = 0;
            int sumColumn = 0;
            sumDiagonalLR += matrix[i,i]; 
            sumDiagonalRL += matrix[2-i,i]; 
            for(int j=0; j<=2; j++){
                   sumRow+= matrix[i,j];     
                   sumColumn+= matrix[j,i];     
            }    
            if(sumRow != 15 || sumColumn != 15) return false;
        }
        if(sumDiagonalLR != 15 || sumDiagonalRL != 15) return false;
        return true;
    }

    public static int calculateCost(int[,] validMatrix, List<List<int>> ourMatrix){
        int cost = 0;
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                cost += Math.Abs(validMatrix[i,j] - ourMatrix[i][j]);
            }    
        }    
    
        return cost;
    

    }
    
    
    public static int formingMagicSquare(List<List<int>> s)
    {
        int magicSquareValue = 15;
        
                // List of distinct values between 1 and 9
        var values = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9 };

        // Generate all permutations
        var permutations = GetPermutations(values, values.Count);

        List< int[,]> validMatrices = new List<int[,]>();
    
        // Loop through each permutation and form a 3x3 matrix
        foreach (var perm in permutations)
        {
            var matrix = FormMatrix(perm);
            if(isValidMatrix(matrix)) validMatrices.Add(matrix);
        }
        
        Console.Write($"{validMatrices.Count()} valid matrices");
        
        int minCost = int.MaxValue;
        
        foreach(int[,] validmatrix in validMatrices){
            minCost = Math.Min(calculateCost(validmatrix, s ), minCost);
        }
        
        return minCost;
        

    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        List<List<int>> s = new List<List<int>>();

        for (int i = 0; i < 3; i++)
        {
            s.Add(Console.ReadLine().TrimEnd().Split(' ').ToList().Select(sTemp => Convert.ToInt32(sTemp)).ToList());
        }

        int result = Result.formingMagicSquare(s);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
