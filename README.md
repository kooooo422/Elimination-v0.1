# Elimination-v0.1 
## 切換場景 SceneManager.LoadScene
https://docs.unity3d.com/ScriptReference/SceneManagement.SceneManager.LoadScene.html
```c#
SceneManager.LoadScene(sceneIndex);
```
## 影片播完跳轉 
https://stackoverflow.com/questions/44696030/detect-when-videoplayer-has-finished-playing
```c#
using UnityEngine;
using UnityEngine.Video;

public class filename : MonoBehaviour
{
    private VideoPlayer m_VideoPlayer;

    void Awake () 
    {
        m_VideoPlayer = GetComponent<VideoPlayer>();
        m_VideoPlayer.loopPointReached += OnMovieFinished; // loopPointReached is the event for the end of the video
    }

    void OnMovieFinished(VideoPlayer player)
    {
        Debug.Log("Event for movie end called");
        player.Stop();
    }
}
```
## call sg90 api
```c#
    void GetData() => StartCoroutine(GetData_Coroutine());
 
    IEnumerator GetData_Coroutine()
    {
        Debug.Log("Loading...");
        string url = "yourip";
        using(UnityWebRequest request = UnityWebRequest.Get(url))
        {
            yield return request.SendWebRequest();
            if (request.isNetworkError || request.isHttpError){
                Debug.Log(request.error);
            }
            else{
                Debug.Log(request.downloadHandler.text);
            }
        }
    }
```
## call esp8266 LED on
https://stackoverflow.com/questions/60862424/how-to-post-my-data-using-unitywebrequest-post-api-call
```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
public class UserData 
{
    public string LED_id;
    public string LED_index;
    public string LED_status;
}
public class backend : MonoBehaviour
{
    void Start()
    {
        Debug.Log("hi");
         StartCoroutine(sendData("1", "2", "on"));
    }
    public IEnumerator sendData(string LED_id, string LED_index, string LED_status)   
    {
        var user = new UserData();
        user.LED_id = LED_id;
        user.LED_index = LED_index;
        user.LED_status = LED_status;

        string json = JsonUtility.ToJson(user);

        var req = new UnityWebRequest("your url", "POST");
        byte[] jsonToSend = new System.Text.UTF8Encoding().GetBytes(json);
        req.uploadHandler = (UploadHandler)new UploadHandlerRaw(jsonToSend);
        req.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        req.SetRequestHeader("Content-Type", "application/json");

        //Send the request then wait here until it returns
        yield return req.SendWebRequest();

        if (req.isNetworkError)
        {
            Debug.Log("Error While Sending: " + req.error);
        }
        else
        {
            Debug.Log("Received: " + req.downloadHandler.text);
        }

    }
}

```
## backend.cs
```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
public class UserData 
{
    public string Led_id;
    public string Led_index;
    public string Led_status;
}
public class backend : MonoBehaviour
{
    public string Id;
    public string Index;
    public string Status;
    void Start()
    {
        StartCoroutine(sendData(Id, Index, Status));
    }
    public IEnumerator sendData(string Led_id, string Led_index, string Led_status)   
    {
        var user = new UserData();
        user.Led_id = Led_id;
        user.Led_index = Led_index;
        user.Led_status = Led_status;

        string json = JsonUtility.ToJson(user);

        var req = new UnityWebRequest("apiURL", "POST");
        byte[] jsonToSend = new System.Text.UTF8Encoding().GetBytes(json);
        req.uploadHandler = (UploadHandler)new UploadHandlerRaw(jsonToSend);
        req.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        req.SetRequestHeader("Content-Type", "application/json");

        //Send the request then wait here until it returns
        yield return req.SendWebRequest();

        if (req.isNetworkError)
        {
            Debug.Log("Error While Sending: " + req.error);
        }
        else
        {
            Debug.Log("Received: " + req.downloadHandler.text);
        }

    }   
}

```
## callapi.cs
```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
public class LedsData 
{
    public string Led_id;
    public string Led_index;
    public string Led_status;
}
public class callAPI : MonoBehaviour
{
    // Start is called before the first frame update
    public string Id;
    public string Index;
    public string Status_Normal;
    public string Status_Warning;
    public string Status_Sad;
    public string callSG90url;
    public string callLedurl;
    public void call_sg90(){
        StartCoroutine(GetData(callSG90url));
    }
    public void call_leds_normal(){
        StartCoroutine(postData(callLedurl,Id, Index, Status_Normal));
    } 
    public void call_leds_warning(){
        StartCoroutine(postData(callLedurl,Id, Index, Status_Warning));
    } 
    public void call_leds_sad(){
        StartCoroutine(postData(callLedurl,Id, Index, Status_Sad));
    } 
    IEnumerator GetData(string URL)
    {
        Debug.Log("Loading...");
        using(UnityWebRequest request = UnityWebRequest.Get(URL))
        {
            yield return request.SendWebRequest();
            if (request.isNetworkError || request.isHttpError){
                Debug.Log(request.error);
            }
            else{
                Debug.Log(request.downloadHandler.text);
            }
        }
    }
    IEnumerator postData(string URL,string Led_id, string Led_index, string Led_status)   
    {
        var user = new LedsData();
        user.Led_id = Led_id;
        user.Led_index = Led_index;
        user.Led_status = Led_status;

        string json = JsonUtility.ToJson(user);

        var req = new UnityWebRequest(URL, "POST");
        byte[] jsonToSend = new System.Text.UTF8Encoding().GetBytes(json);
        req.uploadHandler = (UploadHandler)new UploadHandlerRaw(jsonToSend);
        req.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        req.SetRequestHeader("Content-Type", "application/json");

        //Send the request then wait here until it returns
        yield return req.SendWebRequest();

        if (req.isNetworkError)
        {
            Debug.Log("Error While Sending: " + req.error);
        }
        else
        {
            Debug.Log("Received: " + req.downloadHandler.text);
        }

    }
}

```
## fungus
source code https://github.com/snozbot/fungus/releases/tag/v.3.13.8 <br>
教學連結 https://forum.gamer.com.tw/C.php?bsn=60602&snA=514
# esp8266
## Split String into String array
https://stackoverflow.com/questions/9072320/split-string-into-string-array
```ino
String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}
```
### test function
```ino
String split = "hi this is a split test";
String word3 = getValue(split, ' ', 2);
Serial.println(word3);
```
