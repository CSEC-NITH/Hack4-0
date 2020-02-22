using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class textincrease : MonoBehaviour
{
    public GameObject Panel;

    public void increase()
    {
        changes.AddDrop();

       bool a = changes.check();
        if (a)
        {
            if (Panel != null)
            {
               
                Panel.SetActive(true);
            }
        }
    }

    public void playin()
    {
        
        animate.playi();
    }
   
   
}

