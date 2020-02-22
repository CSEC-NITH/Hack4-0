using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class animate : MonoBehaviour
{
    public static Animator anim;
    // Start is called before the first frame update
    public GameObject button;
    void Start()
    {
        anim = GetComponent<Animator>();
        button = GetComponent<GameObject>();
        
    }

    // Update is called once per frame
    public static void playi()
    {
       
            anim.Play("New Animation");
        
    }
   
 
        
    
}
