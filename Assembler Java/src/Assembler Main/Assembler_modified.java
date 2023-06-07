import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.ArrayList;

public class Assembler_modified {

    public static void main(String[] args) {
        try {
            BufferedWriter myWriter = new BufferedWriter(new FileWriter("out.hack"));
            ArrayList<String> FileLines = No_White_Space.Remove_White_Space();
            String instr;
            Counter VariableNum = new Counter(15);
            for (String line : FileLines){
                if ((line.startsWith("@"))||(line.startsWith("("))){
                    if (line.startsWith("@")) {

                        instr = A_instr.A_instruction(line, FileLines, VariableNum);
                    }
                    else{
                        continue;
                    }
                }
                else{
                    instr = C_instr.C_instruction(line, FileLines);
                }
                System.out.println(instr);
                myWriter.write(instr+ '\n');
            }
            myWriter.close();
        }catch (Exception e){
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}