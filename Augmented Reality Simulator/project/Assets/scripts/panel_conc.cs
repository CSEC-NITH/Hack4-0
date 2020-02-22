using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class panel_conc : MonoBehaviour
{
    public Text tt;
    public double conc;
    // Start is called before the first frame update
    void Start()
    {

        tt = GetComponent<Text>();
    }

    // Update is called once per frame
    void Update()
    {
        conc = changes.getconc();
        tt.text = "   " + conc + "  grams / Litre";
    }
}
