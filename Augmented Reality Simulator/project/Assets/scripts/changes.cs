using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class changes : MonoBehaviour
{
    private Text thisText;
   public static double volume,Conc;
   
    // Start is called before the first frame update
    void Start()
    {
        thisText = GetComponent<Text>();
       

        // set score value to be zero
        volume = 0;
        Conc = 0;
       
    }

    // Update is called once per frame
    void Update()
    {
        // update text of Text element
        thisText.text = "KMno4 used:   " + volume +" mL";
     

    }
    public static void AddDrop()
    {
        // add 500 points to score
        
        volume += 0.3;
        Conc = volume / 500;
        
      
    }
    public static bool check()
    {
        if (volume == 1.5)
        {
           
            changecolour.changebet();

        }
        if (volume == 2.1)
        {
        
            changecolour.changeend();

        }
        if (volume == 2.4)
        {
           
            return true;
        }
        return false;
    }
    public static double getconc()
    {
        return Conc;
        
    }
    public static double getvol()
    {
        return volume;

    }
    public static double getppm()
    {
        return Conc*1000;

    }
}


