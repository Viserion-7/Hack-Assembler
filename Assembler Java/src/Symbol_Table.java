import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Map;
import java.util.LinkedHashMap;

public class Symbol_Table {
    public static final ArrayList<String> FileLines = No_White_Space.Remove_White_Space();
    public static final LinkedHashMap<String, String> SymbolTable = new LinkedHashMap<>();

    static {
        SymbolTable.put("R0", "0");
        SymbolTable.put("R1", "1");
        SymbolTable.put("R2", "2");
        SymbolTable.put("R3", "3");
        SymbolTable.put("R4", "4");
        SymbolTable.put("R5", "5");
        SymbolTable.put("R6", "6");
        SymbolTable.put("R7", "7");
        SymbolTable.put("R8", "8");
        SymbolTable.put("R9", "9");
        SymbolTable.put("R10", "10");
        SymbolTable.put("R11", "11");
        SymbolTable.put("R12", "12");
        SymbolTable.put("R13", "13");
        SymbolTable.put("R14", "14");
        SymbolTable.put("R15", "15");
        SymbolTable.put("SP", "0");
        SymbolTable.put("LCL", "1");
        SymbolTable.put("ARG", "2");
        SymbolTable.put("THIS", "3");
        SymbolTable.put("THAT", "4");
        SymbolTable.put("SCREEN", "16384");
        SymbolTable.put("KBD", "24576");
    }

    public static void main(String[] args) {
        try {
            int bitCount = 15;
            int lineNum = 0;
            for (String line : FileLines) {
                if (line.startsWith("(")) {
                    String symbol = line.substring(1, line.length() - 1);
                    SymbolTable.put(symbol, Integer.toString(lineNum));
                }
                else{
                    lineNum++;
                }
            }
            for (String line : FileLines) {
                if (line.startsWith("@")) {
                    String symbol = line.substring(1);
                    if (SymbolTable.containsKey(symbol)) {
                        // No action needed
                    }
                    else if (symbol.matches("\\d+")) {
                        // No action needed
                    }else {
                        bitCount++;
                        SymbolTable.put(symbol, Integer.toString(bitCount));
                    }
                }
            }

            BufferedWriter myWriter = new BufferedWriter(new FileWriter("SymbolTable.asm"));
            myWriter.write("Symbols \t Values\n");
            for (Map.Entry<String, String> entry : SymbolTable.entrySet()) {
                System.out.println(entry.getKey() + " " + entry.getValue());
                myWriter.write(String.format("%-15s %-15s%n", entry.getKey(), entry.getValue()));
            }
            myWriter.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
