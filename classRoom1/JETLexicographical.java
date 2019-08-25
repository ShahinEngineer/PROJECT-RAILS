/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package jetlexicographical;

import java.util.Arrays;
import java.util.Scanner;

/**
 *
 * @author Mohammad Shahin
 */
public class JETLexicographical {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here

            System.out.println(biggerIsGrater("abcd"));
	}

    
    
    public static String  biggerIsGrater(String w){
    
            
            String test="";
            int i,j=0;
            boolean found=false;
            outerloop:
            for(i = 1;i<=w.length();i++) {
                test = w.substring(w.length() - i); 
                for(j = test.length()-1;j>0;j--) {
                                 
                    if(test.charAt(0)<test.charAt(j)) {
                       found=true;
                        break outerloop;
                        
                    }
                }
            }
            if(found == true){
                char pivot=test.charAt(j);
                String str = test.substring(0,j)+test.substring(j+1);
                char c[] = str.toCharArray();
                Arrays.sort(c); 
                str = pivot + new String(c);
                String result = w.substring(0,w.length()-i)+str;
                return result;    
            }
            else
                return "no answer";
        }

    }

