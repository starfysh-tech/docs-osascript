<a id="//apple_ref/doc/uid/20000032-BABEBGCF"></a>

# About AppleScript

*AppleScript* is a scripting language that provides direct control of scriptable applications and scriptable parts of the Mac OS. A *scriptable application* is one that can respond to a variety of Apple events by performing operations or supplying data. An *Apple event* is a type of interprocess message that can encapsulate commands and data of arbitrary complexity. By providing an API that supports these mechanisms, the [Open Scripting Architecture](osa.html#//apple_ref/doc/uid/TP40001571-BABEBGCF) makes possible one of the most powerful features in OS X—the ability to write scripts that automate operations with multiple applications.

You can use AppleScript scripts to perform repetitive tasks, automate complex workflows, control applications on local or remote computers, and access web services. Because script writers (or scripters) can access features in any scriptable application, they can combine features from many applications. For example, a script might make remote procedure calls to a web service to get stock quotes, add the current stock prices to a database, then graph information from the database in a spreadsheet application. From controlling an image-processing workflow to performing quality assurance testing for a suite of applications, AppleScript makes automation possible.

While the AppleScript scripting language (described in [AppleScript Language Guide](http://developer.apple.com/documentation/AppleScript/Conceptual/AppleScriptLangGuide/index.html), and in a number of detailed third-party books) uses an English-like terminology which may appear simple, it is a rich, object-oriented language, capable of performing complicated programming tasks. However, its real strength comes from providing access to the features available in scriptable applications. If you make your application scriptable, it will help scripters get their work done, and quite likely become indispensable to their work process.

The [Automator](automator.html#//apple_ref/doc/uid/TP40006469-SW1) application, available starting in OS X version 10.4, lets users work in a graphical interface to put together complex, automated workflows. Workflows consist of one or more actions, which are provided by Apple, by developers, and by scripters, and can be written in AppleScript and in other languages, including Objective-C. Starting in OS X v10.5, developers can incorporate workflows directly in their applications, providing another mechanism for accessing features of other applications and the Mac OS.

[Scripting Bridge](scripting_bridge.html#//apple_ref/doc/uid/TP40006467-SW1), available starting in OS X version 10.5, provides an automated process for creating an Objective-C interface to scriptable applications. This allows Cocoa applications and other Objective-C code to efficiently access features of scriptable applications, using native Objective-C syntax. Some other scripting languages, such as Ruby and Python, can use Scripting Bridge, but also have their own software bridges to access features of scriptable applications—for more information, see *Getting Started With Scripting & Automation*.

AppleScript has several other new or improved features in OS X v10.5, including full support for Unicode text, additional support for identifying and working with application objects in scripts, 64-bit support, more accurate and useful error messages, and additional scriptability in Apple technologies such as iChat and the Dock. For more information, see [AppleScript Features](http://www.macosxautomation.com/applescript/features/unicode.html).

<a id="//apple_ref/doc/uid/20000032-1173352"></a><a id="//apple_ref/doc/uid/20000032-1173352-BABIFHCE"></a>

## When to Use AppleScript

The following are common scenarios in which you might use AppleScript or related technologies in your development work.

* You’re creating or updating an application for OS X and you want it to be scriptable. As a scriptable application, users can invoke it in their AppleScript scripts and you can write scripts to perform automated testing during development. You can also make the application accessible to Automator users, or access it through Apple’s Scripting Bridge, or through open source bridge technologies, using languages such as Objective-C, Ruby, and Python.

  For information on these technologies, see [Scriptable Applications](scriptable_apps.html#//apple_ref/doc/uid/TP40001569-BABEBGCF), [Scripting Bridge](scripting_bridge.html#//apple_ref/doc/uid/TP40006467-SW1), and [Automator](automator.html#//apple_ref/doc/uid/TP40006469-SW1) in this document and the related learning paths in *Getting Started With Scripting & Automation* and *Getting Started with AppleScript*.

  “Framework and Language Support,” in [About Apple Events](../../AppleEvents/about_aes_aepg/about_aes_aepg.html#//apple_ref/doc/uid/TP40001449-CH202) in *[Apple Events Programming Guide](../../AppleEvents/intro_aepg/intro_aepg.html#//apple_ref/doc/uid/TP40001449)*, describes trade-offs involved in developing scriptable applications in procedural and object-oriented languages, and in using support provided by the Carbon APIs or the Cocoa application framework.
* You’re interested in automating repetitive operations, whether in development or in other work, using scripts or [Automator](automator.html#//apple_ref/doc/uid/TP40006469-SW1) workflows.

  For information on working with scripts, see [Scripting with AppleScript](work_with_as.html#//apple_ref/doc/uid/TP40001568-BABEBGCF) in this document, as well the learning paths in *Getting Started with AppleScript*.

  To learn about applications and technologies that extend AppleScript and help it work with graphic images, XML, property lists, databases, and other technologies, see [AppleScript Utilities and Applications](as_related_apps.html#//apple_ref/doc/uid/TP40001570-BABEBGCF).

<a id="//apple_ref/doc/uid/20000032-1151403"></a>

## Limitations of AppleScript

The AppleScript scripting language excels in its ability to call on multiple applications, but was not designed to perform task-specific functions itself. So, for example, you cannot use AppleScript to efficiently perform intensive math operations or lengthy text processing. However, you can use AppleScript in combination with shell scripts, Perl scripts, and other scripting languages. This allows you to work with the most efficient language for the task at hand. For related information, see [Using AppleScript with Other Scripting Systems](work_with_as.html#//apple_ref/doc/uid/TP40001568-1152618).

AppleScript relies on developers to build scriptability into their applications. However, a mechanism called GUI scripting, introduced with OS X version 10.3, does allow some scripting of applications that do not contain code for responding to Apple events. For more information, see [System Events and GUI Scripting](as_related_apps.html#//apple_ref/doc/uid/TP40001570-1149074).

  

---

Copyright © 2002, 2007 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2007-10-31
