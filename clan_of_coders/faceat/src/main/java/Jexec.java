/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author nageen
 */
import java.io.*;

class Jexec{
    public void Jexec(){}

    String exec(String execStr){
    try{
        // run process and capture stdout
        Process p = Runtime.getRuntime().exec(execStr);
        InputStream s = p.getInputStream();

        // convert stdout to a string
        BufferedReader br = new BufferedReader(new InputStreamReader(s));  
        StringBuffer sb = new StringBuffer(); 
        String line;  
        while ((line = br.readLine()) != null) {  
        sb.append(line).append("\n");  
        }  
        String output = sb.toString();  

        p.destroy();
        return output.toString();

    }catch(Exception e){
        //actually handle the error here
        e.printStackTrace();
        return String.format("*** Running \"%s\" failed. ***",execStr);
    }
    }
}