# Scripting Bridge

Scripting Bridge, introduced in OS X version 10.5, provides an automated process for creating an Objective-C interface to scriptable applications. This allows Cocoa applications and other Objective-C code to efficiently access features of scriptable applications, using native Objective-C syntax. Some other scripting languages, such as Ruby and Python, can use also Scripting Bridge (they also have open-source software bridges to scriptable applications—RubyOSA and py-appscript). For more information, see *[Ruby and Python Programming Topics for Mac](../../../../Cocoa/Conceptual/RubyPythonCocoa/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004936)*.

To use Scripting Bridge, you add the Scripting Bridge framework to your application project and use command-line tools to generate the interface files for the scriptable application you want to target. Then in your application code, you obtain a reference to an application object for the targeted scriptable application and send Objective-C messages to it.

For details, see *[Scripting Bridge Programming Guide](../../../../Cocoa/Conceptual/ScriptingBridgeConcepts/Introduction/Introduction.html#//apple_ref/doc/uid/TP40006104)* and *[Scripting Bridge Framework Reference](https://developer.apple.com/documentation/scriptingbridge)*. For related sample code, see *[ScriptingBridgeFinder](../../../../../samplecode/ScriptingBridgeFinder/Introduction/Intro.html#//apple_ref/doc/uid/DTS10004283)*.

  

---

Copyright © 2002, 2007 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2007-10-31
