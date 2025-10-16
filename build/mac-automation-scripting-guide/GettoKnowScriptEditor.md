## Getting to Know Script Editor

![image: ../Art/script-editor_icon_2x.png](Art/script-editor_icon_2x.png)

Script Editor, found in `/Applications/Utilities/`, is an app for writing AppleScripts and JavaScripts. It provides the ability to edit, compile, and run scripts, browse scripting terminology, and save scripts in a variety of formats including compiled scripts, apps, and plain text.

> **Note**
>
>
> Xcode can also be used to write AppleScriptObjC and JavaScriptObjC apps.

### Navigating Script Editor Documents

A Script Editor document window includes the following main areas, as shown in Figure 5-1:

**Figure 5-1**A Script Editor document window
![image: ../Art/script-editor_window_withcallouts_2x.png](Art/script-editor_window_withcallouts_2x.png)

* **Toolbar**—Use this to compile, run, and stop your script. Buttons are also available for showing and hiding the accessory view pane and the bundle contents pane. Select View > Customize Toolbar, or Control-click on the toolbar and choose Customize Toolbar, to choose what buttons displayed in the toolbar.

  The toolbar also includes a Record button, which converts manual mouse clicks and keystrokes into script code. However, recording is not supported in JavaScript and few apps support AppleScript recording.
* **Navigation bar**—Use this bar to select a scripting language, target an app, or navigate through the handlers in your script.

  The navigation bar currently only supports navigation of AppleScript handlers.
* **Editor pane**—Write your script code here.
* **Accessory View pane**—View and edit your script’s description here, or browse the result and events produced when your script runs.
* **Bundle Contents pane**— Edit the identifier, version, and copyright info for your script here. You can also use this pane to add, remove, or manage resources contained within the bundle. This pane is accessible only when your script is saved in script bundle or app format.

### Targeting a Scripting Language

When you create a Script Editor document, select a scripting language in the navigation bar. See Figure 5-2.

**Figure 5-2**Setting the scripting language in a Script Editor document window
![image: ../Art/script-editor_langage_selector_2x.png](Art/script-editor_langage_selector_2x.png)

If you always use the same language, set it as the default in the General pane of Script Editor preferences. See Figure 5-3.

**Figure 5-3**Setting the default scripting language for Script Editor documents
![image: ../Art/script-editor_preferences_window_general_pane_language_2x.png](Art/script-editor_preferences_window_general_pane_language_2x.png)

### Viewing Script Events and Results

Script Editor can display the result of executing a script, as well as a log of events sent and received during execution.

> **Note**
>
>
> A *result* is a value generated when a script statement executes. For example, executing the `make` command to create a folder in the Finder produces the newly created folder object as its result. The result of a script is the result of the script’s last statement. If the script’s last statement doesn’t produce a result, then the script has no result.

### Viewing the Script Result

The result of executing your script—if a result was produced—is found in the Accessory View pane. See Figure 5-4.

**Figure 5-4**Viewing the result of a script in Script Editor
![image: ../Art/script-editor_window_result_2x.png](Art/script-editor_window_result_2x.png)

**To view the result of your script**

Do one of the following:

* Press Command-2.
* Choose View > Show Result.
* Click the Show Result (![image: ../Art/icon_showresult_2x.png](Art/icon_showresult_2x.png)) button at the bottom of the Accessory View pane.

### Viewing the Script Log

The Accessory View pane also contains a script log. See Figure 5-5.

**Figure 5-5**Viewing the script log in Script Editor
![image: ../Art/script-editor_eventlog_2x.png](Art/script-editor_eventlog_2x.png)

The script log displays the following information.

* **Result**—The result of executing your script.
* **Messages**—Includes log messages generated as your script runs, as well as the script’s result.
* **Events**—Includes log messages, the script’s result, and events—commands—sent to applications.
* **Replies**—Includes log messages, the script’s result, events sent to applications, and event replies.

**To view the script log**

Do one of the following:

* Press Command-3.
* Choose View > Show Log.
* Click the Show Log (![image: ../Art/icon_showlog_2x.png](Art/icon_showlog_2x.png)) button at the bottom of the Accessory View pane.

> **Note**
>
>
> In AppleScript, log messages are generated using the `log` command. See Listing 5-1.
>
> **APPLESCRIPT**
>
> [Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Log%20a%20Message&script=log%20%22My%20log%20entry.%22%0D)
>
> **Listing 5-1**AppleScript: Example of a log message at the root level of a script
>
> 1. `log "My log entry."`
>
> Since the `log` command targets the script itself, you must explicitly use the `me` keyword to direct it to the script when calling it within a tell statement. See Listing 5-2.
>
> **APPLESCRIPT**
>
> [Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Log%20a%20Message%20in%20a%20Tell%20Statement&script=tell%20app%20%22Finder%22%0D%20%20%20%20tell%20me%20to%20log%20%22My%20log%20entry.%22%0Dend%20tell%0D)
>
> **Listing 5-2**AppleScript: Example of a log message within an application tell statement
>
> 1. `tell app "Finder"`
> 2. ` tell me to log "My log entry."`
> 3. `end tell`
>
> In JavaScript, log messages are generated by calling the `console.log()` method anywhere in your script. See Listing 5-3.
>
> **JAVASCRIPT**
>
> [Open in Script Editor](applescript://com.apple.scripteditor?action=new&name=Log%20a%20Message&script=console.log%28%22My%20log%20entry.%22%29%0D)
>
> **Listing 5-3**JavaScript: Example of a log message
>
> 1. `console.log("My log entry.")`

### Viewing the Log History

The result and script log areas in the Accessory View pane reset each time you run your script. However, you can view historical logs for an opened script in the Log History window. See Figure 5-6.

**Figure 5-6**The Log History window in Script Editor
![image: ../Art/script-editor_resulthistory_window_2x.png](Art/script-editor_resulthistory_window_2x.png)

**To view the Log History window**

Do one of the following:

* Press Option-Command-L.
* Choose View > Log History.
* Click the Log History button (![image: ../Art/icon_loghistory_2x.png](Art/icon_loghistory_2x.png)) in the top right of the Accessory View pane.
