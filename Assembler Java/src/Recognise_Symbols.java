import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class Recognise_Symbols {

    public static void main(String[] args) {
        List<String> SymbolsAndVariables = new ArrayList<>();
        try {
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter the file name");
            String fileName = sc.nextLine();
            sc.close();
            BufferedReader myReader = new BufferedReader(new FileReader(fileName));

            String LineRead;
            List<String> FileLines = new ArrayList<>();
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

            BufferedWriter myWriter = new BufferedWriter(new FileWriter("SymbolsAndVariables.asm"));
            for (String line : FileLines) {
                if (line.startsWith("@")) {
                    if (Character.isLetter(line.charAt(1))) {
                        if (!SymbolsAndVariables.contains(line.substring(1, line.length() - 1))) {
                            SymbolsAndVariables.add(line.substring(1, line.length() - 1));
                            System.out.println(line.substring(1));
                            myWriter.write(line.substring(1) + '\n');
                        }
                    }
                }
            }
            myWriter.close();

        } catch (FileNotFoundException e) {
            System.out.println("File not found");
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}