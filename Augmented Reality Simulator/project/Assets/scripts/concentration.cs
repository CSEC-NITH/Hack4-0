using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class concentration : MonoBehaviour
{
    private Text conctext;
    public double conc;
    // Start is called before the first frame update
    void Start()
    {
        conctext = GetComponent<Text>();
        conc = 0;
    }

    // Update is called once per frame
    void Update()
    {
        conc = changes.getconc();
        conctext.text = "Conc. of Fe2+ ion :  " + conc + " N";
    }
    
}
