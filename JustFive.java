public class JustFive {
    private static int instanceCount = 0;
    
    
    private JustFive() throws InstantiationException{
    	if(instanceCount < 5){
            instanceCount++;
        }else{
            throw new InstantiationException();
        }
    }
    
    public static void main(String[] args) throws InstantiationException{
    	
    	JustFive one = new JustFive();
    	JustFive two = new JustFive();
    	JustFive three = new JustFive();
    	JustFive four = new JustFive();
    	JustFive five = new JustFive();
    	JustFive six = new JustFive();
    }
   
}
