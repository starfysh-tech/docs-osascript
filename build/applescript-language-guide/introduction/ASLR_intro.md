<a id="//apple_ref/doc/uid/TP40000983"></a><a id="//apple_ref/doc/uid/TP40000983-CH208-SW1"></a>

# Introduction to AppleScript Language Guide

This document is a guide to the AppleScript language—its lexical conventions, syntax, keywords, and other elements. It is intended primarily for use with AppleScript 2.0 or later and macOS version 10.5 or later.

AppleScript 2.0 can use scripts developed for any version of AppleScript from 1.1 through 1.10.7, any scripting addition created for AppleScript 1.5 or later for macOS, and any scriptable application for Mac OS v7.1 or later. A script created with AppleScript 2.0 can be used by any version of AppleScript back to version 1.1, provided it does not use features of AppleScript, scripting additions, or scriptable applications that are unavailable in that version.

> <a id="//apple_ref/doc/uid/TP40000983-CH208-DontLinkElementID_14"></a>
>
> **Important:** Descriptions and examples for the terms in this document have been tested with AppleScript 2.0 in OS X v10.5 (Leopard). Except for terms that are noted as being new in Leopard, most descriptions and examples work with previous system versions, but have not been tested against all of them.
>
> If you need detailed information about prior system and AppleScript versions, see *AppleScript Release Notes (OS X v10.4 and earlier)*.

<a id="//apple_ref/doc/uid/TP40000983-CH208-SW2"></a>

## What Is AppleScript?

<a id="//apple_ref/doc/uid/TP40000983-CH208-DontLinkElementID_519"></a>AppleScript is a scripting language created by Apple. It allows users to directly control scriptable Macintosh applications, as well as parts of macOS itself. You can create scripts—sets of written instructions—to automate repetitive tasks, combine features from multiple scriptable applications, and create complex workflows.

> <a id="//apple_ref/doc/uid/TP40000983-CH208-SW3"></a>
>
> **Note:** Apple also provides the Automator application, which allows users to automate common tasks by hooking together ready-made actions in a graphical environment. For more information, see [Automator Documentation](../../../../../navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP40005948-TP40001673).

A scriptable application is one that can be controlled by a script. For AppleScript, that means being responsive to interapplication messages, called <a id="//apple_ref/doc/uid/TP40000983-CH208-DontLinkElementID_520"></a>*Apple events*, sent when a script command targets the application. (Apple events can also be sent directly from other applications and macOS.)

AppleScript itself provides a very small number of commands, but it provides a framework into which you can plug many task-specific commands—those provided by scriptable applications and scriptable parts of macOS.

Most script samples and script fragments in this guide use scriptable features of the Finder application, scriptable parts of macOS, or scriptable applications distributed with macOS, such as TextEdit (located in `/Applications`).

<a id="//apple_ref/doc/uid/TP40000983-CH208-SW4"></a>

## Who Should Read This Document?

You should use this document if you write or modify AppleScript scripts, or if you create scriptable applications and need to know how scripts should work.

