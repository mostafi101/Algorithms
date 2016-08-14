/*
 * Write a recursive static Java method that accepts an array arr of integers argument returns a list of all permutations of these integers.

(A permutation of a sequence of integers is a re-arrangement of the integers. For example, one permutation of  1, 3, 4, 8, 2 is 3, 1, 2, 8, 4.) For this problem, you may assume that the input array contains no duplicate entries. Your method should return an ArrayList of int arrays.

Next, test your method using a main method; the main method should pass in the following array: [1, 5, 4, 2]; then, it should print to the console the resulting list of permutations.*/
import java.util.*;

public class Permutation{
	
	private int[] arrIdxs;
	private ArrayList<Integer> arr;
	public ArrayList<Integer> get_next()
	{
		ArrayList<Integer> ret = new ArrayList<Integer>();
		for (int idx = 0 ; idx < arrIdxs.length;idx++)
			ret.add(idx,arr.get(arrIdxs[idx])); 
		return ret;
	}
	public Permutation(ArrayList<Integer> arr)
	{
		this.arr = new ArrayList<Integer>();
		for (int each:arr)
			this.arr.add(each);
		arrIdxs = new int[arr.size()];
		for(int i = 0 ; i < arr.size();i++) 	
			this.arrIdxs[i]= i;
	}
	
	public boolean next_permutation()
	{
		int i,j,l;

		for(j =arr.size() -2 ;j >=0  ; j--) 
			if (arrIdxs[j+1] > arrIdxs[j])
				break;
		if (j == -1)  
			return false;

		for(l = arr.size()-1;l > j ; l--) 
			if (arrIdxs[l] > arrIdxs[j])
				break;
		
		int swap = arrIdxs[j]; 
		arrIdxs[j] = arrIdxs[l];
		arrIdxs[l] = swap;

		for (i = j+1;i < arrIdxs.length;i++) 
		{
			if (i > arrIdxs.length - i + j )
				break;
			swap = arrIdxs[i];
			arrIdxs[i] = arrIdxs[arrIdxs.length - i + j];
			arrIdxs[arrIdxs.length - i + j] = swap;
		}

		return true;
	}    

	
	
}
