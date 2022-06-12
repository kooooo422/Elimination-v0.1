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
## fungus
source code https://github.com/snozbot/fungus/releases/tag/v.3.13.8 <br>
教學連結 https://forum.gamer.com.tw/C.php?bsn=60602&snA=514
