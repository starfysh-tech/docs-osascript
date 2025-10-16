<a id="//apple_ref/doc/uid/TP40016239-CH37"></a><a id="//apple_ref/doc/uid/TP40016239-CH37-SW1"></a>

## Displaying Progress

Many scripts perform large and time-consuming processing operations. All too often, they do this invisibly; they simply run and the user has no idea how long processing will take. A more user-friendly approach is to provide progress information during script operation. At a basic level, this can be done by displaying periodic dialogs or notifications. See [Displaying Dialogs and Alerts](https://developer.apple.com/library/archive/mac-automation-scripting-guide/DisplayDialogsandAlerts.md#//apple_ref/doc/uid/TP40016239-CH15-SW1) and [Displaying Notifications](https://developer.apple.com/library/archive/mac-automation-scripting-guide/DisplayNotifications.md#//apple_ref/doc/uid/TP40016239-CH61-SW1). At a complex level, this can be done by designing a fully-custom interface that provides processing feedback.

AppleScript and JavaScript can also report progress graphically and textually. For script apps, this progress reporting takes the form of a dialog window containing a progress bar, descriptive text, and a Stop button. See Figure 30-1.

<a id="//apple_ref/doc/uid/TP40016239-CH37-SW2"></a>
**Figure 30-1**A script progress dialog
![image: ../Art/progress_dialog_2x.png](https://developer.apple.com/library/archive/mac-automation-scripting-guide/Art/progress_dialog_2x.png)

For scripts running in Script Editor, this progress reporting appears at the bottom of the script window. See Figure 30-2.

<a id="//apple_ref/doc/uid/TP40016239-CH37-SW3"></a>
**Figure 30-2**Progress displayed in Script Editor
![image: ../Art/scripteditor_progress_2x.png](https://developer.apple.com/library/archive/mac-automation-scripting-guide/Art/scripteditor_progress_2x.png)

For scripts running from the systemwide script menu, this progress reporting appears in the menu bar, beneath a temporarily displayed gear icon. See Figure 30-3.

<a id="//apple_ref/doc/uid/TP40016239-CH37-SW4"></a>
**Figure 30-3**Progress of a script menu script
![image: ../Art/scriptmenu_progress_2x.png](https://developer.apple.com/library/archive/mac-automation-scripting-guide/Art/scriptmenu_progress_2x.png)

AppleScript has several language-level properties and JavaScript has a `Progress` object with properties that are used to produce this type of progress reporting. See Table 30-1.

<a id="//apple_ref/doc/uid/TP40016239-CH37-SW5"></a>

**Table 30-1**Progress properties in AppleScript and JavaScript

| AppleScript Property | JavaScript Property | Value Type | Description |
| --- | --- | --- | --- |
| `progress total steps` | `Progress.totalUnitCount` | Integer | Configures the total number of steps to be reported in the progress. For example, if the script will process 5 images, then the value for `progress total steps` would be `5`. |
| `progress completed steps` | `Progress.completedUnitCount` | Integer | Configures the number of steps completed so far. For example, if the script has processed 3 of 5 images, then the value of `progress completed steps` would be `3`. |
| `progress description` | `Progress.description` | Integer | Text to display when reporting progress. Use this is an opportunity to let the user know what’s happening. For example, it could indicate that images are being processed. |
| `progress additional description` | `Progress.additionalDescription` | Integer | Additional text to display when reporting progress. Use this is an opportunity to provide even more detailed information about what’s happening. For example, it could indicate the specific task being performed, and how much more processing is remaining. |

Listing 30-1 and Listing 30-2 demonstrate how these properties can be used to provide progress information while processing a set of images.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20theImages%20to%20choose%20file%20with%20prompt%20%22Please%20select%20some%20images%20to%20process%3A%22%20of%20type%20%7B%22public.image%22%7D%20with%20multiple%20selections%20allowed%0A%0A--%20Update%20the%20initial%20progress%20information%0Aset%20theImageCount%20to%20length%20of%20theImages%0Aset%20progress%20total%20steps%20to%20theImageCount%0Aset%20progress%20completed%20steps%20to%200%0Aset%20progress%20description%20to%20%22Processing%20Images...%22%0Aset%20progress%20additional%20description%20to%20%22Preparing%20to%20process.%22%0A%0Arepeat%20with%20a%20from%201%20to%20length%20of%20theImages%0A%0A%20%20%20%20--%20Update%20the%20progress%20detail%0A%20%20%20%20set%20progress%20additional%20description%20to%20%22Processing%20image%20%22%20%26%20a%20%26%20%22%20of%20%22%20%26%20theImageCount%0A%0A%20%20%20%20--%20Process%20the%20image%0A%0A%20%20%20%20--%20Increment%20the%20progress%0A%20%20%20%20set%20progress%20completed%20steps%20to%20a%0A%0A%20%20%20%20--%20Pause%20for%20demonstration%20purposes%2C%20so%20progress%20can%20be%20seen%0A%20%20%20%20delay%201%0Aend%20repeat%0A%0A--%20Reset%20the%20progress%20information%0Aset%20progress%20total%20steps%20to%200%0Aset%20progress%20completed%20steps%20to%200%0Aset%20progress%20description%20to%20%22%22%0Aset%20progress%20additional%20description%20to%20%22%22)

<a id="//apple_ref/doc/uid/TP40016239-CH37-SW6"></a>
**Listing 30-1**AppleScript: Display progress while processing images

1. `set theImages to choose file with prompt "Please select some images to process:" of type {"public.image"} with multiple selections allowed`
2. ` `
3. `-- Update the initial progress information`
4. `set theImageCount to length of theImages`
5. `set progress total steps to theImageCount`
6. `set progress completed steps to 0`
7. `set progress description to "Processing Images..."`
8. `set progress additional description to "Preparing to process."`
9. ` `
10. `repeat with a from 1 to length of theImages`
11. ` `
12. ` -- Update the progress detail`
13. ` set progress additional description to "Processing image " & a & " of " & theImageCount`
14. ` `
15. ` -- Process the image`
16. ` `
17. ` -- Increment the progress`
18. ` set progress completed steps to a`
19. ` `
20. ` -- Pause for demonstration purposes, so progress can be seen`
21. ` delay 1`
22. `end repeat`
23. ` `
24. `-- Reset the progress information`
25. `set progress total steps to 0`
26. `set progress completed steps to 0`
27. `set progress description to ""`
28. `set progress additional description to ""`

**JAVASCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=var%20app%20%3D%20Application.currentApplication%28%29%0Aapp.includeStandardAdditions%20%3D%20true%0A%0Avar%20images%20%3D%20app.chooseFile%28%7B%0A%20%20%20%20withPrompt%3A%20%22Please%20select%20some%20images%20to%20process%3A%22%2C%0A%20%20%20%20ofType%3A%20%5B%22public.image%22%5D%2C%0A%20%20%20%20multipleSelectionsAllowed%3A%20true%0A%7D%29%0A%0A%2F%2F%20Update%20the%20initial%20progress%20information%0Avar%20imageCount%20%3D%20images.length%0AProgress.totalUnitCount%20%3D%20imageCount%0AProgress.completedUnitCount%20%3D%200%0AProgress.description%20%3D%20%22Processing%20Images...%22%0AProgress.additionalDescription%20%3D%20%22Preparing%20to%20process.%22%0A%0Afor%20%28i%20%3D%200%3B%20i%20%3C%20imageCount%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20%2F%2F%20Update%20the%20progress%20detail%0A%20%20%20%20Progress.additionalDescription%20%3D%20%22Processing%20image%20%22%20%2B%20i%20%2B%20%22%20of%20%22%20%2B%20imageCount%0A%0A%20%20%20%20%2F%2F%20Process%20the%20image%0A%0A%20%20%20%20%2F%2F%20Increment%20the%20progress%0A%20%20%20%20Progress.completedUnitCount%20%3D%20i%0A%0A%20%20%20%20%2F%2F%20Pause%20for%20demonstration%20purposes%2C%20so%20progress%20can%20be%20seen%0A%20%20%20%20delay%281%29%0A%7D)

<a id="//apple_ref/doc/uid/TP40016239-CH37-SW7"></a>
**Listing 30-2**JavaScript: Display progress while processing images

1. `var app = Application.currentApplication()`
2. `app.includeStandardAdditions = true`
3. ` `
4. `var images = app.chooseFile({`
5. ` withPrompt: "Please select some images to process:",`
6. ` ofType: ["public.image"],`
7. ` multipleSelectionsAllowed: true`
8. `})`
9. ` `
10. `// Update the initial progress information`
11. `var imageCount = images.length`
12. `Progress.totalUnitCount = imageCount`
13. `Progress.completedUnitCount = 0`
14. `Progress.description = "Processing Images..."`
15. `Progress.additionalDescription = "Preparing to process."`
16. ` `
17. `for (i = 0; i < imageCount; i++) {`
18. ` // Update the progress detail`
19. ` Progress.additionalDescription = "Processing image " + i + " of " + imageCount`
20. ` `
21. ` // Process the image`
22. ` `
23. ` // Increment the progress`
24. ` Progress.completedUnitCount = i`
25. ` `
26. ` // Pause for demonstration purposes, so progress can be seen`
27. ` delay(1)`
28. `}`

Clicking the Stop button in a progress dialog results in a user cancelled error.

For additional information, see [Progress Reporting](https://developer.apple.com/library/archive/../../../releasenotes/AppleScript/RN-AppleScript/RN-10_10/RN-10_10.html#//apple_ref/doc/uid/TP40000982-CH110-SW8) in *[AppleScript Release Notes](https://developer.apple.com/library/archive/../../../releasenotes/AppleScript/RN-AppleScript/Introduction/Introduction.html#//apple_ref/doc/uid/TP40000982)* and [Progress](https://developer.apple.com/library/archive/../../../releasenotes/InterapplicationCommunication/RN-JavaScriptForAutomation/Articles/OSX10-10.html#//apple_ref/doc/uid/TP40014508-CH109-SW35) in *[JavaScript for Automation Release Notes](https://developer.apple.com/library/archive/../../../releasenotes/InterapplicationCommunication/RN-JavaScriptForAutomation/Articles/Introduction.html#//apple_ref/doc/uid/TP40014508)*.

> **Note**
>
>
> There’s no need to call a dedicated command to actually display progress information. The act of setting values for the progress properties mentioned above automatically results in progress information being displayed in a dialog, Script Editor, or the menu bar.
