#https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

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
     * Complete the 'timeConversion' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static string timeConversion(string s)
    {
        String hour = s.Substring(0,2);
        String suffix = s.Substring(8,2);

        if(hour.Equals("12") && suffix.Equals("PM")) {
            return s.Substring(0,8);
        }
        else if(hour.Equals("12") && suffix.Equals("AM")) {
            return "00" + s.Substring(2,6);
        }
        
        else if(s.EndsWith("PM")) {
            hour = (int.Parse(s.Substring(0,2)) + 12).ToString();
        }
        
        var rest = s.Substring(2,6);
        
        return String.Format("{0}{1}", hour, rest);

    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string s = Console.ReadLine();

        string result = Result.timeConversion(s);

        textWriter.WriteLine(result);

        textWriter.Flush();
        textWriter.Close();
    }
}
