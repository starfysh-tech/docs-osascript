<a id="//apple_ref/doc/uid/TP40000983-CH225-SW1"></a>

# Double Angle Brackets

<a id="//apple_ref/doc/uid/TP40000983-CH225-DontLinkElementID_435"></a><a id="//apple_ref/doc/uid/TP40000983-CH225-DontLinkElementID_436"></a><a id="//apple_ref/doc/uid/TP40000983-CH225-DontLinkElementID_437"></a>When you type English language script statements in a Script Editor script window, AppleScript is able to compile the script because the English terms are described either in the terminology built into the AppleScript language or in the dictionary of an available scriptable application or scripting addition. When AppleScript compiles your script, it converts it into an internal executable format, then reformats the text to conform to settings in Script Editor’s Formatting preferences.

When you open, compile, edit, or run scripts with Script Editor, you may occasionally see terms enclosed in double angle brackets, or chevrons<a id="//apple_ref/doc/uid/TP40000983-CH225-DontLinkElementID_438"></a> («»). For example, you might see the term `«event sysodlog»` as part of a script—this is the event code representation for a `display dialog` command. The event code representation is also known as <a id="//apple_ref/doc/uid/TP40000983-CH225-DontLinkElementID_439"></a>*raw format*.

For compatibility with Asian national encodings, “《” and “》” are allowed as synonyms for “«” and “»” ( (Option- \ and Option-Shift- \, respectively, on a U.S. keyboard), since the latter do not exist in some Asian encodings.

The following sections provide more information about when chevrons appear in scripts.

<a id="//apple_ref/doc/uid/TP40000983-CH225-SW37"></a>

## When a Dictionary Is Not Available

<a id="//apple_ref/doc/uid/TP40000983-CH225-DontLinkElementID_440"></a>

AppleScript uses double angle brackets in a Script Editor script window when it can’t identify a term. That happens when it encounters a term that isn’t part of the AppleScript language and isn’t defined in an application or scripting addition dictionary that is available when the script is opened or compiled.

For example, if a script is compiled on one machine and later opened on another, the dictionary may not be available, or may be from an older version of the application or scripting addition that does not support the term.

This can also happen if the file `StandardAdditions.osax` is not present in `/System/ScriptingAdditions`. Then, scripting addition commands such as `display dialog` will not be present and will be replaced with chevron notation (`«event sysodlog»`) when you compile or run the script.

<a id="//apple_ref/doc/uid/TP40000983-CH225-SW2"></a>

## When AppleScript Displays Data in Raw Format

<a id="//apple_ref/doc/uid/TP40000983-CH225-DontLinkElementID_441"></a>

Double angle brackets can also occur in results. For example, if the value of a variable is a `script` object named `Joe`, AppleScript represents the `script` object as shown in this script:

```
script Joe
    property theCount : 0
end script
 
set scriptObjectJoe to Joe
scriptObjectJoe
--result: «script Joe»
```

Similarly, if Script Editor can’t display a variable’s data directly in its native format, it uses double angle brackets to enclose both the word `data` and a sequence of numerical values that represent the data. Although this may not visually resemble the original data, the data’s original format is preserved.

This may occur because an application command returns a value that does not belong to any of the normal AppleScript classes. You can store such data in variables and send them as parameters to other commands, but Script Editor cannot display the data in its native format.

<a id="//apple_ref/doc/uid/TP40000983-CH225-SW3"></a>

## Entering Script Information in Raw Format

<a id="//apple_ref/doc/uid/TP40000983-CH225-DontLinkElementID_442"></a>You can enter double angle brackets, or chevrons («»), directly into a script by typing Option-Backslash and Shift-Option-Backslash. You might want to do this if you’re working on a script that needs to use terminology that isn’t available on your current machine—for example, if you’re working at home and don’t have the latest dictionary for a scriptable application you are developing, but you know the codes for a supported term.

You can also use AppleScript to display the underlying codes for a script, using the following steps:

1. Create a script using standard terms compiled against an available application or scripting addition.
2. Save the script as text and quit Script Editor.
3. Remove the application or scripting addition from the computer.
4. Open the script again and compile it.
5. When AppleScript asks you to locate the application or scripting addition, cancel the dialog.

Script Editor can compile the script, but displays chevron format for any terms that rely on a missing dictionary.

<a id="//apple_ref/doc/uid/TP40000983-CH225-SW4"></a>

## Sending Raw Apple Events From a Script

<a id="//apple_ref/doc/uid/TP40000983-CH225-DontLinkElementID_443"></a>The term `«event sysodlog»` is actually the raw form for an Apple event with event class `'syso'` and event ID `'dlog'` (the `display dialog` command). For a list of many of the four-character codes and their related terminology used by Apple, see *[AppleScript Terminology and Apple Event Codes Reference](../../../../../releasenotes/AppleScript/ASTerminology_AppleEventCodes/TermsAndCodes.html#//apple_ref/doc/uid/TP40004532)*.

You can use raw syntax to enter and execute events (even complex events with numerous parameters) when there is no dictionary to support them. However, providing detailed documentation for how to do so is beyond the scope of this guide.<a id="//apple_ref/doc/uid/TP40000983-CH225-DontLinkElementID_444"></a><a id="//apple_ref/doc/uid/TP40000983-CH225-DontLinkElementID_445"></a><a id="//apple_ref/doc/uid/TP40000983-CH225-DontLinkElementID_446"></a>

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
