<a id="//apple_ref/doc/uid/TP40006469-SW1"></a>

# Automator

Automator is a workflow automation application, first available in OS X version 10.4. Automator, which is located in `/Applications`, lets you create complex workflows using a graphical interface that does not require any knowledge of scripting languages. A workflow consists of one or more actions, executed sequentially, with each action typically taking the output of the previous action as its input. An action performs a distinct operation, such as copying a file, cropping a photo, or sending an email message. You can run a workflow in Automator or save it as a standalone application.

Starting in OS X version 10.5, you can also embed and execute Automator workflows in your application.

Automator includes actions for many Apple applications, including Finder, Mail, Safari, Xcode, iPhoto, iTunes, and QuickTime Player, and you can write actions that make features of your applications available in Automator. You use Xcode and Interface Builder to put together actions, using the Action project template (also available starting in OS X v10.4). Actions are implemented as plug-ins and you can write them using AppleScript (for scriptable applications) or Objective-C.

> <a id="//apple_ref/doc/uid/TP40006469-SW2"></a>
>
> **Note:** If your application is scriptable, other developers and users can write actions for it. However, by supplying actions yourself, you can be sure to make your application look its best in Automator.

For information on using the Automator application, choose Help in Automator or Help > Mac Help in the Finder and search for “Automator”. For information on creating actions, see *[Automator Programming Guide](https://developer.apple.com/library/archive/../../AppleApplications/Conceptual/AutomatorConcepts/Automator.html#//apple_ref/doc/uid/TP40001450)* and *[Automator Framework Reference](https://developer.apple.com/documentation/automator)*. For information on using workflows in your application, see *[Automation Release Notes for OS X v10.7](https://developer.apple.com/library/archive/../../../releasenotes/AppleApplications/RN-Automator/index.html#//apple_ref/doc/uid/TP40001840)*, as well as the class descriptions for `AMWorkflow`, `AMWorkflowView`, and `AMWorkflowController` in *[Automator Framework Reference](https://developer.apple.com/documentation/automator)*

  

---

Copyright © 2002, 2007 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2007-10-31