*AppleScript Language Guide* assumes you are familiar with the high-level information about AppleScript found in *[AppleScript Overview](../../AppleScriptX/AppleScriptX.html#//apple_ref/doc/uid/10000156i)*.

<a id="//apple_ref/doc/uid/TP40000983-CH208-DontLinkElementID_1"></a>

## Organization of This Document

This guide describes the AppleScript language in a series of chapters and appendixes.

The first five chapters introduce components of the language and basic concepts for using it, then provide additional overview on working with script objects and handler routines:

* [AppleScript Lexical Conventions](../conceptual/ASLR_lexical_conventions.html#//apple_ref/doc/uid/TP40000983-CH214-SW1) describes the characters, symbols, keywords, and other language elements that make up statements in an AppleScript script.
* [AppleScript Fundamentals](../conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW2) describes basic concepts that underly the terminology and rules covered in the rest of this guide.
* [Variables and Properties](../conceptual/ASLR_variables.html#//apple_ref/doc/uid/TP40000983-CH223-SW10) describes common issues in working with variables and properties, including how to declare them and how AppleScript interprets their scope.
* [Script Objects](../conceptual/ASLR_script_objects.html#//apple_ref/doc/uid/TP40000983-CH207-BAJJCIAA) describes how to define, initialize, send commands to, and use inheritance with script objects.
* [About Handlers](../conceptual/ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-CJBIDBJH) provides information on using handlers (a type of function available in AppleScript) to factor and reuse code.

The following chapters provide reference for the AppleScript Language:

* [Class Reference](../reference/ASLR_classes.html#//apple_ref/doc/uid/TP40000983-CH1g-246384) describes the classes AppleScript defines for common objects used in scripts.
* [Commands Reference](../reference/ASLR_cmds.html#//apple_ref/doc/uid/TP40000983-CH216-SW59) describes the commands that are available to any script.
* [Reference Forms](../reference/ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-120522) describes the syntax for specifying an object or group of objects in an application or other container.
* [Operators Reference](../reference/ASLR_operators.html#//apple_ref/doc/uid/TP40000983-CH5g-124070) provides a list of the operators AppleScript supports and the rules for using them, along with sections that provide additional detail for commonly used operators.
* [Control Statements Reference](../reference/ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-157332) describes statements that control when and how other statements are executed. It covers standard conditional statements, as well as statements used in error handling and other operations.
* [Handler Reference](../reference/ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-163762) shows the syntax for defining and calling handlers and describes other statements you use with handlers.

The following chapter describes an AppleScript-related feature of macOS:

* [Folder Actions Reference](../reference/ASLR_folder_actions.html#//apple_ref/doc/uid/TP40000983-CH219-SW2) describes how you can write and attach script handlers to specific folders, such that the handlers are invoked when the folders are modified.

The following appendixes provide additional information about the AppleScript language and how to work with errors in scripts:

* [AppleScript Keywords](../reference/ASLR_keywords.html#//apple_ref/doc/uid/TP40000983-CH222-SW2) lists the keywords of the AppleScript language, provides a brief description for each, and points to related information.
* [Error Numbers and Error Messages](../reference/ASLR_error_codes.html#//apple_ref/doc/uid/TP40000983-CH220-SW5) describes error numbers and error messages you may see in working with AppleScript scripts.
* [Working with Errors](../reference/ASLR_error_xmpls.html#//apple_ref/doc/uid/TP40000983-CH221-SW1) provides detailed examples of handling errors with [try Statements](../reference/ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-128973) and [error Statements](../reference/ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-129657).
* [Double Angle Brackets](../conceptual/ASLR_raw_data.html#//apple_ref/doc/uid/TP40000983-CH225-SW1) describes when you are likely to see double angle brackets (or chevrons—`«»`) in scripts and how you can work with them.
* [Libraries using Load Script](../reference/ASLR_load_script.html#//apple_ref/doc/uid/TP40000983-CH227-SW1) describes how to save libraries of handlers and access them from other scripts.
* [Unsupported Terms](../reference/ASLR_unsupported_terms.html#//apple_ref/doc/uid/TP40000983-CH224-SW1) lists terms that are no longer supported in AppleScript.

<a id="//apple_ref/doc/uid/TP40000983-CH208-38112"></a>

## Conventions Used in This Guide

<a id="//apple_ref/doc/uid/TP40000983-CH208-DontLinkElementID_521"></a>Glossary terms are shown in *boldface* where they are defined.

> <a id="//apple_ref/doc/uid/TP40000983-CH208-DontLinkElementID_15"></a>
>
> **Important:** This document sometimes uses the continuation character (¬) for sample statements that don’t fit on one line on a document page. It also uses the continuation character in some syntax statements to identify an item that, if included, must appear on the same line as the previous item. The continuation character itself is not a required part of the syntax—it is merely a mechanism for including multiple lines in one statement.

The following conventions are used in syntax descriptions:

|  |  |
| --- | --- |
| `language element` | Plain computer font indicates an element that you type exactly as shown. If there are special symbols (for example, `+` or `&`), you also type them exactly as shown.<a id="//apple_ref/doc/uid/TP40000983-CH208-DontLinkElementID_522"></a> |
| *placeholder* | Italic text indicates a placeholder that you replace with an appropriate value.<a id="//apple_ref/doc/uid/TP40000983-CH208-DontLinkElementID_523"></a> |
| [optional] | Brackets indicate that the enclosed language element or elements are optional.<a id="//apple_ref/doc/uid/TP40000983-CH208-DontLinkElementID_524"></a> |
| (a group) | Parentheses group elements together.  However, the parentheses shown in [Handler Syntax (Positional Parameters)](../reference/ASLR_handlers.html#//apple_ref/doc/uid/TP40000983-CH7g-166812) are part of the syntax. |
| [optional]... | Three ellipsis points (...) after a group defined by brackets indicate that you can repeat the group of elements within brackets 0 or more times.<a id="//apple_ref/doc/uid/TP40000983-CH208-DontLinkElementID_525"></a> |
| a \| b \| c | Vertical bars separate elements in a group from which you must choose a single element. The elements are often grouped within parentheses or brackets.<a id="//apple_ref/doc/uid/TP40000983-CH208-DontLinkElementID_526"></a><a id="//apple_ref/doc/uid/TP40000983-CH208-DontLinkElementID_527"></a> |
| Filenames shown in scripts | Most filenames shown in examples in this document include extensions, such as `rtf` for a TextEdit document. Use of extensions in scripts is generally dependent on the “Show all file extensions” setting in the Advanced pane of Finder Preferences.  To work with the examples on your computer, you may need to modify either that setting or the filenames. |

<a id="//apple_ref/doc/uid/TP40000983-CH208-DontLinkElementID_2"></a>

## See Also

These Apple documents provide additional information for working with AppleScript:

* See *Getting Started with AppleScript* for a guided quick start, useful to both scripters and developers.
* See *[AppleScript Overview](../../AppleScriptX/AppleScriptX.html#//apple_ref/doc/uid/10000156i)*, including the chapter [Scripting with AppleScript](../../AppleScriptX/Concepts/work_with_as.html#//apple_ref/doc/uid/TP40001568), for a high-level overview of AppleScript and its related technologies.
* See *Getting Started With Scripting & Automation* for information on the universe of scripting technologies available in macOS.
* See [AppleScript Terminology and Apple Event Codes](http://developer.apple.com/releasenotes/AppleScript/ASTerminology_AppleEventCodes/TermsAndCodes.html) for a list of many of the scripting terms defined by Apple.

For additional information on working with the AppleScript language and creating scripts, see one of the comprehensive third-party documents available in bookstores and online.

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
