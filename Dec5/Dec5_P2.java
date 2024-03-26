import java.io.*;

public class Dec5_P2{
    public static void main(String[] args){
        FileInputStream fIn = null;
        try{
            fIn = new FileInputStream("testInput.txt");
            System.out.println(fIn.read());
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }

    }
}