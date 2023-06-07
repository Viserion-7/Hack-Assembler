import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.io.BufferedWriter;
import java.io.FileWriter;

public class A_Instruction {
    public static final ArrayList<String> FileLines = No_White_Space.Remove_White_Space();
    public static final HashMap<String, String> SymbolTable = new HashMap<>();

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
            List<String> Value_Table = new ArrayList<>();
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
                        Value_Table.add(SymbolTable.get(symbol));
                    } else if (symbol.matches("\\d+")) {
                        Value_Table.add(symbol);
                    } else {
                        bitCount++;
                        SymbolTable.put(symbol, Integer.toString(bitCount));
                        Value_Table.add(Integer.toString(bitCount));
                    }
                }
            }

            BufferedWriter myWriter = new BufferedWriter(new FileWriter("A_Instruction.asm"));
            for (String WriteValue  : Value_Table) {
                String Binary = Integer.toBinaryString(Integer.parseInt(WriteValue));
                Binary = String.format("%16s", Binary).replace(' ', '0');
                System.out.println(WriteValue);
                System.out.println(Binary);
                myWriter.write(Binary+'\n');
            }
            myWriter.close();

        }catch (Exception e) {
            e.printStackTrace();
        }
    }
}
