import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class No_White_Space {
    public static ArrayList<String> Remove_White_Space() {
        ArrayList<String> FileLines = null;
        try {
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter the file name");
            String fileName = sc.nextLine();
            sc.close();
            BufferedReader myReader = new BufferedReader(new FileReader(fileName));
            String LineRead;
            FileLines = new ArrayList<>();
            while ((LineRead = myReader.readLine()) != null) {
                LineRead = LineRead.replaceAll(" ", "");
                if (!LineRead.isEmpty() && !LineRead.startsWith("//")) {
                    if (LineRead.contains("//")) {
                        LineRead = LineRead.substring(0, LineRead.indexOf("//"));
                    }
                    FileLines.add(LineRead);
                }
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return FileLines;
    }

    public static void main(String[] args) {
        try {
            BufferedWriter myWriter = new BufferedWriter(new FileWriter("NoWhiteSpace.asm"));
            ArrayList<String> ReadLines = Remove_White_Space();
            for (String line : ReadLines) {
                System.out.println(line);
                myWriter.write(line + '\n');
            }
            myWriter.close();
        } catch (Exception e) {
            e.printStackTrace();
        }


    }

}