<a id="//apple_ref/doc/uid/TP40000983-CH218-SW2"></a>

# AppleScript Fundamentals

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_275"></a>This chapter describes basic concepts that underlie the terminology and rules covered in the rest of this guide.

* [Script Editor Application](#//apple_ref/doc/uid/TP40000983-CH218-SW36)
* [AppleScript and Objects](#//apple_ref/doc/uid/TP40000983-CH218-SW1)
* [Object Specifiers](#//apple_ref/doc/uid/TP40000983-CH218-SW7)
* [Coercion (Object Conversion)](#//apple_ref/doc/uid/TP40000983-CH218-SW21)
* [Scripting Additions](#//apple_ref/doc/uid/TP40000983-CH218-SW3)
* [Commands Overview](#//apple_ref/doc/uid/TP40000983-CH218-SW8)
* [AppleScript Error Handling](#//apple_ref/doc/uid/TP40000983-CH218-SW10)
* [Global Constants in AppleScript](#//apple_ref/doc/uid/TP40000983-CH218-BAJBDEJI)
* [The it and me Keywords](#//apple_ref/doc/uid/TP40000983-CH218-SW4)
* [Aliases and Files](#//apple_ref/doc/uid/TP40000983-CH218-SW28)
* [Remote Applications](#//apple_ref/doc/uid/TP40000983-CH218-SW9)
* [Debugging AppleScript Scripts](#//apple_ref/doc/uid/TP40000983-CH218-SW20)

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW36"></a>

## Script Editor Application

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_276"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_277"></a>The Script Editor application is located in `/Applications/Utilities`. It provides the ability to edit, compile, and execute scripts, display application scripting terminologies, and save scripts in a variety of formats, such as compiled scripts, applications, and plain text.

Script Editor can display the result of executing an AppleScript script and can display a log of the Apple events that are sent during execution of a script. In the Script Editor Preferences, you can also choose to keep a history of recent results or event logs.

Script Editor has text formatting preferences for various types of script text, such as language keywords, comments, and so on. You can also turn on or off the Script Assistant, a code completion tool that can suggest and fill in scripting terms as you type. In addition, Script Editor provides a contextual menu to insert many types of boilerplate script statements, such as conditionals, comments, and error handlers.

A *dictionary* <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_278"></a>is the part of a scriptable application that specifies the scripting terms it understands. You can choose File &gt; Open Dictionary in Script Editor to display the dictionary<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_279"></a> of a scriptable application or scripting addition on your computer. Or you can drag an application icon to the Script Editor icon to display its dictionary (if it has one).

To display a list that includes just the scriptable applications and scripting additions provided by macOS, choose Window &gt; Library. Double-click an item in the list to display its dictionary. Figure 2-1 shows the dictionary for the Finder application in OS X v10.5. The dictionary is labeled as “Finder.sdef”. The sdef format, along with other terminology formats, is described in “Specifying Scripting Terminology” in *[AppleScript Overview](../../AppleScriptX/AppleScriptX.html#//apple_ref/doc/uid/10000156i)*.

<a id="//apple_ref/doc/uid/TP40000983-CH218-1153023-BBCCDDAF"></a>

<a id="//apple_ref/doc/uid/TP40001568-1153023"></a>**Figure 2-1**  The Finder dictionary in Script Editor (in OS X v10.5)

![The Finder dictionary in Script Editor (in OS X v10.5)](../Art/finder_dictionary_2x.png)![The Finder dictionary in Script Editor (in OS X v10.5)](../Art/finder_dictionary_2x.png)

There are also third-party editors for AppleScript.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW1"></a>

## AppleScript and Objects

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_280"></a>AppleScript is an object-oriented language. When you write, compile, and execute scripts, everything you work with is an object. An *object* is an instantiation of a class definition, which can include properties and actions. AppleScript defines classes for the objects you most commonly work with, starting with the top-level `script` object, which is the overall script you are working in.

Within in a `script` object, you work with other objects, including:

* AppleScript objects:

  AppleScript defines classes for boolean values, scripts, text, numbers, and other kinds of objects for working in scripts; for a complete list, see [Class Reference](../reference/ASLR_classes.html#//apple_ref/doc/uid/TP40000983-CH1g-246384).
* macOS objects:

  Scriptable parts of macOS and applications distributed with it, such as Finder, System Events, and Database Events (located in `/System/Library/CoreServices`), define many useful classes.
* Application objects:

  Third-party scriptable applications define classes that support a wide variety of features.

The following sections provide more detail about objects:

* [What Is in a Script Object](#//apple_ref/doc/uid/TP40000983-CH218-SW15)
* [Properties](#//apple_ref/doc/uid/TP40000983-CH218-SW5)
* [Elements](#//apple_ref/doc/uid/TP40000983-CH218-SW14)

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW15"></a>

### What Is in a Script Object

When you enter AppleScript statements in script window in Script Editor, you are working in a top-level `script` object. All `script` object definitions follow the same syntax, except that a top-level `script` object does not have statements marking its beginning and end.

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_281"></a>A `script` object can contain the following:

* Property definitions (optional):

  A property is a labeled container in which to store a value.
* An explicit `run` handler (optional):

  A `run` handler contains statements AppleScript executes when the script is run. (For more information, see [run Handlers](ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-SW15).)
* An implicit `run` handler (optional):

  An implicit `run` handler consists of any statements outside of any contained handlers or `script` objects.
* Additional handlers (optional):

  A handler is the equivalent of a subroutine. (For details, see [About Handlers](ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-CJBIDBJH).)
* Additional `script` objects (optional):

  A `script` object can contain nested `script` objects, each of which is defined just like a top-level `script` object, except that a nested `script` object is bracketed with statements that mark its beginning and end. (For details, see [Script Objects](ASLR_script_objects.html#//apple_ref/doc/uid/TP40000983-CH207-BAJJCIAA).)

Here is an example of a simple script with one property, one handler, one nested `script` object, and an implicit `run` handler with two statements:

```
property defaultClientName : "Mary Smith"
 
on greetClient(nameOfClient)
    display dialog ("Hello " & nameOfClient & "!")
end greetClient
 
script testGreet
    greetClient(defaultClientName)
end script
 
run testGreet --result: "Hello Mary Smith!"
greetClient("Joe Jones") --result: "Hello Joe Jones!"
```

The first statement in the `run` handler is `run testGreet`, which runs the nested `script` object `testGreet`. That `script` object calls the handler `greetClient()`, passing the property `defaultClientName`. The handler displays a dialog, greeting the default client, Mary Smith.

The second statement in the `run` handler calls `greetClient()` directly, passing the string `"Joe Jones"`.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW5"></a>

### Properties

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_282"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_283"></a>A *property* of an object is a characteristic that has a single value and a label, such as the `name` property of a window or the `month` property of a date. The definition for any AppleScript class includes the name and class for each of its properties. Property names must be unique within a class. Property values can be read/write or read only.

The AppleScript `date` class, for example, defines both read/write and read only properties. These include the `weekday` property, which is read only, and the `month`, `day`, and `year` properties, which are read/write. That’s because the value of the `weekday` property depends on the other properties—you can’t set an arbitrary weekday for an actual date.

The class of a property can be a simple class such as `boolean` or `integer`, a composite class such as a `point` class (made up of two integers), or a more complex class.

Most classes only support predefined properties. However, for the `script` class, AppleScript lets you to define additional properties. For information on how to do this, see [Defining Properties](ASLR_variables.html#//apple_ref/doc/uid/TP40000983-CH223-SW2). You can also define properties for `record` objects.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW14"></a>

### Elements

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_284"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_285"></a>An *element* is an object contained within another object. The definition for any AppleScript class includes the element types it can contain. An object can typically contain zero or more of each of its elements.

For a given element type, an object can contain many elements or none, and the number of elements that it contains may change over time. For example, it is possible for a `list` object to contain no items (it can be an empty list). At a later time, the same list might contain many items.

Whether you can add elements to or remove elements from an object depends on the class and the element. For example, a `text` object is immutable—you cannot add or remove text once the object is created. For a `list` object, you cannot remove items, but you can use the `set` command to add an item to the beginning or end:

```
set myList to {1, "what", 3} --result: {1, "what", 3}
set beginning of myList to 0
set end of myList to "four"
myList --result: {0, 1, "what", 3, "four"}
```

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW7"></a>

## Object Specifiers

An *object specifier*<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_286"></a> specifies the information needed to find another object in terms of the objects in which it is contained. An object specifier can refer to an application object, such as a window or file, or to an AppleScript object, such as an item in a list or a property in a record.

An object specifier is fully evaluated (or resolved) only when a script is run, not when it is compiled. A script can contain a valid object specifier (such as `third document of application "TextEdit"` that causes an error when the script is executed (because, for example, there may be less than three documents open).

Applications typically return object specifiers in response to commands. For example, if you ask the Finder for a window, it returns information that specifies the window object your script asked for (if it exists). The top-level container in an object specifier is typically the application itself.

You create an object specifier every time your script uses a phrase that describes the path to an object or property, such as `name of window 1 of application "Finder"`. When you use the `a reference to` operator, it creates a `reference` object that wraps an object specifier.

The difference between an object specifier and the object it refers to is like the difference between a building address and the building itself. The address is a series of words and numbers, such as “2121 Oak Street, San Francisco, CA” that identifies a location (on a street, in a city, in a state). It is distinct from the building itself. If the building at that location is torn down and replaced with a new building, the address remains the same.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW23"></a>

### What Is in an Object Specifier

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_287"></a>An object specifier describes an object type, a location, and how to distinguish the object from other objects of the same type in that location. These three types of information—the type, or class; the location, or container; and the distinguishing information, or reference form—allow you to specify any object.

In the following example, the class of the object is `paragraph`. The container is the phrase `of document 1`. Because this phrase is inside a `tell` statement, the `tell` statement provides the top-level container, `of application "TextEdit"`. The distinguishing information (the reference form) is the combination of the class, `paragraph`, and an index value, `1`, which together indicate the first paragraph.

```
tell application "TextEdit"
    paragraph 1 of document 1
end tell
```

> <a id="//apple_ref/doc/uid/TP40000983-CH218-SW39"></a>
>
> **Note:** If you examine the dictionary for the TextEdit application, you might think this script should say `paragraph 1 of text of document 1`. However, where the meaning is unambiguous, some applications make life easier for scripters by allowing them to omit a container from an object specifier. TextEdit uses this feature in supplying an <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_288"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_289"></a>*implicitly specified subcontainer* for the text in a document. That is, if an object specifier identifies an object, such as a word or paragraph, that is contained in a document’s text, TextEdit automatically supplies the `of text` part of the object specifier.

In addition to the index reference form, you can specify objects in a container by name, by range, by ID, and by the other forms described in [Reference Forms](../reference/ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-120522).

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW24"></a>

### Containers

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_290"></a>A container is an object that contains one or more objects or properties. In an object specifier, a container specifies where to find an object or a property. To specify a container, use the word `of` or `in`, as in the following statement (from a Finder `tell` block):<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_291"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_292"></a>

```
folder "Applications" of startup disk
```

A container can be an object or a series of objects, listed from the innermost to the outermost containing object, as in the following:

```
tell application "Finder"
    first item of first folder of first disk
end tell
```

You can also use the possessive form (`'s`) to specify containers. In the following example, the innermost container is `first window` and the object it contains is a `name` property:<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_293"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_294"></a>

```
tell application "TextEdit"
    first window's name
end tell
```

In this example, the target of the `tell` statement (`"TextEdit"`) is the outer container for the object specifier.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW25"></a>

### Absolute and Relative Object Specifiers

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_295"></a>An <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_296"></a>*absolute object specifier* has enough information to identify an object or objects uniquely. It can be used unambiguously anywhere in a script. For a reference to an application object to be absolute, its outermost container must be the application itself, as in:

```
version of application "Finder" --result: "10.5.1"
```

In contrast, <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_297"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_298"></a>a *relative object specifier* does not specify enough information to identify an object or objects uniquely; for example:

```
name of item 1 of disk 2
```

When AppleScript encounters a relative object specifier in a `tell` statement, it attempts to use the default target specified by the statement to complete the object specifier. Though it isn’t generally needed, this implicit target can be specified explicitly using the keyword `it`, which is described in [The it and me Keywords](#//apple_ref/doc/uid/TP40000983-CH218-SW4).

The default target of a `tell` statement is the object that receives commands if no other object is specified. For example, the following `tell` statement tells the Finder to get a name using the previous relative object specifier.

```
tell application "Finder"
    name of item 1 of disk 2
end tell
```

When AppleScript encounters a relative object specifier outside any `tell` statement, it tries to complete the object specifier by looking up the inheritance chain described in [Inheritance in Script Objects](ASLR_script_objects.html#//apple_ref/doc/uid/TP40000983-CH207-SW5).

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW27"></a>

### Object Specifiers in Reference Objects

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_299"></a>When you can create a `reference` object with the <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_300"></a>`a reference to` operator, it contains an object specifier. For example:

```
tell application "TextEdit"
    set docRef to a reference to the first document
    --result: document 1 of application "TextEdit"
        -- an object specifier
    name of docRef --result: "New Report.rtf"
        -- name of the specified object
end tell
```

In this script, the variable `docRef` is a reference whose object specifier refers to the first document of the application TextEdit—which happens to be named “New Report.rtf” in this case. However, the object that `docRef` refers to can change. If you open a second TextEdit document called “Second Report.rtf” so that its window is in front of the previous document, then run this script again, it will return the name of the now-frontmost document, “Second Report.rtf”.

You could instead create a reference with a more specific object specifier:

```
tell application "TextEdit"
    set docRef to a reference to document "New Report.rtf"
    --result: document "New Report.rtf" of application "TextEdit"
    name of docRef --result: "New Report.rtf"
end tell
```

If you run this script after opening a second document, it will still return the name of the original document, “New Report.rtf”, if the document exists.

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_301"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_302"></a>After you create a `reference` object with the `a reference to` operator, you can use the `contents` property to get the value of the object that it refers to. That is, using the `contents` property causes the reference’s object specifier to be evaluated. In the following script, for example, the content of the variable `myWindow` is the window reference itself.<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_303"></a>

```
set myWindow to a ref to window "Q1.rtf" of application "TextEdit"
myWindow
    -- result: window "Q1.rtf" of application "TextEdit" (object specifier)
contents of myWindow
    --result: window id 283 of application "TextEdit" (an evaluated window)
get myWindow
    -- result: window "Q1.rtf" of application "TextEdit" (object specifier)
```

Note that the result of the `get` command is to return the reference’s object specifier, not to resolve the specifier to the object it specifies.

When it can, AppleScript will implicitly dereference a reference object (without use of the `contents` property), as in the following example:

```
set myWindow to a ref to window 1 of application "TextEdit"
name of myWindow --result: "Q1.rtf" (if that is the first window's name)
```

For related information, see the Discussion section for the `reference` class.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW21"></a>

## Coercion (Object Conversion)

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_304"></a>*Coercion* (also known as <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_305"></a>*object conversion*) is the process of converting objects from one class to another. AppleScript converts an object to a different class in either of these circumstances:

* in response to the `as` operator<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_306"></a>
* automatically, when an object is of a different class than was expected for a particular command or operation

Not all classes can be coerced to all other class types. Table 2-1 summarizes the coercions that AppleScript supports for commonly used classes. For more information about each coercion, see the corresponding class definition in [Class Reference](../reference/ASLR_classes.html#//apple_ref/doc/uid/TP40000983-CH1g-246384).

AppleScript provides many coercions, either as a built-in part of the language or through the Standard Additions scripting addition. You can use these coercions outside of a `tell` block in your script. However, coercion of application class types may be dependent on the application and require a `tell` block that targets the application.

The `as` operator specifies a specific coercion or set of coercions. For example, the following statement coerces the integer `2` into the text `"2"` before storing it in the variable `myText`:

```
set myText to 2 as text
```

If you provide a command parameter or operand of the wrong class, AppleScript automatically coerces the operand or parameter to the expected class, if possible. If the conversion can’t be performed, AppleScript reports an error.

When coercing `text` strings to values of class `integer`, `number`, or `real`, or vice versa, AppleScript uses the current Numbers settings in the Formats pane in International preferences to determine what separators to use in the string. When coercing strings to values of class `date` or vice versa, AppleScript uses the current Dates settings in the Formats pane.<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_307"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW12"></a>

**Table 2-1**  Default coercions supported by AppleScript

| Convert from class | To class | Notes |
| `alias` | `list` (single-item)  `text` |  |
| `application` | `list` (single-item) | This is both an AppleScript class and an application class. |
| `boolean` | `integer`  `list` (single-item)  `text` |  |
| `class` | `list` (single-item)  `text` |  |
| `constant` | `list` (single-item)  `text` |  |
| `date` | `list` (single-item)  `text` |  |
| `file` | `list` (single-item)  `text` |  |
| `integer` | `list` (single-item)  `real`  `text` | Coercing an `integer` to a `number` does not change its class. |
| `list` (single-item) | any class to which the item can be coerced if it is not part of a list |  |
| `list` (multiple-item) | `text`, if each of the items in the list can be coerced to a `text` object |  |
| `number` | `integer`  `list` (single-item)  `real`  `text` | Values identified as values of class `number` are really values of either class `integer` or class `real`. |
| `POSIX file` | see `file` | `POSIX file` is a pseudo-class equivalent to the `file` class. |
| `real` | `integer`  `list` (single-item) | In coercing to `integer`, any fractional part is rounded.  Coercing a `real` to a `number` does not change its class. |
| `record` | `list` | All labels are lost in the coercion and the resulting list cannot be coerced back to a record. |
| `reference` | any class to which the referenced object can be coerced |  |
| `script` | `list` (single-item) |  |
| `text` | `integer`  `list` (single-item)  `real` | Can coerce to `integer` or `real` only if the `text` object represents an appropriate number. |
| `unit types` | `integer`  `list` (single-item)  `real`  `text` | Can coerce between unit types in the same category, such as `inches` to `kilometers` (length) or `gallons` to `liters` (liquid volume). |

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW3"></a>

## Scripting Additions

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_308"></a>A *scripting addition* is a file or bundle that provides handlers you can use in scripts to perform commands and coercions.

Many of the commands described in this guide are defined in the Standard Additions scripting addition in macOS. These commands are stored in the file `StandardAdditions.osax` in `/System/Library/ScriptingAdditions`, and are available to any script. You can examine the terminology for the Standard Additions by opening this file in Script Editor.

> <a id="//apple_ref/doc/uid/TP40000983-CH218-SW19"></a>
>
> **Note:** A script can obtain the location of the Standard Additions with this script statement, which uses the `path to (folder)` command:
>
> ```
> path to scripting additions as text
>     --result: "Hard_Disk:System:Library:ScriptingAdditions:"
> ```

Scripting additions can be embedded within bundled script applets by placing them in a folder named `Scripting Additions` (note the space between “Scripting” and “Additions”) inside the bundle’s `Contents/Resources/` folder. Note that Script Editor does not look for embedded scripting additions when editing bundled applets. During script development, any required scripting additions must be properly installed in `/System/ScriptingAdditions`, `/Library/ScriptingAdditions`, or `~/Library/ScriptingAdditions` so that Script Editor can find them.

Developers can create their own scripting additions, as described in Technical Note TN1164, *[Scripting Additions for Mac OS X](../../../../../technotes/tn1164/_index.html#//apple_ref/doc/uid/DTS10003003)*. For related conceptual information, see *[AppleScript Overview](../../AppleScriptX/AppleScriptX.html#//apple_ref/doc/uid/10000156i)*, particularly the section “Extending AppleScript with Coercions, Scripting Additions, and Faceless Background Applications” in the chapter [Open Scripting Architecture](../../AppleScriptX/Concepts/osa.html#//apple_ref/doc/uid/TP40001571).

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW8"></a>

## Commands Overview

A *command* is a word or a series of words used in AppleScript statements to request an action. Every command is directed at a *target*, which is the object that responds to the command. The target is often an *application object*<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_309"></a> (one that is stored in an application or its documents and managed by the application, such as a window or document) or an object in macOS. However, it can also be a `script` object or a value in the current script.

Commands often return results. For example, the `display dialog` command returns a record that may contain text, a button name, and other information. Your script can examine this record to determine what to do next. You can assign the result of a command to a variable you define, or access it through the predefined AppleScript `result` variable.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW26"></a>

### Types of Commands

Scripts can make use of the following kinds of commands:

* <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_310"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_311"></a>An *AppleScript command* is one that is built into the AppleScript language. There currently are five such commands: `get` , `set`, `count`, `copy`, and `run`. Except for `copy` , each of these commands can also be implemented by applications. That is, there is an AppleScript version of the command that works on AppleScript objects, but an application can define its own version that works on the object types it defines.
* <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_312"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_313"></a>A *scripting addition command* is one that is implemented through the mechanism described in [Scripting Additions](#//apple_ref/doc/uid/TP40000983-CH218-SW3)). Although anyone can create a scripting addition (see Technical Note TN1164, *[Scripting Additions for Mac OS X](../../../../../technotes/tn1164/_index.html#//apple_ref/doc/uid/DTS10003003)*), this guide documents only the scripting addition commands from the Standard Additions, supplied by Apple as part of macOS. These commands are available to all scripts.
* <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_314"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_315"></a>A *user-defined command* is one that is implemented by a handler defined in a `script` object. To invoke a user-defined command outside of a `tell` statement, simply use its name and supply values for any parameters it requires. The command will use the current script as its target.

  To invoke a user-defined command inside a `tell` statement, see [Calling Handlers in a tell Statement](ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-SW1).
* <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_316"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_317"></a>An *application command* is one that is defined by scriptable application to provide access to a scriptable feature. They are typically enclosed in a `tell` statement that targets the application. You can determine which commands an application supports by examining its dictionary in Script Editor.

  Scriptable applications that ship with macOS, such as the Finder and System Events applications (located in `/System/Library/CoreServices`), provide many useful scripting commands.

  Third-party scriptable applications also provide commands you can use in scripts. Many support all or a subset of the Standard commands, described in Technical Note TN2106, *[Scripting Interface Guidelines](../../../../../technotes/tn2002/tn2106.html#//apple_ref/doc/uid/DTS10003199)*. These include commands such as `delete`, `duplicate`, `exists`, and `move`, as well as application implementations of AppleScript commands, such as `get` and `set`.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW18"></a>

### Target

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_318"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_319"></a>There are two ways to explicitly specify an object as the target of a command: by supplying it as the direct parameter of the command (described in the next section) or by specifying it as the target of a `tell` statement that contains the command. If a script doesn’t explicitly specify the target with a `tell` statement, and it isn’t handled by a handler in the script or by AppleScript itself, it is sent to the next object in the inheritance chain (see [The AppleScript Inheritance Chain](ASLR_script_objects.html#//apple_ref/doc/uid/TP40000983-CH207-SW15)).

In the following script, the target of the `get` command is the object specifier `name of first window`. Because the enclosing `tell` statement specifies the Finder application, the full specifier is `name of first window of application "Finder"`, and it is the Finder application which obtains and returns the requested information.

```
tell application "Finder"
    get name of first window
end tell
```

When a command targets an application, the result may be an application object. If so, subsequent statements that target the result object are sent to the application.

A script may also implicitly specify a target by using an application command imported using a `Note` statement. For example, the `extract address` command in the following script targets the Mail application because the command was imported from Mail:

```
use application "Mail"
extract address from "John Doe &lt;jdoe@example.com&gt;"
```

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW13"></a>

### Direct Parameter

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_320"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_321"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_322"></a>The *direct parameter* is a value, usually an object specifier, that appears immediately next to a command and specifies the target of the command. Not all commands have a direct parameter. If a command can have a direct parameter, it is noted in the command’s definition.

In the following statement, the object specifier `last file of window 1 of application "Finder"` is the direct parameter of the `duplicate` command:

```
duplicate last file of window 1 of application "Finder"
```

The direct parameter usually appears immediately after the command, but may also appear immediately before it. This can be easier to read for some commands, such as `exists` in this example:

```
if file "semaphore" of application "Finder" exists then
   -- continue processing...
end if
```

A `tell` statement specifies a default target for all commands contained within it, so the direct parameter is optional. The following example has the same result as the previous example:<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_323"></a>

```
tell last file of window 1 of application "Finder"
    duplicate
end tell
```

<a id="//apple_ref/doc/uid/TP40000983-CH218-BAJHBFBA"></a>

### Parameters That Specify Locations

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_324"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_325"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_326"></a>Many commands have parameters that specify locations. A location can be either an insertion point or another object. An *insertion point* is a location where an object can be added.<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_327"></a>

In the following example, the `to` parameter specifies the location to which to move the first paragraph. The value of the `to` parameter of the `duplicate` command is the relative object specifier `before paragraph 4`, which is an insertion point. AppleScript completes the specifier with the target of the `tell` statement, `front document of application "TextEdit"`.

```
tell front document of application "TextEdit"
    duplicate paragraph 1 to before paragraph 4
end tell
```

The phrases `paragraph 1` and `before paragraph 4` are called index and relative references, respectively. For more information, see [Reference Forms](../reference/ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-120522).

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW10"></a>

## AppleScript Error Handling

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_328"></a>During script execution, errors may occur due to interaction with macOS, problems encountered in an application script command, or problems caused by statements in the script itself. When an error occurs, AppleScript stops execution at the current location, signals an error, and looks up the calling chain for script statements that can handle the error. That is, it looks for the nearest error-handling code block that surrounds the location where the error occurred.

Scripts can handle errors by enclosing statements that may encounter an error within a `try` statement. The `try` statement includes an `on error` section that is invoked if an error occurs. AppleScript passes information about the error, including an error number and an error message, to the `on error` section. This allows scripts to examine the error number and to display information about it.

If the error occurs within a handler that does not provide a `try` statement, AppleScript looks for an enclosing `try` statement where the handler was invoked. If none of the calls in the call chain is contained in a `try` statement, AppleScript stops execution of the script and displays an error message (for any error number other than -128, described below).

A script can use an `error` statement to signal an error directly. Doing so invokes the AppleScript error handling mechanism, which looks for an enclosing `try` statement to handle the error.

Some “errors” are the result of the normal operation of a command. For example, commands such as `display dialog` and `choose file` signal <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_329"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_330"></a>`error –128` (User canceled), if the user clicks the Cancel button. Scripts routinely handle the user canceled error to ensure normal operation. For an example of how to do this, see the Examples section for the `display dialog` command. If no `try` statement in a script handles the -128 error, AppleScript halts execution of the script without displaying any error message.<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_331"></a>

For related information, see [Results](ASLR_lexical_conventions.html#//apple_ref/doc/uid/TP40000983-CH214-SW19), [error Statements](../reference/ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-129657), [try Statements](../reference/ASLR_control_statements.html#//apple_ref/doc/uid/TP40000983-CH6g-128973), [Error Numbers and Error Messages](../reference/ASLR_error_codes.html#//apple_ref/doc/uid/TP40000983-CH220-SW5), and [Working with Errors](../reference/ASLR_error_xmpls.html#//apple_ref/doc/uid/TP40000983-CH221-SW1).

<a id="//apple_ref/doc/uid/TP40000983-CH218-BAJBDEJI"></a>

## Global Constants in AppleScript

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_332"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_333"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_334"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_335"></a>AppleScript defines a number of global constants that you can use anywhere in a script.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW38"></a>

### AppleScript Constant

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_336"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_337"></a>The global constant `AppleScript` provides access to properties you can use throughout your scripts.

You can use the `AppleScript` identifier itself to distinguish an AppleScript property from a property of the current target with the same name, as shown in the section [version](#//apple_ref/doc/uid/TP40000983-CH218-SW6).

The following sections describe additional properties of `AppleScript`.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW29"></a>

#### pi

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_338"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_339"></a>This `mathematical` value represents the ratio of a circle's circumference to its diameter. It is defined as a real number with the value 3.14159265359.

For example, the following statement computes the area of a circle with radius 7:

```
set circleArea to pi * 7 * 7 --result: 153.9380400259
```

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW40"></a>

#### result

When a statement is executed, AppleScript stores the resulting value, if any, in the predefined property <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_340"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_341"></a>`result`. The value remains there until another statement is executed that generates a value. Until a statement that yields a result is executed, the value of `result` is undefined. You can examine the result in Script Editor by looking in the Result pane of the script window.<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_342"></a>

> <a id="//apple_ref/doc/uid/TP40000983-CH218-SW43"></a>
>
> **Note:** When an error occurs during script execution, AppleScript signals an error. It doesn’t return error information in the `result` property. For more information, see [AppleScript Error Handling](#//apple_ref/doc/uid/TP40000983-CH218-SW10).

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW30"></a>

#### Text Constants

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_343"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_344"></a>AppleScript defines the text properties `space`, `tab`, `return`, `linefeed`, and `quote`. You effectively use these properties as text constants to represent white space or a double quote (`"`) character. They are described in the Special String Characters section of the `text` class.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW22"></a>

#### text item delimiters

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_345"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_346"></a>AppleScript provides the `text item delimiters` property for use in processing text. This property consists of a list of strings used as delimiters by AppleScript when it coerces a list to text or gets text items from text strings. When getting `text items` of text, all of the strings are used as separators. When coercing a list to text, the first item is used as a separator.

> <a id="//apple_ref/doc/uid/TP40000983-CH218-SW45"></a>
>
> **Note:** Prior to OS X Snow Leopard v10.6, AppleScript only used the first delimiter in the list when getting `text items`.

Because `text item delimiters` respect `considering` and `ignoring` attributes in AppleScript 2.0, delimiters are case-insensitive by default. Formerly, they were always case-sensitive. To enforce the previous behavior, add an explicit `considering case` statement.

You can get and set the current value of the `text item delimiters` property. Normally, AppleScript doesn’t use any delimiters. For example, if the text delimiters have not been explicitly changed, the statement

```
{"bread", "milk", "butter", 10.45}  as string
```

returns the following:

```
"breadmilkbutter10.45"
```

For printing or display purposes, it is usually preferable to set `text item delimiters` to something that’s easier to read. For example, the script

```
set AppleScript's text item delimiters to {", "}
{"bread", "milk", "butter", 10.45}  as string
```

returns this result:

```
"bread, milk, butter, 10.45"
```

The `text item delimiters` property can be used to extract individual names from a pathname. For example, the script

```
set AppleScript's text item delimiters to {":"}
get last text item of "Hard Disk:CD Contents:Release Notes"
```

returns the result `"Release Notes"`.

If you change the `text item delimiters` property in Script Editor, it remains changed until you restore its previous value or until you quit Script Editor and launch it again. If you change `text item delimiters` in a script application, it remains changed in that application until you restore its previous value or until the script application quits; however, the delimiters are not changed in Script Editor or in other script applications you run.

Scripts commonly use an error handler to reset the `text item delimiters` property to its former value if an error occurs (for more on dealing with errors, see [AppleScript Error Handling](#//apple_ref/doc/uid/TP40000983-CH218-SW10)):

```
set savedDelimiters to AppleScript's text item delimiters
try
    set AppleScript's text item delimiters to {"**"}
    --other script statements...
    --now reset the text item delimiters:
    set AppleScript's text item delimiters to savedDelimiters
on error m number n
    --also reset text item delimiters in case of an error:
    set AppleScript's text item delimiters to savedDelimiters
    --and resignal the error:
    error m number n
end try
```

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW6"></a>

#### version

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_347"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_348"></a>This property provides the current version of AppleScript. The following script shows how to check for a version greater than or equal to version 1.9. The `if` statement is wrapped in a `considering numeric strings` statement so that an AppleScript version such as `1.10.6` compares as larger than, say, version `1.9`.

```
considering numeric strings
    if version of AppleScript as string ≥ "1.9" then
        -- Perform operations that depend on version 1.9 or greater
    else
        -- Handle case where version is not high enough
    end if
end considering
```

Applications can have their own `version` property, so to access the AppleScript version explicitly, you use the phrase `version of AppleScript`. This will work inside a `tell` block that targets another application, such as the following:

```
tell application "Finder"
    version --result: "10.5.1"
    version of AppleScript --result: "2.0"
end tell
```

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW41"></a>

### current application Constant

The <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_349"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_350"></a>`current application` constant refers to the application that is executing the current AppleScript script (for example, Script Editor). Because the current application is the parent of AppleScript <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_351"></a>(see [The AppleScript Inheritance Chain](ASLR_script_objects.html#//apple_ref/doc/uid/TP40000983-CH207-SW15)), it gets a chance to handle commands that aren’t handled by the current script or by AppleScript.

The `current application` constant is an object specifier—if you ask AppleScript for its value, the result is the object specifier:

```
get current application --result: current application
```

However, if you ask for `name of current application`, AppleScript resolves the object specifier and returns the current application’s name:

```
name of current application --result: "Script Editor"
```

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW44"></a>

### missing value Constant

The <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_352"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_353"></a>`missing value` constant is a placeholder for missing or uninitialized information.

For example, the following statements use the `missing value` constant to determine if a variable has changed:

```
set myVariable to missing value
    -- perform operations that might change the value of myVariable
if myVariable is equal to missing value then
    -- the value of the variable never changed
else
    -- the value of the variable did change
end if
```

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW42"></a>

### true, false Constants

AppleScript defines the <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_354"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_355"></a>Boolean constants <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_356"></a>`true` and <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_357"></a>`false`. These constants are described with the `boolean` class.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW4"></a>

## The it and me Keywords

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_358"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_359"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_360"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_361"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_362"></a>AppleScript defines the keyword `me` to refer to the current script and the keyword `it` to refer to the current target. (The <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_363"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_364"></a>*current script* is the one that is currently being executed; the <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_365"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_366"></a>*current target* is the object that is the current default target for commands.) It also defines `my` as a synonym for `of me` and `its`<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_367"></a> as a synonym for `of it`.

If a script hasn’t targeted anything, `it` and `me` refer to the same thing—the script—as shown in the following example:

```
-- At the top-level of the script:
me --result: «script» (the top-level script object)
it --result: «script» (same as it, since no target set yet)
```

A `tell` statement specifies a default target. In the following example, the default target is the Finder application:

```
-- Within a tell block:
tell application "Finder" -- sets target
    me --result: «script» (still the top-level script object)
    it --result: application "Finder" (target of the tell statement)
end tell
```

You can use the words `of me` or `my` to indicate that the target of a command is the current script and not the target of the `tell` statement. In the following example, the word `my` indicates that `minimumValue()` handler is defined by the script, not by Finder:

```
tell application "Finder"
    set fileCount to count files in front window
    set myCount to my minimumValue(fileCount, 100)
    --do something with up to the first 100 files…
end tell
```

You can also use `of me` or `my` to distinguish script properties from object properties. Suppose there is a TextEdit document open named “Simple.rtf”:

```
tell document 1 of application "TextEdit"
    name --result: "Simple.rtf" (implicitly uses target of tell)
    name of it --result: "Simple.rtf" (specifies target of tell)
    me --result: «script» (top-level script object, not target of tell)
end tell
```

The following example shows how to specify different `version` properties in a Finder `tell` statement. The Finder is the default target, but using `version of me`, `my version`, or `version of AppleScript` allows you to specify the version of the top-level `script` object. (The top-level `script` object returns the AppleScript version, because it inherits from AppleScript, as described in [The AppleScript Inheritance Chain](ASLR_script_objects.html#//apple_ref/doc/uid/TP40000983-CH207-SW15).)

```
tell application "Finder"
    version --result: "10.5.1" (Finder version is the default in tell block)
    its version --result: "10.5.1" (specifically asks for Finder version)
    version of me --result: "2.0" (AppleScript version)
    my version --result: "2.0" (AppleScript version)
    version of AppleScript --result: "2.0" (AppleScript version)
end tell
```

For information on using `it` in a filter reference, see the Discussion section for the [Filter](../reference/ASLR_reference_forms.html#//apple_ref/doc/uid/TP40000983-CH4g-BAJJHEFE) reference form.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW28"></a>

## Aliases and Files

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_368"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_369"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_370"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_371"></a>To refer to items and locations in the macOS file system, you use `alias` objects and `file` objects.

An `alias` object is a dynamic reference to an existing file system object. Because it is dynamic, it can maintain the link to its designated file system object even if that object is moved or renamed.

A `file` object represents a specific file at a specific location in the file system. It can refer to an item that does not currently exist, such as the name and location for a file that is to be created. A `file` object is not dynamic, and always refers to the same location, even if a different item is moved into that place. The `POSIX file` pseudo-class is roughly synonymous with file: `POSIX file` specifiers evaluate to a `file` object, but they use different semantics for the name, as described in [Specifying Paths](#//apple_ref/doc/uid/TP40000983-CH218-SW11).

The following is the recommended usage for these types:

* Use an `alias` object to refer to existing file system objects.
* Use a `file` object to refer to a file that does not yet exist.
* Use a `POSIX file` specifier if you want to specify the file using a POSIX path.

The following sections describe how to specify file system objects by path and how to work with them in your scripts.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW11"></a>

### Specifying Paths

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_372"></a>You can create `alias` objects and `file` objects by supplying a name specifier, where the name is the path to an item in the file system.

For alias and file specifiers, the path is an HFS path, which takes the form `"disk:item:subitem:subsubitem:...:item"`. For example, `"Hard_Disk:Applications:Mail.app"` is the HFS path to the Mail application, assuming your boot drive is named `"Hard_Disk"`.

HFS paths with a leading colon, such as `":folder:file"`, are resolved relative to the HFS working directory. However, their use is discouraged, because the location of the HFS working directory is unspecified, and there is no way to control it from AppleScript.

For POSIX file specifiers, the path is a POSIX path, which takes the form `"/item/subitem/subsubitem/.../item"`. The disk name is not required for the boot disk. For example, `"/Applications/Mail.app"` is the POSIX path to the Mail application. You can see the POSIX path of an item in Finder in the "Where" field of its Get Info window. Despite the name, POSIX file specifiers may refer to folders or disks. Use of `"~"` to specify a home directory is not supported.

POSIX paths without a leading slash, such as `"folder/file"`, are resolved relative to the POSIX working directory. This is supported, but only is useful for scripts run from the shell—the working directory is the current directory in the shell. The location of the POSIX working directory for applications is unspecified.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW33"></a>

### Working With Aliases

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_373"></a>AppleScript defines the `alias` class to represent aliases. An alias can be stored in a variable and used throughout a script.

The following script first creates an alias to an existing file in the variable `notesAlias`, then uses the variable in a `tell` statement that opens the file. It uses a `try` statement to check for existence of the alias before creating it, so that the alias is only created once, even if the script is run repeatedly.

```
try
    notesAlias -- see if we've created the alias yet
on error
    -- if not, create it in the error branch
    set notesAlias to alias "Hard_Disk:Users:myUser:Feb_Notes.rtf"
end try
-- now open the file from the alias:
tell application "TextEdit" to open notesAlias
```

Finding the object an alias refers to is called *resolving* an alias. AppleScript 2.0 attempts to resolve aliases only when you run a script. However, in earlier versions, AppleScript attempts to resolve aliases at compile time.

Once you run the previous example, creating the alias, the script will be able to find the original file when you run it again, even if the file’s name or location changes. (However, if you run the script again after recompiling it, it will create a new alias.)

You can get the HFS path from an alias by coercing it to text:

```
notesAlias as text --result: "Hard_Disk:Users:myUser:Feb_Notes.rtf"
```

You can use the `POSIX path` property to obtain a POSIX-style path to the item referred to by an alias:

```
POSIX path of notesAlias --result: "/Feb_Notes.rtf"
```

If an alias doesn’t refer to an existing file system object then it is broken. You can’t create an alias to an object that doesn’t exist, such as a file you plan to create. For that you use a `file` object, described in the next section.

For a sample script that shows how a script application can process a list of aliases it receives when a user drops one or more file icons on it, see [open Handlers](ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-SW16).

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW31"></a>

### Working With Files

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_374"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_375"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_376"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_377"></a>AppleScript uses `file` objects to represent files in scripts. A `file` object can be stored in a variable and used throughout a script. The following script first creates a `file` object for an existing file in the variable `notesFile`, then uses the variable in a `tell` statement that opens the file:

```
set notesFile to POSIX file "/Users/myUser/Feb_Meeting_Notes.rtf"
tell application "TextEdit" to open notesFile
```

You can use a `file` object to specify a name and location for a file that may not exist:

```
set newFile to POSIX file "/Users/myUser/BrandNewFile.rtf"
```

Similarly, you can let a user specify a new file with the `choose file name` command, then use the returned `file` object to create the file. In the following example, if the user cancels the `choose file name` dialog, the rest of the script is not executed. If the user does supply a file name, the script opens the file, creating it if necessary, then uses a `try` statement to make sure it closes the file when it is finished writing to it.

```
set theFile to choose file name
set referenceNumber to open for access theFile with write permission
try
    -- statements to write to the file
on error
    close access referenceNumber
end try
close access referenceNumber
```

Typically, when you pass a `file` object to a command that uses it to operate on a new or existing item in the file system, the components of the path must exist for the command to succeed.<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_378"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_379"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_380"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW9"></a>

## Remote Applications

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_381"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_382"></a>A script can target an application on a remote computer if remote applications are enabled on that computer, and if the script specifies the computer with an eppc-style specifier.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW34"></a>

### Enabling Remote Applications

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_383"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_384"></a>For a script to send commands to a remote application, the following conditions must be satisfied:

* The computer that contains the application and the computer on which the script is run must be connected to each other through a network.
* Remote Apple Events (set in the Sharing preferences pane) must be enabled on the remote computer and user access must be provided (you can allow access for all users or for specified users only).
* If the specified remote application is not running, you must run it.
* You must authenticate as admin when you compile or run the script.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW37"></a>

### eppc-Style Specifiers

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_385"></a>An eppc-style specifier takes the following format:

```
eppc://[user[:password]@]IP_address
```

`ip_address`
:   <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_386"></a>Either a numeric IP address in dotted decimal form (four numbers, from 0 to 255, separated by periods; for example, `123.23.23.123`) or a hostname. A hostname can be a Bonjour name.

The following are examples of valid eppc-style specifiers. If you supply the user name and password, no authentication is required. If you do not supply it, authentication may be required.

```
"eppc://myCoolMac.local" -- hostname, no user or pwd
"eppc://myUserName:pwd@myCoolMac.local" -- user, pwd, and hostname
"eppc://123.23.23.123" -- IP address, no user or pwd
"eppc://myUserName:pwd@123.23.23.123" -- user, pwd, and IP address
"eppc://myUserName@server.company.com" -- server address, user
```

> <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_9"></a>
>
> **Important:** If a part of the eppc-style specifier contains non-UTF-8 characters or white space, it must be URL-encoded: for example, here is a user name that contains a space:
>
> `John%20Smith`.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW35"></a>

### Targeting Remote Applications

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_387"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_388"></a>You can target an application that is running on a remote machine and you can launch applications on remote machines that are not currently running.

The following example uses an eppc-style specifier to target the Finder on a remote computer. It includes a user name and password, so no authentication is required.

```
set remoteMachine to "eppc://userName:pwd@MacName.local"
tell app "Finder" of machine remoteMachine to close front window
```

> <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_10"></a>
>
> **Important:** If you compile an erroneous eppc-style address, you will have to quit and relaunch Script Editor for changes to that address to take effect.

In some cases, you’ll need to use a `using terms from` statement to tell AppleScript to compile against the local version of an application. The following example uses that technique in telling the remote Finder application to open the TextEdit application:

```
set remoteFinder to application "Finder" of machine ¬
    "eppc://myUserName:pwd@123.23.23.123"
 
using terms from application "Finder"
    tell remoteFinder
        open application file id "com.apple.TextEdit"
    end tell
end using terms from
```

If you omit the password (`pwd`) in the previous script, you will have to authenticate when you run the script.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW20"></a>

## Debugging AppleScript Scripts

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_389"></a>AppleScript does not include a built-in debugger, but it does provide several simple mechanisms to help you debug your scripts or just observe how they are working.

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW16"></a>

### Feedback From Your Script

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_390"></a>You can insert various statements into a script to indicate the current location and other information. In the simplest case, you can insert a beep command in a location of interest:

```
beep 3 -- three beeps; a very important part of the script!
```

A `display dialog` command can display information about what’s happening in a script and, like a breakpoint, it halts execution until you dismiss it (or until it times out, depending on the parameters you pass). The following example displays the current script location and the value of a variable:

```
display dialog "In factorial routine; x = " & (x as string)
```

The `say` command can get your attention by speaking the specified text. In the following example, `currentClient` is a `text` object that stores a client name:

```
say "I'm in the clientName handler. The client is " & currentClient
```

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW17"></a>

### Logging

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_391"></a><a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_392"></a>Script Editor can display a log of the Apple events that are sent during execution of a script. In the Script Editor Preferences, you can also choose to keep a history of recent results or event logs.

In addition, you can insert `log` statements into a script. Log output is shown in the Event Log pane of a script window, and also in the <a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_393"></a>Event Log History window, if it is open.

The following simple example logs the current word in a `repeat with loopVariable (in list)` statement:

```
set wordList to words in "Where is the hammer?"
repeat with currentWord in wordList
    log currentWord
    if contents of currentWord is equal to "hammer" then
        display dialog "I found the hammer!"
    end if
end repeat
```

The following shows how the words appear in the log when the script is run:

```
    (*Where*)
    (*is*)
    (*the*)
    (*hammer*)
```

<a id="//apple_ref/doc/uid/TP40000983-CH218-SW32"></a>

### Third Party Debuggers

<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_394"></a>If you need full-featured debugging capabilities, there are powerful, third-party AppleScript debuggers available.<a id="//apple_ref/doc/uid/TP40000983-CH218-DontLinkElementID_395"></a>

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
