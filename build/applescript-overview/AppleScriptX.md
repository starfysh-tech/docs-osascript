# Introduction to AppleScript Overview

> **Important:** This document is no longer being updated. For the latest information about Apple SDKs, visit the [documentation website](https://developer.apple.com/documentation).

*AppleScript Overview* provides a high-level overview of AppleScript and its related technologies to help you determine where you can use them in your work.

> **Note:** For information on the universe of scripting technologies available on OS X, see *Getting Started With Scripting & Automation*.

AppleScript is a scripting language that makes possible direct control of scriptable applications and of many parts of the Mac OS. A scriptable application is one that makes its operations and data available in response to AppleScript messages, called Apple events.

With scriptable applications, users can write scripts to automate operations, while developers can use AppleScript as an aid to rapid prototyping and automated testing. Developers can also use technologies including Apple events, AppleScript, Automator, and Scripting Bridge, to take advantage of services provided by other applications and by the Mac OS.

AppleScript and Apple events are based on the Open Scripting Architecture, which is implemented by several OS X frameworks. Apple provides a number of additional applications and technologies that enhance AppleScript or take advantage of its features.

## Who Should Read This Document

You should read *AppleScript Overview* to get a broad understanding of AppleScript and related automation technologies, and to determine where they fit into your development process.

This document may also be of interest if you write AppleScript scripts and would like to know more about the technology behind them.

*AppleScript Overview* is intended for a general developer audience, but experience with some kind of scripting language is helpful. If you are starting from scratch, see *Getting Started with AppleScript*.

## Organization of This Document

This document contains the following:

* [About AppleScript](Concepts/ScriptingOnOSX.md#//apple_ref/doc/uid/20000032-BABEBGCF) introduces AppleScript, describes when you might use it, and notes some limitations.
* [Open Scripting Architecture](Concepts/osa.md#//apple_ref/doc/uid/TP40001571-BABEBGCF) describes the underlying technology used to implement AppleScript and Apple events. It also describes how to extend AppleScript.
* [Scripting with AppleScript](Concepts/work_with_as.md#//apple_ref/doc/uid/TP40001568-BABEBGCF) provides a brief description of how you work with AppleScript scripts. It also describes options for combining AppleScript scripting with other kinds of scripting.
* [Scriptable Applications](Concepts/scriptable_apps.md#//apple_ref/doc/uid/TP40001569-BABEBGCF) explains how scriptable applications work, including how they specify their scripting terminology, and describes the programming resources available for creating scriptable applications.
* [Scripting Bridge](Concepts/scripting_bridge.md#//apple_ref/doc/uid/TP40006467-SW1) describes a technology available starting in OS X version 10.5 that generates Objective-C API for accessing scriptable applications.
* [Automator](Concepts/automator.md#//apple_ref/doc/uid/TP40006469-SW1) describes Apple’s graphical automation program and how developers can take advantage of it.
* [AppleScript Utilities and Applications](Concepts/as_related_apps.md#//apple_ref/doc/uid/TP40001570-BABEBGCF) describes utilities and applications that work with AppleScript or provide additional features you can use in AppleScript scripts.

## See Also

You can find additional introductory information on AppleScript and related technologies in *Getting Started with AppleScript*.

There are also links to related documentation throughout *AppleScript Overview*.

  

---

Copyright © 2002, 2007 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2007-10-31
