<a id="//apple_ref/doc/uid/TP40000983-CH7g-163762"></a>

# Handler Reference

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_926"></a>This chapter provides reference for handlers, which are defined and introduced in [About Handlers](../conceptual/ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-CJBIDBJH). It describes the types of parameters you can use with handlers and how you invoke them. It also describes the `continue` and `return` statements, which you use to control the flow of execution in handlers.

<a id="//apple_ref/doc/uid/TP40000983-CH7g-SW1"></a>

continue

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_927"></a>A `continue` statement causes AppleScript to invoke the handler with the same name in the parent of the current handler. If there is no such handler in the parent, AppleScript looks up the parent chain, ending with the current application.

A `continue` statement is like a handler call, in that after execution completes in the new location, it resumes with the statement after the `continue` statement.

##### Syntax

|  |
| --- |
| ``` continue handlerName [ parameterList ]  ``` |

##### Placeholders

*handlerName*
:   A required identifier that specifies the name of the current handler (which is also the name of the handler in which to continue execution).

*parameterList*
:   The list of parameters to be passed to *handlerName*. The list must follow the same format as the parameter definitions in the handler definition for the command. For handlers with labeled parameters, this means that the parameter labels must match those in the handler definition. For handlers with positional parameters, the parameters must appear in the correct order. You can list the parameter variables that were specified in the original command (and thus the original values) or you can list values that may differ from those of the original variables.<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_928"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_929"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_209"></a>

##### Examples

You can write a handler that overrides an AppleScript command but uses a `continue` statement to pass control on to the AppleScript command if desired:

```
on beep numTimes
    set x to display dialog "Start beeping?" buttons {"Yes", "No"}
    if button returned of x is "Yes" then ¬
        continue beep numTimes -- Let AppleScript handle the beep.
        -- In this example, nothing to do after returning from the continue.
end beep
 
beep 3 --result: local beep handler invoked; shows dialog before beeping
tell my parent to beep 3 -- result: AppleScript beep command invoked
```

When AppleScript encounters the statement `beep 3`, it invokes the local `beep` handler, which displays a dialog. If the user clicks Yes, the handler uses a `continue` statement to pass the `beep` command to the script’s parent (AppleScript), which handles the command by beeping. If the user clicks No, it does not continue the `beep` command, and no sound is heard.

The final statement, `tell my parent to beep 3`, shows how to directly invoke the AppleScript `beep` command, rather than the local handler.

For an example that uses a `continue` statement to exit a script handler and return control to the application’s default `quit` handler, see [quit Handlers](../conceptual/ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-SW9).

