import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.List;
import java.util.ArrayList;

public class Recognise_Symbols {
    public static void main(String[] args) {
        List<String> SymbolsAndVariables = new ArrayList<>();
        try {
            ArrayList<String> FileLines = No_White_Space.Remove_White_Space();
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

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}