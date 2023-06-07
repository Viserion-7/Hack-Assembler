import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.FileNotFoundException;

public class Assembler {
    public static final ArrayList<String> FileLines = No_White_Space.Remove_White_Space();
    public static final HashMap<String, String> SymbolTable = new HashMap<>();
    public static final HashMap<String, HashMap<String, String>> comp_value = new HashMap<>();
    public static final HashMap<String, String> dest_value = new HashMap<>();
    public static final HashMap<String, String> jump_value = new HashMap<>();
    public static final HashMap<String, String> compValueMap0 = new HashMap<>();
    public static final HashMap<String, String> compValueMap1 = new HashMap<>();

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

        compValueMap0.put("0", "101010");
        compValueMap0.put("1", "111111");
        compValueMap0.put("-1", "111010");
        compValueMap0.put("D", "001100");
        compValueMap0.put("A", "110000");
        compValueMap0.put("!D", "001101");
        compValueMap0.put("!A", "110001");
        compValueMap0.put("-D", "001111");
        compValueMap0.put("-A", "110011");
        compValueMap0.put("D+1", "011111");
        compValueMap0.put("A+1", "110111");
        compValueMap0.put("D-1", "001110");
        compValueMap0.put("A-1", "110010");
        compValueMap0.put("D+A", "000010");
        compValueMap0.put("D-A", "010011");
        compValueMap0.put("A-D", "000111");
        compValueMap0.put("D&A", "000000");
        compValueMap0.put("D|A", "010101");

        compValueMap1.put("M", "110000");
        compValueMap1.put("!M", "110001");
        compValueMap1.put("-M", "110011");
        compValueMap1.put("M+1", "110111");
        compValueMap1.put("M-1", "110010");
        compValueMap1.put("D+M", "000010");
        compValueMap1.put("D-M", "010011");
        compValueMap1.put("M-D", "000111");
        compValueMap1.put("D&M", "000000");
        compValueMap1.put("D|M", "010101");

        comp_value.put("0", compValueMap0);
        comp_value.put("1", compValueMap1);

        dest_value.put("0", "000");
        dest_value.put("M", "001");
        dest_value.put("D", "010");
        dest_value.put("MD", "011");
        dest_value.put("A", "100");
        dest_value.put("AM", "101");
        dest_value.put("AD", "110");
        dest_value.put("AMD", "111");

        jump_value.put("0", "000");
        jump_value.put("JGT", "001");
        jump_value.put("JEQ", "010");
        jump_value.put("JGE", "011");
        jump_value.put("JLT", "100");
        jump_value.put("JNE", "101");
        jump_value.put("JLE", "110");
        jump_value.put("JMP", "111");
    }

    public static String instruction(String dest,String comp,String jump){
        String binary = "111";
        if (comp_value.get("0").containsKey(comp))
        {
            binary += "0"+comp_value.get("0").get(comp);
        }
        else
        {
            binary += "1"+comp_value.get("1").get(comp);
        }

        if (!dest.equals("0"))
        {
            binary += dest_value.get(dest);
        }
        else
        {
            binary += "000";
        }

        if (!jump.equals("0"))
        {
            binary += jump_value.get(jump);
        }
        else
        {
            binary += "000";
        }
        return binary;
    }

    public static void main(String[] args) {
        System.out.println(" Started Assembler.java");
        try {
            BufferedWriter myWriter = new BufferedWriter(new FileWriter("out.hack"));
            List<String> Value_Table = new ArrayList<>();
            int bitCount = 15;
            int A_instr_counter = 0;
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
            String Binary;
            String WriteValue;
            for (String line : FileLines) {
                if ((line.startsWith("@"))||(line.startsWith("("))) {

                    // A instruction
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
                        WriteValue = Integer.toBinaryString(Integer.parseInt(Value_Table.get(A_instr_counter)));
                        Binary = String.format("%16s", WriteValue).replace(' ', '0');
                        A_instr_counter++;
                        System.out.println(Binary);
                        myWriter.write(Binary + "\n");
                    }

                // C-instruction
                } else {
                        String equalSpace = line.replace("=", " ");
                        String semiColonSpace = equalSpace.replace(";", " ");
                        String[] instr = semiColonSpace.split(" ");

                        if (instr.length == 3) {
                            Binary = instruction(instr[0], instr[1], instr[2]);
                        }
                        else if (instr.length == 2) {
                            if (line.contains("=")) {
                                Binary = instruction(instr[0], instr[1], "0");
                            }
                            else {
                                Binary = instruction("0", instr[0], instr[1]);
                            }
                        }
                        else {
                            Binary = instruction("0", instr[0], "0");
                        }
                        System.out.println(Binary);
                        myWriter.write(Binary + "\n");

                }
            }
            myWriter.close();
        }catch (FileNotFoundException e) {
            System.out.println("File not found");
            e.printStackTrace();
        }catch (Exception e) {
            e.printStackTrace();
        }
    }
}