For additional examples, see [Using the continue Statement in Script Objects](../conceptual/ASLR_script_objects.html#//apple_ref/doc/uid/TP40000983-CH207-SW9).

<a id="//apple_ref/doc/uid/TP40000983-CH7g-163937"></a>

return

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_930"></a>A `return` statement exits a handler and optionally returns a specified value. Execution continues at the place in the script where the handler was called.<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_931"></a>

##### Syntax

|  |
| --- |
| ```  return [ expression ]  ``` |

##### Placeholders

*expression*
:   Represents the value to return.

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_210"></a>

##### Examples

The following statement, inserted in the body of a handler, returns the integer `2`:

```
return 2 -- returns integer value 2
```

If you include a `return` statement without an expression, AppleScript exits the handler immediately and no value is returned:

```
return -- no value returned
```

See other sections throughout [Handler Reference](#//apple_ref/doc/uid/TP40000983-CH7g-163762) for more examples of scripts that use the `return` statement.

##### Discussion

If a handler does not include a `return` statement, AppleScript returns the value returned by the last statement. If the last statement doesn’t return a value, AppleScript returns nothing.

When AppleScript has finished executing a handler (that is, when it executes a `return` statement or the last statement in the handler), it passes control to the place in the script immediately after the place where the handler was called. If a handler call is part of an expression, AppleScript uses the value returned by the handler to evaluate the expression.

It is often considered good programming practice to have just one `return` statement and locate it at the end of a handler. Doing so can provide the following benefits:

* The script is easier to understand.
* The script is easier to debug.
* You can place cleanup code in one place and make sure it is executed.

In some cases, however, it may make more sense to use multiple `return` statements. For example, the `minimumValue` handler in [Handler Syntax (Positional Parameters)](#//apple_ref/doc/uid/TP40000983-CH7g-166812) is a simple script that uses two `return` statements.

For related information, see [AppleScript Error Handling](../conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW10).

<a id="//apple_ref/doc/uid/TP40000983-CH7g-SW2"></a>

Handler Syntax (Labeled Parameters)

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_932"></a>A handler is a collection of statements that can be invoked by name. This section describes the syntax for handlers that use labeled parameters.

Labeled parameters are identified by their labels and can be listed in any order.

##### Syntax

|  |
| --- |
| ``` ( on \| to ) handlerName ¬    [ [ of \| in ] directParamName ] ¬    [ ASLabel userParamName ]... ¬    [ given userLabel : userParamName [, userLabel : userParamName ]...]       [ statement ]... end [ handlerName ]  ``` |

##### Placeholders

*handlerName*
:   An identifier that names the handler.

*directParamName*
:   An identifier for the direct parameter variable. If it is included, *directParamName* must be listed immediately after the command name. The word `of` or `in` before *directParamName* is required in user-defined handlers, but is optional in terminology-defined handlers (for example, those defined by applications). If a user-defined handler includes a direct parameter, the handler must also include at least one variable parameter.

*ASLabel*
:   An AppleScript-defined label. The available labels are:<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_933"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_934"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_935"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_936"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_937"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_938"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_939"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_940"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_941"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_942"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_943"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_944"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_945"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_946"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_947"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_948"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_949"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_950"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_951"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_952"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_953"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_954"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_955"></a><a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_956"></a> `about`, `above`, `against`, `apart from`, `around`, `aside from`, `at`, `below`, `beneath`, `beside`, `between`, `by`, `for`, `from`, `instead of`, `into`, `on`, `onto`, `out of`, `over`, `since`, `thru` (or `through`), `under`. These are the only labels that can be used without the special label `given`.<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_957"></a> Each label must be unique among the labels for the handler (that is, you cannot use the same label for more than one parameter).

*userLabel*
:   An identifier for a user-defined label, associated with a user-defined parameter. Each label must be unique. The first *userLabel*-*userParamName* pair must follow the word `given`; any additional pairs are separated by commas.

*userParamName*
:   An identifier for a parameter variable.

*statement*
:   Any AppleScript statement. These statements can include definitions of `script` objects, each of which, like any `script` object, can contain handlers and other `script` objects. However, you cannot declare another handler within a handler, except within a `script` object. Handlers often contain a [return](#//apple_ref/doc/uid/TP40000983-CH7g-163937) statement.

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_211"></a>

##### Examples

For examples and related conceptual information, see [Handlers with Labeled Parameters](../conceptual/ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-SW22).

##### Discussion

A handler written to respond to an application command (like those in [Handlers in Script Applications](../conceptual/ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-SW14)) need not include all of the possible parameters defined for that command. For example, an application might define a command with up to five possible parameters, but you could define a handler for that command with only two of the parameters.

If a script calls a handler with more parameters than are specified in the handler definition, the extra parameters are ignored.

<a id="//apple_ref/doc/uid/TP40000983-CH7g-165917"></a>

Calling a Handler with Labeled Parameters

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_958"></a>This section describes the syntax for calling a handler with labeled parameters.

##### Syntax

|  |
| --- |
| ```  handlerName ¬   [ [ of \| in ] directParam ] ¬   [ [ ASLabel paramValue ...] ¬    \| [ with labelForTrueParam [, labelForTrueParam ]... ¬     [ ( and \| , ) labelForTrueParam ] ] ¬    \| [ without labelForFalseParam [, labelForFalseParam ]...] ¬     [ ( and \| , ) labelForFalseParam ] ] ¬    \| [ given userLabel : paramValue [, userLabel : paramValue ]...]...   ``` |

##### Placeholders

*handlerName*
:   An identifier that names the handler.

*directParam*
:   Any valid expression. The expression for the direct parameter must be listed first if it is included at all.

*ASLabel*
:   One of the following AppleScript-defined labels used in the definition of the handler: `about`, `above`, `against`, `apart from,` `around`, `aside from`, `at`, `below`, `beneath`, `beside`, `between`, `by`, `for`, `from`, `instead of`, `into`, `on`, `onto`, `out of`, `over`, `since`, `thru` (or `through`), `under`.

*paramValue*
:   The value of a parameter, which can be any valid expression.

*labelForTrueParam*
:   The label for a Boolean parameter whose value is `true`. You use this form in `with` clauses. Because the value `true` is implied by the word `with`, you provide only the label, not the value. For an example, see the `findNumbers` handler in [Handlers with Labeled Parameters](../conceptual/ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-SW22). <a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_959"></a>

*labelForFalseParam*
:   The label for a Boolean parameter whose value is `false`. You use this form in `without` clauses. Because the value `false` is implied by the word `without`, you provide only the label, not the value.<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_960"></a>

*paramLabel*
:   Any parameter label used in the definition of the handler that is not among the labels for *ASLabel*. You must use the special label `given` to specify these parameters. For an example, see the `findNumbers` handler below.

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_212"></a>

##### Examples

For examples, see [Handlers with Labeled Parameters](../conceptual/ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-SW22).

##### Discussion

When you call a handler with labeled parameters, you supply the following:

1. The handler name.
2. A value for the direct parameter, if the handler has one. It must directly follow the handler name.
3. One label-value pair for each AppleScript-defined label and parameter defined for the handler.
4. One label-value pair for each user-defined label and parameter defined for the handler that *is not* a boolean value.

   The first pair is preceded by the word `given`; a comma precedes each additional pair. The order of the pairs does not have to match the order in the handler definition.
5. For each user-defined label and parameter defined for the handler that *is* a boolean value, you can either:

   1. Supply the label, followed by a boolean expression (as with non-boolean parameters); for example:

      ```
      given rounding:true
      ```
   2. Use a combination of `with` and `without` clauses, as shown in the following examples:

      ```
      with rounding, smoothing and curling
      with rounding without smoothing, curling
      ```

      > <a id="//apple_ref/doc/uid/TP40000983-CH7g-SW3"></a>
      >
      > **Note:** AppleScript automatically converts between some forms when you compile. For example, `given rounding:true` is converted to `with rounding`, and `with rounding, smoothing` is converted to `with rounding and smoothing`.

<a id="//apple_ref/doc/uid/TP40000983-CH7g-166812"></a>

Handler Syntax (Positional Parameters)

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_961"></a>A handler is a collection of statements that can be invoked by name. This section describes the syntax for handlers that use positional parameters.

> <a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_213"></a>
>
> **Important:** The parentheses that surround the parameter list in the following definition are part of the syntax.

##### Syntax

|  |
| --- |
| ```  on \| to handlerName ( [ userParamName [, userParamName ]...] )     [ statement ]...  end [ handlerName ]   ``` |

##### Placeholders

*handlerName*
:   An identifier that names the handler.

*userParamName*
:   An identifier for a user-defined parameter variable.

*statement*
:   Any AppleScript statement, including global or local variable declarations. For information about the scope of local and global variables, see [Scope of Variables and Properties](../conceptual/ASLR_variables.html#//apple_ref/doc/uid/TP40000983-CH223-SW1).

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_214"></a>

##### Examples

For examples and related conceptual information, see [Handlers with Positional Parameters](../conceptual/ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-SW13).

<a id="//apple_ref/doc/uid/TP40000983-CH7g-166906"></a>

Calling a Handler with Positional Parameters

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_962"></a>A call for a handler with positional parameters must list the parameters in the same order as they are specified in the handler definition.

##### Syntax

|  |
| --- |
| ``` handlerName ( [ paramValue [, paramValue ]...] )  ``` |

##### Placeholders

*handlerName*
:   An identifier that names the handler.

*paramValue*
:   The value of a parameter, which can be any valid expression. If there are two or more parameters, they must be listed in the same order in which they were specified in the handler definition.

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_215"></a>

##### Examples

For examples, see [Handlers with Positional Parameters](../conceptual/ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-SW13)

##### Discussion

When you call a handler with positional parameters, you supply the following:

1. The handler name.
2. An opening and closing parenthesis.
3. If the handler has any parameters, then you also list, within the parentheses, the following:

   One value for each parameter defined for the handler. The value can be any valid expression.<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_963"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH7g-SW4"></a>

Handler Syntax (Interleaved Parameters)

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_964"></a>A handler is a collection of statements that can be invoked by name. This section describes the syntax for handlers that use interleaved parameters.

##### Syntax

|  |
| --- |
| ``` on \| to handlerNamePart : userParamName [ namePart : userParamName ]... )    [ statement ]... end [ handlerName ]   ``` |

##### Placeholders

*handlerNamePart* , *namePart*
:   An identifier that, combined with the other parts, forms the handler name.

*userParamName*
:   An identifier for a user-defined parameter variable.

*statement*
:   Any AppleScript statement, including global or local variable declarations. For information about the scope of local and global variables, see [Scope of Variables and Properties](../conceptual/ASLR_variables.html#//apple_ref/doc/uid/TP40000983-CH223-SW1).

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_216"></a>

##### Examples

For examples and related conceptual information, see [Handlers with Interleaved Parameters](../conceptual/ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-SW2).

<a id="//apple_ref/doc/uid/TP40000983-CH7g-SW5"></a>

Calling a Handler with Interleaved Parameters

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_965"></a>A call for a handler with interleaved parameters must list the parameters in the same order as they are specified in the handler definition.

##### Syntax

|  |
| --- |
| ``` ( tell scriptObject to \| scriptObject 's \| my ) handlerNamePart : paramValue [ namePart : paramValue ]...]   ``` |

##### Placeholders

scriptObject
:   A script object to direct the handler call to, which can be any valid expression.

*handlerNamePart* , *namePart*
:   An identifier that names the handler.

*paramValue*
:   The value of a parameter, which can be any valid expression. If there are two or more parameters, they must be listed in the same order in which they were specified in the handler definition.

<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_217"></a>

##### Examples

For examples, see [Handlers with Positional Parameters](../conceptual/ASLR_about_handlers.html#//apple_ref/doc/uid/TP40000983-CH206-SW13)

##### Discussion

When you call a handler with positional parameters, you supply the following:

1. A script object to direct the handler call to, either using `tell` *script* `to`, *script*`'s`, or `my`, equivalent to `tell me to`.
2. The first handler name part.
3. A value for the first parameter.
4. For each additional parameter, you also list the following:

   The next name part, followed by a colon and a value for that parameter. The value can be any valid expression.<a id="//apple_ref/doc/uid/TP40000983-CH7g-DontLinkElementID_966"></a>

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
