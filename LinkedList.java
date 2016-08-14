/*
 * Create your own linked list (do not use any of the classes provided in the Collections API). Implement the following two operations:

If you are using jdk1.4 or before:

     void add(Object ob); 

     boolean find(Object ob);

     String toString();

If you are using j2se5.0 and you know generic programming:

     void add(T ob);

     boolean find(T ob);

     String toString()

The toString method should arrange the elements of the list in a comma-separated sequence, in the following format:

[elem0, elem1, elem2, …, elemN]

Test your linked list in a main method which does the following:

a. Creates an instance of your list and adds the following Strings to it:

“Straight”, “Bent”, “Equals”, “Well”, “Storm”

b. Uses your find function to search for the keys “Well” and “Strength”

c. Outputs both the input list and the search results to the consoleand output the results to the consoleby repeatedly using your add function to populate a new instance of your linked list with Strings, and then outputting to console the boolean result of searching for some String in this list.*/
class LinkedList<T>{
	//Class variables for the Linked List
	private Node head;
	private int numNodes;
	
	
	/*public LinkedList(T ob){
		head = new Node(ob);
	}*/
	
	public void add(T ob){
		Node temp = head;
		head = new Node(ob);
		head.next = temp;
	}
	
	public boolean find(T ob){
		Node current = head;
		while(current!=null){
	         if(current.data.equals(ob))
	        	 return true;
	         current = current.next;
	    }
		return false;
		
	}
	
	@Override public String toString(){
		Node current = head;
		String temp = "";
		while(current != null){
			temp = temp+current.data+",";
			current = current.next;
		}
		temp = temp.substring(0, temp.length()-1);
		return temp;
		
	}
		
	public void printList()
	{
		Node temp = head;
		while(temp != null)
		{
			System.out.println(temp.data);
			temp = temp.next;
		}
	}
	
	
	
	
	
	public int getSize()
	{
		return numNodes;
	}
	
	class Node
	{
		//Declare class variables
		Node next;
		T data;
		
		Node(T dat)
		{
			data = dat;
		}
	}
	
	
}
