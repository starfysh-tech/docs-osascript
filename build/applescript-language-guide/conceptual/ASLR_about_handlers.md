<a id="//apple_ref/doc/uid/TP40000983-CH206-CJBIDBJH"></a>

# About Handlers

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_229"></a>When script developers want to factor and re-use their code, they can turn to handlers. A handler is a collection of statements that can be invoked by name. Handlers are also known as functions, subroutines, or methods.

This chapter describes how to work with handlers, in the following sections:

* [Handler Basics](#//apple_ref/doc/uid/TP40000983-CH206-SW3)
* [Handlers in Script Applications](#//apple_ref/doc/uid/TP40000983-CH206-SW14)

For detailed reference information, see [Handler Reference](../reference/ASLR_handlers.md#//apple_ref/doc/uid/TP40000983-CH7g-163762).

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW3"></a>

## Handler Basics

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_230"></a>A *handler* is a collection of statements that can be invoked by name. Handlers are useful in scripts that perform the same action in more than one place. You can package statements that perform a specific task as a handler, give it a descriptive name, and call it from anywhere in the script. This makes the script shorter and easier to maintain.

A script can contain one or more handlers. However, you can not nest a handler definition within another handler (although a script object defined in a handler can contain other handlers).

The definition for a handler specifies the parameters it uses, if any, and may specify a class or classes for the parameter and a default value.

When you call a handler, you must list its parameters according to how they are specified in its definition. Handlers may have labeled, positional, or interleaved parameters, described in subsequent sections. If a parameter has a specified class, AppleScript will coerce the actual value to that class as if using the `as` operator. If a parameter has a default value, that parameter may be omitted.

A handler definition can contain variable declarations and statements. It may use a `return` statement (described in detail in `return`) to return a value and exit the handler<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_231"></a>.

The sections that follow provide additional information on working with handlers:

* [Defining a Simple Handler](#//apple_ref/doc/uid/TP40000983-CH206-SW23)
* [Handlers with Labeled Parameters](#//apple_ref/doc/uid/TP40000983-CH206-SW22)
* [Handlers with Positional Parameters](#//apple_ref/doc/uid/TP40000983-CH206-SW13)
* [Handlers with Patterned Positional Parameters](#//apple_ref/doc/uid/TP40000983-CH206-SW20)
* [Recursive Handlers](#//apple_ref/doc/uid/TP40000983-CH206-SW11)
* [Errors in Handlers](#//apple_ref/doc/uid/TP40000983-CH206-SW10)
* [Passing by Reference Versus Passing by Value](#//apple_ref/doc/uid/TP40000983-CH206-SW4)
* [Calling Handlers in a tell Statement](#//apple_ref/doc/uid/TP40000983-CH206-SW1)

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW23"></a>

### Defining a Simple Handler

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_232"></a>The following is a definition for a simple handler that takes any parameter value that can be displayed as text (presumably one representing a date) and displays it in a dialog box. The handler name is `rock`; its parameter is `around the clock`, where `around` is a parameter label and `clock` is the parameter name (`the` is an AppleScript filler for readability):

```
on rock around the clock
    display dialog (clock as text)
end rock
```

This handler allows an English-like calling statement:

```
rock around the current date -- call handler to display current date
```

A handler can have no parameters. To indicate that a handler has no parameters, you include a pair of empty parentheses after the handler name in both the handler definition and the handler call. For example, the following `helloWorld` script has no parameters.<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_233"></a>

```
on helloWorld()
    display dialog "Hello World"
end
 
helloWorld() -- Call the handler
```

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW22"></a>

### Handlers with Labeled Parameters

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_234"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_235"></a>To define a handler with labeled parameters, you list the labels to use when calling the handler and the statements to be executed when it is called. (The syntax is shown in [Handler Syntax (Labeled Parameters)](../reference/ASLR_handlers.md#//apple_ref/doc/uid/TP40000983-CH7g-SW2).)

Handlers with labeled parameters can also have a direct parameter. With the exception of the direct parameter, which must directly follow the handler name, labeled parameters can appear in any order, with the labels from the handler definition identifying the parameter values. This includes parameters listed in `given`, `with`, and `without` clauses (of which there can be any number).

The `findNumbers` handler in the following example uses the special label `given` to define a parameter with the label `given rounding`.

```
to findNumbers of numberList above minLimit given rounding:roundBoolean
        set resultList to {}
        repeat with i from 1 to (count items of numberList)
            set x to item i of numberList
            if roundBoolean then -- round the number
                -- Use copy so original list isn’t modified.
                copy (round x) to x
            end if
            if x > minLimit then
                set end of resultList to x
            end if
        end repeat
        return resultList
end findNumbers
```

The next statements show how to call `findNumbers` by passing a predefined `list` variable:

```
set myList to {2, 5, 19.75, 99, 1}
findNumbers of myList above 19 given rounding:true
    --result: {20, 99}
findNumbers of myList above 19 given rounding:false
    --result: {19.75, 99}
```

You can also specify the value of the `rounding` parameter by using a `with` or `without` clause to indicate `true` or `false`. (In fact, when you compile the previous examples, AppleScript automatically converts `given rounding:true` to `with rounding` and `given rounding:false` to `without rounding`.) These examples pass a `list` object directly, rather than using a `list` variable as in the previous case:

```
findNumbers of {5.1, 20.1, 20.5, 33} above 20 with rounding
    --result: {33}
 
findNumbers of {5.1, 20.1, 20.5, 33.7} above 20 without rounding
    --result: {20.1, 20.5, 33.7}
```

Here is another handler that uses parameter labels:

```
to check for yourNumber from startRange thru endRange
    if startRange ≤ yourNumber and yourNumber ≤ endRange then
        display dialog "Congratulations! Your number is included."
    end if
end check
```

The following statement calls the handler, causing it to display the `"Congratulations!"` message

```
check for 8 from 7 thru 10 -- call the handler
```

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW13"></a>

### Handlers with Positional Parameters

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_236"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_237"></a>The definition for a handler with positional parameters shows the order in which to list parameters when calling the handler and the statements to be executed when the handler is called. The definition must include parentheses, even if it doesn’t include any parameters. The syntax is shown in [Handler Syntax (Positional Parameters)](../reference/ASLR_handlers.md#//apple_ref/doc/uid/TP40000983-CH7g-166812).

In the following example, the `minimumValue` routine returns the smaller of two values:

```
on minimumValue(x, y)
    if x < y then
        return x
    else
        return y
    end if
end minimumValue
 
-- To call minimumValue:
minimumValue(5, 105) --result: 5
```

The first line of the `minimumValue` handler specifies the parameters of the handler. To call a handler with positional parameters you list the parameters in the same order as they are specified in the handler definition.

If a handler call is part of an expression, AppleScript uses the value returned by the handler to evaluate the expression. For example, to evaluate the following expression, AppleScript first calls `minimumValue`, then evaluates the rest of the expression.

```
minimumValue(5, 105) + 50 --result: 55
```

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW20"></a>

### Handlers with Patterned Positional Parameters

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_238"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_239"></a>You can create a handler whose positional parameters define a pattern to match when calling the handler. For example, the following handler takes a single parameter whose pattern consists of two items in a list:

```
on displayPoint({x, y})
    display dialog ("x = " & x & ", y = " & y)
end displayPoint
 
-- Calling the handler:
set testPoint to {3, 8}
displayPoint(testPoint)
```

A parameter pattern can be much more complex than a single list. The handler in the next example takes two numbers and a record whose properties include a list of bounds. The handler displays a dialog box summarizing some of the passed information.

```
on hello(a, b, {length:l, bounds:{x, y, w, h}, name:n})
    set q to a + b
 
    set response to "Hello " & n & ", you  are " & l & ¬
        " inches tall and occupy position (" & x &  ", " & y & ")."
 
    display dialog response
 
end hello
 
set thing to {bounds:{1, 2, 4, 5}, name:"George", length:72}
hello (2, 3, thing)
--result: A dialog displaying “Hello George, you are 72 inches  tall
--          and occupy position (1,2).”
```

The properties of a record passed to a handler with patterned parameters don’t have to be given in the same order in which they are given in the handler’s definition, as long as all the properties required to fit the pattern are present.

The following call to `minimumValue` uses the value from a handler call to `maximumValue` as its second parameter. The `maximumValue` handler (not shown) returns the larger of two passed numeric values.

```
minimumValue(20, maximumValue(1, 313)) --result: 20
```

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW2"></a>

### Handlers with Interleaved Parameters

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_240"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_241"></a>A handler with interleaved parameters is a special case of one with positional parameters. The definition shows the order in which to list parameters when calling the handler and the statements to be executed when the handler is called, but the name of the handler is broken into pieces and interleaved with the parameters, which can make it easier to read. Handlers with interleaved parameters may be used in any script, but are especially useful with bridged Objective-C methods, since they naturally resemble Objective-C syntax. The syntax is shown in [Handler Syntax (Interleaved Parameters)](../reference/ASLR_handlers.md#//apple_ref/doc/uid/TP40000983-CH7g-SW4).

A handler with interleaved parameters may have only one parameter, as in this example:

```
on areaOfCircleWithRadius:radius
    return radius ^ 2 * pi
end areaOfCircleWithRadius:
```

Or more than one, as in this example:

```
on areaOfRectangleWithWidth:w height:h
    return w * h
end areaOfRectangleWithWidth:height:
```

To call a handler with interleaved parameters, list the parameters in the same order as they are specified in the handler definition. Despite the resemblance to labeled parameters, the parameters may not be reordered. Also, the call must be explicitly sent to an object, even if the target object is the default, `it`. For example:

```
its foo:5 bar:105 --this works
tell it to foo:5 bar:105 --as does this
foo:5 bar:105 --syntax error.
```

> <a id="//apple_ref/doc/uid/TP40000983-CH206-SW5"></a>
>
> **Note:** The actual name of an interleaved-parameter handler is all the name parts strung together with underscores, and is equivalent to a handler defined using that name with positional parameters. For example, these two handler declarations are equivalent:
>
> ```
> on tableView:t objectValueForTableColumn:c row:r
> on tableView_objectValueForTableColumn_row_(t, c, r)
> ```
>
> Given a compiled script, AppleScript will automatically translate between the two forms depending on whether or not the current system version supports interleaved parameters.

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW12"></a>

### Parameter Specifications

> <a id="//apple_ref/doc/uid/TP40000983-CH206-SW18"></a>
>
> **Note:** Parameter specifications are supported in OS X Yosemite v10.10 and later.

The parameter “name” in a handler definition may be a simple name, as shown above, or it may additionally specify a required class and, for labeled parameters, a default value. To specify a required class, follow the name with `as` *class* or `as {`*class*`,`…`}`. For example, you could declare a parameter to be specifically an integer like this:

```
on factorial(x as integer)
```

The effect is as if the handler began with `set x to x as integer`; if coercing the actual value to an integer fails, AppleScript throws an appropriate error, which may be caught with a `try` block. The class may be a list of classes, as described in [Operators Reference](../reference/ASLR_operators.md#//apple_ref/doc/uid/TP40000983-CH5g-124070).

Labeled parameters may be declared with a default value by following the formal parameter name with `:`*literal*. Doing so makes the parameter optional when called. For example, this declares a `make` handler with a default value for the `with data` parameter:

```
on make new theClass with data theData : missing value
```

This handler can now be called without supplying a `with data` parameter; the handler would see `theData` set to the specified default `missing value`, which it could then test for and handle appropriately.

A parameter may use both a type specification and a default value. For example, this declares a `make` handler with a `with properties` parameter that must be a record and has a default value of an empty record:

```
on make new theClass with properties theProperties as record : {}
```

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW11"></a>

### Recursive Handlers

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_242"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_243"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_244"></a>A *recursive handler* is a handler that calls itself. For example, this recursive handler generates a factorial. (The factorial of a number is the product of all the positive integers from 1 to that number. For example, 4 factorial is equal to 1 \* 2 \* 3 \* 4, or 24. The factorial of 0 is 1.)

```
on factorial(x)
    if x > 0 then
        return x * factorial(x - 1)
    else
        return 1
    end if
end factorial
 
-- To call factorial:
factorial(10)   --result: 3628800
```

In the example above, the handler `factorial` is called once, passing the value `10`. The handler then calls itself recursively with a value of `x - 1`, or `9`. Each time the handler calls itself, it makes another recursive call, until the value of `x` is `0`. When `x` is equal to `0`, AppleScript skips to the `else` clause and finishes executing all the partially executed handlers, including the original `factorial` call.

When you call a recursive handler, AppleScript keeps track of the variables and pending statements in the original (partially executed) handler until the recursive handler has completed. Because each call uses some memory, the maximum number of pending handlers is limited by the available memory. As a result, a recursive handler may generate an error before the recursive calls complete.

In addition, a recursive handler may not be the most efficient solution to a problem. For example, the factorial handler shown above can be rewritten to use a `repeat` statement instead of a recursive call, as shown in the example in `repeat with loopVariable (from startValue to stopValue)`.

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW10"></a>

### Errors in Handlers

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_245"></a>As with any AppleScript statements that may encounter an error, you can use a `try` statement to deal with possible errors in a handler. A `try` statement includes two collections of statements: one to be executed in the general case, and a second to be executed only if an error occurs.

By using one or more `try` statements with a handler, you can combine the advantages of reuse and error handling in one package. For a detailed example that demonstrates this approach, see [Working with Errors](../reference/ASLR_error_xmpls.md#//apple_ref/doc/uid/TP40000983-CH221-SW1).

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW4"></a>

### Passing by Reference Versus Passing by Value

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_246"></a>Within a handler, each parameter is like a variable, providing access to passed information. AppleScript passes all parameters by reference, which means that a passed variable is shared between the handler and the caller, as if the handler had created a variable using the `set` command. However, it is important to remember a point raised in [Using the copy and set Commands](ASLR_variables.md#//apple_ref/doc/uid/TP40000983-CH223-SW7): only mutable objects can actually be changed.

As a result, a parameter’s class type determines whether information is effectively passed by value or by reference:

* For mutable objects (those whose class is `date`, `list`, `record`, or `script`), information is passed *by reference*:

  If a handler changes the value of a parameter of this type, the original object is changed.
* For all other class types, information is effectively passed *by value*:

  Although AppleScript passes a reference to the original object, that object cannot be changed. If the handler assigns a new value to a parameter of this type, the original object is unchanged.

If you *want* to pass by reference with a class type other than `date`, `list`, `record`, or `script`, you can pass a `reference` object that refers to the object in question. Although the handler will have access only to a copy of the `reference` object, the specified object will be the same. Changes to the specified object in the handler will change the original object, although changes to the `reference` object itself will not.

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW1"></a>

### Calling Handlers in a tell Statement

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_247"></a>To call a handler from within a `tell` statement, you must use the reserved words `of me` or `my` to indicate that the handler is part of the script and not a command that should be sent to the target of the `tell` statement.<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_248"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_249"></a>

For example, the following script calls the `minimumValue` handler defined in [Handlers with Positional Parameters](#//apple_ref/doc/uid/TP40000983-CH206-SW13) from within a `tell` statement. If this call did not include the words `of me`, it would cause an error, because AppleScript would send the `minimumValue` command to TextEdit, which does not understand that message.

```
tell front document of application "TextEdit"
    minimumValue(12, 400) of me
    set paragraph 1 to result as text
end tell
--result: The handler call is successful.
```

Instead of using the words `of me`, you could insert the word `my` before the handler call:

```
my minimumValue(12, 400)
```

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW14"></a>

## Handlers in Script Applications

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_250"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_251"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_252"></a>A *script application* is an application whose only function is to run the script associated with it. Script applications contain handlers that allow them to respond to commands. For example, many script applications can respond to the `run` command and the `open` command. A script application receives a `run` command whenever it is launched and an `open` command whenever another icon is dropped on its icon in the Finder. It can also contain other handlers to respond to commands such as `quit` or `print`.

When saving a script in Script Editor, you can create a script application by choosing either Application or Application Bundle from the File Format options. Saving as Application results in a simple format that is compatible with Mac OS 9.<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_253"></a> Saving as Application Bundle results in an application that uses the modern bundle format, with its specified directory structure, which is supported back to OS X v10.3.<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_254"></a>

When creating a script application, you can also specify whether a <a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_255"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_256"></a>startup screen should appear before the application runs its script. Whatever you write in the Description pane of the script window in Script Editor is displayed in the startup screen. <a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_257"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_258"></a>You can also specify in Script Editor whether a script application should stay open after running. The default is for the script to quit immediately after it is run.

You can run a script application from the Finder much like any other application. If it has a startup screen, the user must click the Run button or press the Return key before the script actually runs.

Consider the following simple script

```
tell application "Finder"
    close front window
end tell
```

What this script does as a script application depends on what you specify when you save it. If you don’t specify a startup screen or tell it to stay open, it will automatically execute once, closing the front Finder window, and then quit.

If a script application modifies the value of a property, the changed value persists across launches of the application. For related information, see [Scope of Variables and Properties](ASLR_variables.md#//apple_ref/doc/uid/TP40000983-CH223-SW1).

For information about some common script application handlers, see the following sections:

* [run Handlers](#//apple_ref/doc/uid/TP40000983-CH206-SW15)
* [open Handlers](#//apple_ref/doc/uid/TP40000983-CH206-SW16)
* [idle and quit Handlers for Stay-Open Applications](#//apple_ref/doc/uid/TP40000983-CH206-SW7)

See [Handler Reference](../reference/ASLR_handlers.md#//apple_ref/doc/uid/TP40000983-CH7g-163762) for syntax information.

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW15"></a>

### run Handlers

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_259"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_260"></a>When you run a script or launch a script application, its `run` handler is invoked. A script’s `run` handler is defined in one of two ways:

* As an implicit `run` handler, which consists of all statements declared outside any handler or nested `script` object in a script.

  Declarations for properties and `global` variables are not considered statements in this context—that is, they are not considered to be part of an implicit `run` handler.
* As an explicit `run` handler, which is enclosed within `on run` and `end` statements, similar to other handlers.<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_261"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_262"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_263"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_264"></a>

Having both an implicit and an explicit `run` handler is not allowed, and causes a syntax error during compilation. If a script has no run handler (for example, a script that serves as a library of handlers, as described in [Parameter Specifications](#//apple_ref/doc/uid/TP40000983-CH206-SW12)), executing the script does nothing. However, sending it an explicit `run` command causes an error.

The following script demonstrates an implicit `run` handler. The script consists of a statement that invokes the `sayHello` handler, and the definition for the handler itself:

```
sayHello()
 
on sayHello()
    display dialog "Hello"
end sayHello
```

The implicit `run` handler for this script consists of the statement `sayHello()`, which is the only statement outside the handler. If you save this script as a script application and then run the application, the script receives a `run` command, which causes it to execute the one statement in the implicit `run` handler.

You can rewrite the previous script to provide the exact same behavior with an explicit `run` handler:

```
on run
    sayHello()
end run
 
on sayHello()
    display dialog "Hello"
end sayHello
```

Whether a script is saved as a script application or as a compiled script, its `run` handler is invoked when the script is run. You can also invoke a `run` handler in a script application from another script. For information about how to do this, see [Calling a Script Application From a Script](#//apple_ref/doc/uid/TP40000983-CH206-SW17).

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW16"></a>

### open Handlers

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_265"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_266"></a>Mac apps, including script applications, receive an `open` command whenever the user drops file, folder, or disk icons on the application’s Finder icon, even if the application is already running.

If the script in a script application includes an `open` handler, the handler is executed when the application receives the `open` command. The `open` handler takes a single parameter which provides a list of all the items to be opened. Each item in the list is an`alias` object.

For example, the following `open` handler makes a list of the pathnames of all items dropped on the script application’s icon and saves them in the frontmost TextEdit document:

```
on open names
    set pathNamesString to "" -- Start with empty text string.
    repeat with i in names
        -- In this loop, you can perform operations on each dropped item.
        -- For now, just get the name and append a return character.
        set iPath to (i as text)
        set pathNamesString to pathNamesString & iPath & return
    end repeat
    -- Store list in open document, to verify what was dropped.
    tell application "TextEdit"
        set paragraph 1 of front document to pathNamesString
    end tell
    return
end open
```

Files, folders, or disks are not moved, copied, or affected in any way by merely dropping them on a script application. However, the script application’s handler can tell Finder to move, copy, or otherwise manipulate the items. For examples that work with Finder items, see [Folder Actions Reference](../reference/ASLR_folder_actions.md#//apple_ref/doc/uid/TP40000983-CH219-SW2).

You can also run an `open` handler by sending a script application the `open` command. For details, see [Calling a Script Application From a Script](#//apple_ref/doc/uid/TP40000983-CH206-SW17).

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW7"></a>

### idle and quit Handlers for Stay-Open Applications

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_267"></a>By default, a script application that receives a `run` or `open` command handles that single command and then quits. In contrast, a stay-open script application (one saved as Stay Open in Script Editor) stays open after it is launched.

A stay-open script application can be useful for several reasons:

* Stay-open script applications can receive and handle other commands in addition to `run` and `open`. This allows you to use a script application as a script server that, when it is running, provides a collection of handlers that can be invoked by any other script.
* Stay-open script applications can perform periodic actions, even in the background, as long as the script application is running.

Two particular handlers that stay-open script applications often provide are an `idle` handler and a `quit` handler.

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW8"></a>

#### idle Handlers

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_268"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_269"></a>If a stay-open script application includes an `idle` handler, AppleScript sends the script application periodic `idle` commands—by default, every 30 seconds—allowing it to perform background tasks when it is not performing other actions.

If an `idle` handler returns a positive number, that number becomes the rate (in seconds) at which the handler is called. If the handler returns a non-numeric value, the rate is not changed. You can return 0 to maintain the default delay of 30 seconds.

For example, when saved as a stay-open application, the following script beeps every 5 seconds:

```
on idle
    beep
    return 5
end idle
```

The result returned from a handler is just the result of the last statement, even if it doesn’t include the word `return` explicitly. (See `return` for more information.) For example, this handler gets called once a minute, because the value of the last statement is 60:

```
on idle
    set x to 10
    beep
    set x to x * 6  -- The handler returns the result (60).
end idle
```

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW9"></a>

#### quit Handlers

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_270"></a><a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_271"></a>AppleScript sends a stay-open script application a `quit` command whenever the user chooses the Quit menu command or presses Command-Q while the application is active. If the script includes a `quit` handler, the statements in the handler are run before the application quits.

A `quit` handler can be used to set script properties, tell another application to do something, display a dialog box, or perform almost any other task. If the handler includes a `continue quit` statement, the script application’s default quit behavior is invoked and it quits. If the `quit` handler returns before it encounters a `continue quit` statement, the application doesn’t quit.

> <a id="//apple_ref/doc/uid/TP40000983-CH206-SW6"></a>
>
> **Note:** The `continue` statement passes control back to the application’s default `quit` handler. For more information, see `continue`.

For example, this handler checks with the user before allowing the application to quit:

```
on quit
    display dialog "Really quit?" ¬
        buttons {"No", "Quit"} default button  "Quit"
    if the button returned of the result is "Quit" then
        continue quit
    end if
    -- Without the continue statement, the application doesn't quit.
end quit
```

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_8"></a>

**Warning:** 
If AppleScript doesn’t encounter a `continue quit` statement while executing an `on quit` handler, it may seem to be impossible to quit the application. For example, if the handler shown above gets an error before the `continue quit` statement, the application won’t quit. If necessary, you can use Force Quit (Command-Option-Esc) to halt the application. <a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_272"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH206-SW17"></a>

## Calling a Script Application From a Script

<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_273"></a>A script can send commands to a script application just as it can to other applications. To launch a non-stay-open application and run its script, use a `launch` command followed by a `run` command, like this:

```
launch application "NonStayOpen"
run application "NonStayOpen"
```

The `launch` command launches the script application without sending it an implicit `run` command. When the `run` command is sent to the script application, it processes the command, sends back a reply if necessary, and quits.

Similarly, to launch a non-stay-open application and run its `stringTest` handler (which takes a `text` object as a parameter), use a `launch` command followed by a `stringTest` command, like this:

```
tell application "NonStayOpen"
    launch
    stringTest("Some example text.")
end tell
```

For information on how to create script applications, see [Handlers in Script Applications](#//apple_ref/doc/uid/TP40000983-CH206-SW14).<a id="//apple_ref/doc/uid/TP40000983-CH206-DontLinkElementID_274"></a>

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
