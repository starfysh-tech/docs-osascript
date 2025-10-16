<a id="//apple_ref/doc/uid/TP40016239-CH72"></a><a id="//apple_ref/doc/uid/TP40016239-CH72-SW1"></a>

## Types of Scripts

There are many different types of scripts on the Mac.

![image: ../Art/icon_applet_48_2x.png](Art/icon_applet_48_2x.png)

**Applets**—A script that’s been saved as an app. It behaves like other apps. Double-click it to launch and run it. When an applet is launched, any code in its `run` handler executes. If a script doesn’t contain an explicit `run` handler, then the top level of the script is treated as an implicit `run` handler and any code there executes.

![image: ../Art/icon_droplet_48_2x.png](Art/icon_droplet_48_2x.png)

**Droplets**—A script applet that has been configured to accept dropped files and folders. Double-click it to launch and run it—execute its `run` handler. Or, drag and drop files and folders onto it to process them. In a droplet, dropped files and folders are passed directly to an AppleScript `open` handler or JavaScript `openDocuments` function for processing.

![image: ../Art/icon_compiled_48_2x.png](Art/icon_compiled_48_2x.png)

**Scripts**—A script document file. Double-click it to open it for editing. Some apps and processes can load and run scripts. For example, Mail rules can execute scripts to process messages matching specific criteria. Scripts are sometimes referred to as *compiled scripts*.

![image: ../Art/icon_compiled_48_2x.png](Art/icon_compiled_48_2x.png)

**Script bundles**—A script document that’s been saved in *bundle* format. A bundle is a directory with a standardized, hierarchical structure that holds executable code and the resources used by that code.

![image: ../Art/icon_applet_48_2x.png](Art/icon_applet_48_2x.png)

**Stay-open scripts**—By default, applets and droplets run and quit after launch. When configured as stay-open, however, they remain open until explicitly ordered to quit. Often, stay-open scripts include an `idle` handler, which initiates periodic actions.

For detailed information about `run`, `open`, and `idle` handlers in AppleScript, see [Handlers in Script Applications](../../../AppleScript/Conceptual/AppleScriptLangGuide/conceptual/ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-SW14) in *[AppleScript Language Guide](../../../AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html#//apple_ref/doc/uid/TP40000983)*. For information about `run`, `openDocuments`, and `idle` functions in JavaScript, see [Applets](../../../../releasenotes/InterapplicationCommunication/RN-JavaScriptForAutomation/Articles/OSX10-10.html#//apple_ref/doc/uid/TP40014508-CH109-SW15) in *[JavaScript for Automation Release Notes](../../../../releasenotes/InterapplicationCommunication/RN-JavaScriptForAutomation/Articles/Introduction.html#//apple_ref/doc/uid/TP40014508)*. For information about bundles, see *[Bundle Programming Guide](../../../CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i)*.
