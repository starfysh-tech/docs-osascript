## About this Guide

This guide provides high-level information about scripting on the Mac and isn’t designed to serve as a language guide. Primarily, it introduces core concepts, highlights resources, and provides examples that demonstrate common scripting tasks.

This guide does not provide examples for every possible task that can be scripted in a given situation or app. For example, it doesn’t cover automating every single scriptable text manipulation function. Instead, it covers automating a range of commonly encountered scenarios, such as changing the case of text, splitting text, and adding a prefix to text. These examples can be used for guidance when attempting to automate other scriptable tasks.

Many of the examples in this guide have been written modularly, allowing them to be copied and pasted into your own scripts, where they may be used as is or modified to meet your unique needs. Most examples are commented and relatively easy to follow, even with little or no prior scripting experience.

The majority of examples in this guide are provided in both AppleScript and JavaScript format. A language label precedes each example, making its language easily distinguishable at a glance. Some examples demonstrate using the scripting bridges, AppleScriptObjC and JavaScriptObjC, to interact with Objective-C classes. Additional examples are occasionally provided in notes to show alternative solutions.

> **Note**
>
>
> Some examples in this guide require OS X 10.11 or later.
>
> Some JavaScript examples in this guide use template strings—string literals which may include embedded expressions, such as the one shown in Listing 4-1.
>
> **JAVASCRIPT**
>
> [Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=numberOfPeople%20%3D%2012%0Aconsole.log%28%60There%20are%20%24%7BnumberOfPeople%7D%20people.%60%29)
>
> **Listing 4-1**JavaScript: Example of a Template String with an embedded expression
>
> 1. `numberOfPeople = 12`
> 2. `` console.log(`There are ${numberOfPeople} people.`) ``
>
> Template strings were introduced as a JavaScript standard in 2015, and are supported in OS X 10.11 and later.

### Opening Examples in Script Editor

Links have been provided throughout this guide to open example code directly in Script Editor. To open an example, click the “Open in Script Editor” link above a code listing. Depending on the security settings on your Mac, you may be prompted to confirm you want to open the script in Script Editor. If you receive this prompt, click the New Script button to create a new document. See Figure 4-1 and Figure 4-2.

**Figure 4-1**The dialog that opens when you click the “Open in Script Editor” link
![image: ../Art/scripteditor_openscript_alert_2x.png](Art/scripteditor_openscript_alert_2x.png)

**Figure 4-2**Example of a script that opens after you click the New Script button
![image: ../Art/scripteditor_openedscript_2x.png](Art/scripteditor_openedscript_2x.png)
> **Note**
>
>
> New Script Editor documents are set to use your default scripting language, as configured in the General pane of Script Editor preferences. See [Targeting a Scripting Language](GettoKnowScriptEditor.md#//apple_ref/doc/uid/TP40016239-CH5-SW4) to learn how to configure an example script to target a different scripting language.
