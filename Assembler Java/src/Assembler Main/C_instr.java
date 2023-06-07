import java.util.ArrayList;
import java.util.HashMap;

public class C_instr {
    public static final HashMap<String, String> dest_value = new HashMap<>();
    public static final HashMap<String, String> jump_value = new HashMap<>();
    public static final HashMap<String, String> compValueMap0 = new HashMap<>();
    public static final HashMap<String, String> compValueMap1 = new HashMap<>();

    static {

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
    public static String convertor(String dest,String comp,String jump){
        String binary = "111";
        if (compValueMap0.containsKey(comp))
        {
            binary += "0"+compValueMap0.get(comp);
        }
        else
        {
            binary += "1"+compValueMap1.get(comp);
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
    public static String C_instruction(String line, ArrayList<String> FileLines) {

        String equalSpace = line.replace("=", " ");
        String semiColonSpace = equalSpace.replace(";", " ");
        String[] instr = semiColonSpace.split(" ");
        String dest = "0";
        String comp = "0";
        String jump = "0";
        if (instr.length == 3) {
            dest = instr[0];
            comp = instr[1];
            jump = instr[2];
        } else if (instr.length == 2) {
            if (line.contains("=")) {
                dest = instr[0];
                comp = instr[1];
            } else {
                comp = instr[0];
                jump = instr[1];
            }
        } else {
            comp = instr[0];
        }
        String Binary = convertor(dest, comp, jump);
        return Binary;

    }
}
