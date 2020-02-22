using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class disablepanel : MonoBehaviour
{
    public GameObject Panel;
   
    public void see()
    {
            changes.volume = 0;
            changes.Conc = 0;
            Panel.SetActive(false);
        
        
    }
}
