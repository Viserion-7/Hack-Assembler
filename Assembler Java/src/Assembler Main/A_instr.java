import java.util.ArrayList;
import java.util.HashMap;

public class A_instr {
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

    public static String A_instruction(String ToConvert, ArrayList<String> FileLines,Counter counter) {
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
        if (ToConvert.startsWith("@")) {
            String symbol = ToConvert.substring(1);
            if (SymbolTable.containsKey(symbol)) {
                ToConvert = SymbolTable.get(symbol);
            } else if (symbol.matches("\\d+")) {
                ToConvert = symbol;
            } else {
                counter.increment();
                SymbolTable.put(symbol, Integer.toString(counter.getValue()));
                ToConvert = Integer.toString(counter.getValue());
            }
        }
        String Binary = Integer.toBinaryString(Integer.parseInt(ToConvert));
        Binary = String.format("%16s", Binary).replace(' ', '0');

        return Binary;
    }
}