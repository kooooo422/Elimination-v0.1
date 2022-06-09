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
## fungus
source code https://github.com/snozbot/fungus/releases/tag/v.3.13.8 <br>
教學連結 https://forum.gamer.com.tw/C.php?bsn=60602&snA=514
