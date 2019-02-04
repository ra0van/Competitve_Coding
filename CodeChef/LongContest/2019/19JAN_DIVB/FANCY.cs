using System;

public class Test
{
	public static void Main()
	{
	    int t = Convert.ToInt32(Console.ReadLine());
	    for(int i =0; i<t; i++){
	        string input = Console.ReadLine().ToLower();
	        string [] array = input.Split(' ');
	        bool flag = true;
	        foreach(var str in array){
	            if (str == "not"){
	                flag = false;
	                break;
	            }
	        }
	        string result = flag ? "regularly fancy" : "Real Fancy";
	        Console.WriteLine(result);
	    }
	}
}
