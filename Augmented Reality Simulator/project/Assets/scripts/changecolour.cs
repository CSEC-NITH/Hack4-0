using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class changecolour : MonoBehaviour
{
   public static Renderer rend;
   
    
    
    // Start is called before the first frame update
    public void Start()
    {
        rend = GetComponent<Renderer>();
    }

    // Update is called once per frame
   public static void changebet()
    {
        rend.material.color = new Color(255, 255, 255);
       
    }
    public static void changeend()
    {
        rend.material.color = new Color(255, 30, 0);

    }
}
