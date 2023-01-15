using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LoadAsset : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        // GameObject instance = Instantiate(Resources.Load("sampleFurniture", typeof(GameObject))) as GameObject;
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    public void loadModel(){
        Resources.Load("sampleFurniture", typeof(GameObject));
    }
}
