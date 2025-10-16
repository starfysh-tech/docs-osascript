<a id="//apple_ref/doc/uid/TP40000983-CH6g-157332"></a>

# Control Statements Reference

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_834"></a>This chapter describes AppleScript control statements. A *control statement* is a statement that determines when and how other statements are executed or how expressions are evaluated. For example, a control statement may cause AppleScript to skip or repeat certain statements.

*Simple statements* can be written on one line, while *compound statements* can contain other statements, including multiple clauses with nested and multi-line statements. A compound statement is known as a *statement block*.

Compound statements begin with one or more reserved words, such as `tell`, that identify the type of control statement. The last line of a compound statement always starts with `end`, and can optionally include the word that begins the control statement (such as `end tell`).

<a id="//apple_ref/doc/uid/TP40000983-CH6g-130224"></a>

### considering and ignoring Statements

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_835"></a>The `considering` and `ignoring` statements cause AppleScript to consider or ignore specific characteristics as it executes groups of statements. There are two kinds of `considering` and `ignoring` statements:

* Those that specify attributes to be considered or ignored in performing text comparisons.
* Those that specify whether AppleScript should consider or ignore responses from an application.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-159879"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_836"></a>

considering / ignoring (text comparison)

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_837"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_838"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_839"></a>Specify how AppleScript should treats attributes, such as case, in performing text comparisons.

##### Syntax

|  |
| --- |
| ```  considering attribute [, attribute ... and attribute ] ¬     [ but ignoring attribute [, attribute ... and attribute ] ]        [ statement ]...  end considering   ignoring attribute [, attribute ... and attribute ] ¬     [ but considering attribute [, attribute ... and attribute ] ]        [ statement ]...  end ignoring  ``` |

##### Placeholders

*attribute*
:   A characteristic of the text: `case` : If this attribute is ignored, uppercase letters are not distinguished from lowercase letters. See Special Considerations below for related information. See also `greater than, less than` for a description of how AppleScript sorts letters, punctuation, and other symbols.<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_840"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_841"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_842"></a> `diacriticals` : If this attribute is ignored, `text` objects are compared as if no diacritical marks (such as ´, `, ˆ, ¨, and ˜) are present; for example, `"résumé"` is equal to `"resume"`.<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_843"></a> `hyphens` : If this attribute is ignored, `text` objects are compared as if no hyphens are present; for example `"anti-war"` is equal to `"antiwar"`. <a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_844"></a> `numeric strings` : By default, this attribute is ignored, and text strings are compared according to their character values. For example, if this attribute is considered, `"1.10.1" > "1.9.4"` evaluates as `true`; otherwise it evaluates as `false`. This can be useful in comparing version strings.<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_845"></a> `punctuation` : If this attribute is ignored,`text` objects are compared as if no punctuation marks (such as `. , ? : ; ! ' "`) are present; for example `"What? he inquired."` is equal to `"what he inquired"`. <a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_846"></a> `white space` : If this attribute is ignored, the `text` objects are compared as if spaces, tab characters, and return characters were not present; for example `"Brick house"` would be considered equal to `"Brickhouse"`.<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_847"></a> *Default Value:* : Case and numeric strings are ignored; all others are considered.

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_180"></a>

##### Examples

The following examples show how `considering` and `ignoring` statements for various attributes can change the value of text comparisons.

```
"Hello Bob" = "HelloBob" --result: false
ignoring white space
    "Hello Bob" = "HelloBob" --result: true
end ignoring
 
"BOB" = "bob" --result: true
considering case
    "BOB" = "bob" --result: false
end considering
 
"a" = "á" --result: false
ignoring diacriticals
    "a" = "á" --result: true
end considering
 
"Babs" = "bábs" --result: false
 
ignoring case
    "Babs" = "bábs" --result: false
end ignoring
 
ignoring case and diacriticals
    "Babs" = "bábs" --result: true
end ignoring
```

##### Discussion

You can nest `considering` and `ignoring` statements. If the same attribute appears in both an outer and inner statement, the attribute specified in the inner statement takes precedence.<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_848"></a> When attributes in an inner `considering` or `ignoring` statement are different from those in outer statements, they are added to the attributes to be considered and ignored.

##### Special Considerations

Because `text item delimiters` (described in [version](https://developer.apple.com/library/archive/applescript-language-guide/conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW6)) respect `considering` and `ignoring` attributes in AppleScript 2.0, delimiters are case-insensitive by default. Formerly, they were always case-sensitive. To enforce the previous behavior, add an explicit `considering case` statement.

`considering` and `ignoring` are fully Unicode-aware. For example, with `ignoring case`, “Горбач” is equal to “ГОРБАЧ”. Also, the characters ignored by diacriticals, hyphens, punctuation, and white space are defined by Unicode character classes:

* `ignoring punctuation` ignores category P\*, which includes left- and right-quotation marks such as `“ ” « »`.
* `ignoring hyphens` ignores category Pd, which includes em- and en-dashes.
* `ignoring whitespace` ignores category Z\*, plus tab (\t), return (\r), and linefeed (\n), which includes em-, en-, and non-breaking spaces.

Para

<a id="//apple_ref/doc/uid/TP40000983-CH6g-SW2"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_849"></a>

considering / ignoring (application responses)

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_850"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_851"></a>Permits a script to continue without waiting for an application to respond to commands that target it.

##### Syntax

|  |
| --- |
| ``` considering | ignoring  application responses    [ statement ]... end [ considering | ignoring ]  ``` |

##### Placeholders

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_181"></a>

##### Examples

The following example shows how to use an ignoring statement so that a script needn’t wait while Finder is performing a potentially lengthy task:

```
tell application "Finder"
    ignoring application responses
        empty the trash
    end ignoring
end tell
```

Your script may want to ignore most responses from an application, but wait for a response to a particular statement. You can do so by nesting `considering` and `ignoring` statements:

```
tell application "Finder"
    ignoring application responses
        empty the trash
        -- other statements that ignore application responses
        considering application responses
            set itemName to name of first item of startup disk
        end considering
        -- other statements that ignore application responses
    end ignoring
end tell
```

##### Discussion

A response to an application command indicates whether the command completed successfully, and also returns results and error messages, if there are any. When you use an `ignoring application responses` block, you forego this information.

Results and error messages from AppleScript commands, scripting additions, and expressions are not affected by the `application responses` attribute.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-129657"></a>

### error Statements

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_852"></a>During script execution, errors can occur in the operating system (for example, when a specified file isn’t found), in an application (for example, when the script specifies an object that doesn’t exist), and in the script itself. An <a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_853"></a>*error message* is a message that is supplied by an application, AppleScript, or macOS when an error occurs during the handling of a command. An error message can include an <a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_854"></a>*error number*, which is an integer that identifies the error; an <a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_855"></a>*error expression*, which is an expression, usually a `text` object, that describes the error; and other information.

A script can signal an error—which can then be handled by an error handler—with the `error` statement. This allows scripts to supply their own messages for errors that occur within the script. For example, a script can prepare to handle anticipated errors by using a `try` statement. In the `on error` branch of a `try` statement, a script may be able to recover gracefully from the error. If not, it can use an `error` statement to resignal the error message it receives, modifying the message as needed to supply information specific to the script.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-129678"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_856"></a>

error

Signals an error in a script.

##### Syntax

|  |
| --- |
| ```  error [ errorMessage ] [ number errorNumber ] ¬    [ partial resultresultList ] ¬    [ from offendingObject ] [ to expectedType ]  ``` |

##### Placeholders

*errorMessage*
:   A `text` object describing the error. Although this parameter is optional, you should provide descriptions for errors wherever possible. If you do not include an error description, an empty `text` object ("") is passed to the error handler.

*errorNumber*
:   The error number for the error. This is an optional parameter. If you do not include a number parameter, the value -2700 (unknown error) is passed to the error handler. If the error you are signaling is a close match for one that already has an AppleScript error constant, you can use that constant. If you need to create a new number for the error, avoid using one that conflicts with error numbers defined by AppleScript, macOS, and the Apple Event Manager. In general, you should use positive numbers from 500 to 10,000. For more information, see [Error Numbers and Error Messages](https://developer.apple.com/library/archive/applescript-language-guide/reference/ASLR_error_codes.md#//apple_ref/doc/uid/TP40000983-CH220-SW5).

*resultList*
:   A list of objects. Applies only to commands that return results for multiple objects. If results for some, but not all, of the objects specified in the command are available, you can include them in the partial result parameter. This is rarely supported by applications.

*offendingObject*
:   A reference to the object, if any, that caused the error.

*expectedType*
:   A class. If a parameter specified in the command was not of the expected class, and AppleScript was unable to coerce it to the expected class, then you can include the expected class in the `to` parameter.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_182"></a>

##### Examples

The following example uses a `try` statement to handle a simple error, and demonstrates how you can use an `error` statement to catch an error, then resignal the error exactly as it was received, causing AppleScript to display an error dialog (and halt execution):

```
try
    word 5 of "one two three"
on error eStr number eNum partial result rList from badObj to expectedType
    -- statements that take action based on the error
    display dialog "Doing some preliminary handling..."
    -- then resignal the error
    error eStr number eNum partial result rList from badObj to expectedType
end try
```

In the next example, an `error` statement resignals an error, but omits any original error information and supplies its own message to appear in the error dialog:

```
try
    word 5 of "one two three"
on error
    -- statements to execute in case of error
    error "There are not enough words."
end try
```

For more comprehensive examples, see [Working with Errors](https://developer.apple.com/library/archive/applescript-language-guide/reference/ASLR_error_xmpls.md#//apple_ref/doc/uid/TP40000983-CH221-SW1).

<a id="//apple_ref/doc/uid/TP40000983-CH6g-158244"></a>

### if Statements

An `if` statement allows you to define statements or groups of statements that are executed only in specific circumstances, based on the evaluation of one or more Boolean expressions.<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_857"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_858"></a>

An `if` statement is also called a conditional statement. Boolean expressions in `if` statements are also called tests.<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_859"></a>

<a id="//apple_ref/doc/uid/TP40000983-CH6g-126990"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_860"></a>

if (simple)

Executes a statement if a Boolean expression evaluates to `true`.

##### Syntax

|  |
| --- |
| ```  if boolean then statement   ``` |

##### Placeholders

*boolean*
:   A Boolean expression.

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_183"></a>

##### Examples

This script displays a dialog if the value of the Boolean expression `ageOfCat > 1` is `true`. (The variable `ageOfCat` is set previously.)

```
if ageOfCat > 1 then display dialog "This is not a kitten."
```

<a id="//apple_ref/doc/uid/TP40000983-CH6g-127122"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_861"></a>

if (compound)

Executes a group (or groups) of statements if a Boolean expression (or expressions) evaluates to `true`.

##### Syntax

|  |
| --- |
| ```  if boolean [ then ]    [ statement ]...  [else if boolean [ then ]    [ statement ]...]...  [else    [ statement ]...]  end [ if ]  ``` |

##### Placeholders

*boolean*
:   A Boolean expression.

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_184"></a>

##### Examples

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_862"></a>The following example uses a compound `if` statement, with a final `else` clause, to display a statement based on the current temperature (obtained separately):

```
if currentTemp < 60 then
    set response to "It's a little chilly today."
else if currentTemp > 80 then
    set response to "It's getting hotter today."
else
    set response to "It's a nice day today."
end if
display dialog response
```

##### Discussion

An `if` statement can contain any number of `else if` clauses; AppleScript looks for the first Boolean expression contained in an `if` or `else if` clause that is `true`, executes the statements contained in its block (the statements between one `else if` and the following `else if` or `else` clause), and then exits the `if` statement.<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_863"></a>

An `if` statement can also include a final `else`<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_864"></a> clause. The statements in its block are executed if no other test in the `if` statement passes.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-127362"></a>

### repeat Statements

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_865"></a>You use a `repeat` statement to create loops or execute groups of repeated statements in scripts.

There are a number of types of `repeat` statement, each differing in the way it terminates the loop. Each of the options, from repeating a loop a specific number of times, to looping over the items in a list, to looping until a condition is met, and so on, lends itself to particular kinds of tasks.

For information on testing and debugging `repeat` statements, see [Debugging AppleScript Scripts](https://developer.apple.com/library/archive/applescript-language-guide/conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW20).

<a id="//apple_ref/doc/uid/TP40000983-CH6g-128843"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_866"></a>

exit

Terminates a `repeat` loop and resumes execution with the statement that follows the `repeat` statement.<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_867"></a>

You can only use an `exit` statement inside a `repeat` statement. Though most commonly used with the `repeat (forever)` form, you can also use an `exit` statement with other types of `repeat` statement.

##### Syntax

|  |
| --- |
| ```  exit [ repeat ]  ``` |

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_185"></a>

##### Examples

See the example in `repeat (forever)`.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-127499"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_868"></a>

repeat (forever)

Repeats a statement (or statements) until an <a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_869"></a>`exit` statement is encountered.

> <a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_186"></a>
>
> **Important:** A `repeat` (forever) statement will never complete unless you cause it to do so.

To terminate a `repeat` (forever) statement, you can:

* Use an `exit` statement and design the logic so that it eventually encounters the `exit` statement.
* Use a `return` statement, which exits the handler or script that contains the loop, and therefore the loop as well.
* Use a `try` statement and rely on an error condition to exit the loop.

##### Syntax

|  |
| --- |
| ```  repeat     [ statement ]...  end [ repeat ]  ``` |

##### Placeholders

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_187"></a>

##### Examples

This form of the `repeat` statement is similar to the `repeat until` form, except that instead of putting a test in the `repeat` statement itself, you determine within the loop when it is time to exit. You might use this form, for example, to wait for a lengthy or indeterminate operation to complete:

```
repeat
    -- perform operations
    if someBooleanTest then
        exit repeat
    end if
end repeat
```

In a script application that stays open, you can use an `idle` handler to perform periodic tasks, such as checking for an operation to complete. See [idle Handlers](https://developer.apple.com/library/archive/applescript-language-guide/conceptual/ASLR_about_handlers.md#//apple_ref/doc/uid/TP40000983-CH206-SW8) for more information.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-127676"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_870"></a>

repeat (number) times

Repeats a statement (or statements) a specified number of times.

##### Syntax

|  |
| --- |
| ```  repeat integer [ times ]     [ statement ]...  end [ repeat ]  ``` |

##### Placeholders

*integer*
:   Specifies the number of times to repeat the statements in the body of the loop. Instead of an integer, you can specify any value that can be coerced to an integer. If the value is less than one, the body of the `repeat` statement is not executed.

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_188"></a>

##### Examples

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_871"></a>The following handler uses the `repeat (number) times` form of the `repeat` statement to raise a passed number to the passed power:

```
on raiseToTheNth(x, power)
    set returnVal to x
    repeat power - 1 times
        set returnVal to returnVal * x
    end repeat
    return returnVal
end raiseToTheNth
```

<a id="//apple_ref/doc/uid/TP40000983-CH6g-128014"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_872"></a>

repeat until

Repeats a statement (or statements) until a condition is met. Tests the condition before executing any statements.

##### Syntax

|  |
| --- |
| ```  repeat until boolean     [ statement ]...  end [ repeat ]  ``` |

##### Placeholders

*boolean*
:   A Boolean expression. If it has the value `true` when entering the loop, the statements in the loop are not executed.

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_189"></a>

##### Examples

The following example uses the `repeat until` form of the `repeat` statement to allow a user to enter database records. The handler `enterDataRecord()`, which is not shown, returns `true` if the user is done entering records:

```
set userDone to false
repeat until userDone
    set userDone to enterDataRecord()
end repeat
```

<a id="//apple_ref/doc/uid/TP40000983-CH6g-127845"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_873"></a>

repeat while

Repeats a statement (or statements) as long as a condition is met. Tests the condition before executing any statements. Similar to the `repeat until` form, except that it continues *while* a condition is `true`, instead of *until* it is `true`.

##### Syntax

|  |
| --- |
| ```  repeat while boolean     [ statement ]...  end [ repeat ]  ``` |

##### Placeholders

*boolean*
:   A Boolean expression. If it has the value `false` when entering the loop, the statements in the loop are not executed.

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_190"></a>

##### Examples

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_874"></a>The following example uses the `repeat while` form of the `repeat` statement to allow a user to enter database records. In this case, we’ve just reversed the logic shown in the `repeat until` example. Here, the handler `enterDataRecord()`, which is not shown, returns `true` if the user is *not* done entering records:

```
set userNotDone to true
repeat while userNotDone
    set userNotDone to enterDataRecord()
end repeat
```

<a id="//apple_ref/doc/uid/TP40000983-CH6g-128207"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_875"></a>

repeat with loopVariable (from startValue to stopValue)

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_876"></a>Repeats a statement (or statements) until the value of the controlling loop variable exceeds the value of the predefined stop value.

##### Syntax

|  |
| --- |
| ```  repeat with  loopVariable  from  startValue  to  stopValue [ by  stepValue ]     [ statement ]...  end [ repeat ]  ``` |

##### Placeholders

*loopVariable*
:   Controls the number of iterations. It can be a previously defined variable or a new variable you define in the `repeat` statement.

*startValue*
:   Specifies a value that is assigned to *loopVariable* when the loop is entered. You can specify an integer or any value that can be coerced to an integer.

*stopValue*
:   Specifies an value. When that value is exceeded by the value of *loopVariable*, iteration ends. If *stopValue* is less than *startValue*, the body is not executed. You can specify an integer or any value that can be coerced to an integer.

*stepValue*
:   Specifies a value that is added to *loopVariable* after each iteration of the loop. You can assign an `integer` or a `real` value; a `real` value is rounded to an `integer`. *Default Value:* : 1

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_191"></a>

##### Examples

The following handler uses the `repeat with loopVariable (from startValue to stopValue)` form of the `repeat` statement to compute a factorial value (the factorial of a number is the product of all the positive integers from 1 to that number):

```
on factorial(x)
    set returnVal to 1
    repeat with n from 2 to x
        set returnVal to returnVal * n
    end repeat
    return returnVal
end factorial
```

##### Discussion

You can use an existing variable as the loop variable in a `repeat with loopVariable (from startValue to stopValue)` statement or define a new one in the statement. In either case, the loop variable is defined outside the loop. You can change the value of the loop variable inside the loop body but it will get reset to the next loop value the next time through the loop. After the loop completes, the loop variable retains its last value.

AppleScript evaluates *startValue*, *stopValue*, and *stepValue* when it begins executing the loop and stores the values internally. As a result, if you change the values in the body of the loop, it doesn’t change the execution of the loop.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-128481"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_877"></a>

repeat with loopVariable (in list)

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_878"></a>Loops through the items in a specified list.

The number of iterations is equal to the number of items in the list. In the first iteration, the value of the variable is a reference to the first item in *list*, in the second iteration, it is a reference to the second item in *list*, and so on.

##### Syntax

|  |
| --- |
| ```  repeat with loopVariable in list     [ statement ]...  end [ repeat ]  ``` |

##### Placeholders

*loopVariable*
:   Any previously defined variable or a new variable you define in the `repeat` statement (see Discussion).

*list*
:   A list or a object specifier (such as `words 1 thru 5`) whose value is a list. *list* can also be a record; AppleScript coerces the record to a list (see Discussion).

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_192"></a>

##### Examples

The following script uses the `repeat with loopVariable (in list)` form of the `repeat` statement to loop through a list of first names, displaying a greeting for each.

```
set peopleList to {"Chris", "David", "Sal", "Ben"}
repeat with aPerson in peopleList
    display dialog "Hello " & aPerson & "!"
end repeat
```

##### Discussion

You can use an existing variable as the loop variable in a `repeat with loopVariable (in list)` statement or define a new one in the `repeat with…` statement. In either case, the loop variable is assigned a new value—the current item in the loop—at the start of each loop. After the loop completes, the loop variable retains its last value.

This example uses an existing variable as the loop variable:

```
set currentIncrement to 0
-- The loop variable is an existing variable, defined above
repeat with currentIncrement in {1, 2, 3, 4}
    -- Do something
end repeat
currentIncrement
--result: item 4 of {1, 2, 3, 4} --result: the last value of the loop variable
```

This example defines a new variable as the loop variable:

```
-- The loop variable is a new variable, defined in the repeat statement
repeat with currentIncrement in {1, 2, 3, 4}
    -- Do something
end repeat
currentIncrement
--result: item 4 of {1, 2, 3, 4} --result: the last value of the loop variable
```

You can change the value of the loop variable inside the loop body, but it gets reset to the next loop value the next time through the loop. Again, after the loop completes, the loop variable retains its last value.

```
repeat with currentIncrement in {1, 2, 3, 4}
    display dialog currentIncrement
    set currentIncrement to 0
end repeat
currentIncrement
--result: 0
```

AppleScript evaluates *loopVariable* `in` *list* as an object specifier—a reference to the current item in the list—that takes on the value of `item 1 of list`, `item 2 of list`, `item 3 of list`, and so on until it reaches the last item in the list. For example:

```
repeat with i in {1, 2, 3, 4}
    set listItem to i
end repeat
--result: item 4 of {1, 2, 3, 4} --result: an object specifier
```

To access the actual value of an item in the list, rather than a reference to the item, use the `contents of` property:

```
repeat with i in {1, 2, 3, 4}
    set listItem to contents of i
end repeat
--result: 4
```

This technique is especially important when performing a comparison, as you typically want to test whether the *value* of a list item matches another value. The following script examines a list of words, displaying a dialog if it finds the word “hammer” in the list. To perform a proper comparison, the test statement (`if (contents of currentWord) is equal to "hammer" then`) compares the `contents` of the current list item, rather than the object specifier itself.

```
set wordList to words in "Where is the hammer?"
repeat with currentWord in wordList
    log currentWord
    if (contents of currentWord) is equal to "hammer" then
        display dialog "I found the hammer!"
    end if
end repeat
```

> <a id="//apple_ref/doc/uid/TP40000983-CH6g-SW11"></a>
>
> **Note:** In the previous example, the statement `log currentWord` logs the current list item to Script Editor’s log pane. For more information about logging, see [Debugging AppleScript Scripts](https://developer.apple.com/library/archive/applescript-language-guide/conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW20).

You can also use list variables directly in expressions, which may result in an implicit coercion from an object reference to a specific data type. In the following example, the loop variable `i` is implicitly coerced to an integer (equivalent to explicitly retrieving the `contents of i`) by using the `+` operator to add it to a variable containing an integer.

```
set total to 0
repeat with i in {1, 2, 3, 4}
    set total to total + i
end repeat
--result: 10
```

<a id="//apple_ref/doc/uid/TP40000983-CH6g-158637"></a>

### tell Statements

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_879"></a>A `tell` statement specifies the default target—that is, the object to which commands are sent if they do not include a direct parameter. Statements within a `tell` statement that use terminology from the targeted object are compiled against that object’s dictionary.

The object of a `tell` statement is typically a reference to an application object or a `script` object. For example, the following `tell` statement targets the Finder application:

```
tell application "Finder"
    set frontWindowName to name of front window
    -- any number of additional statements can appear here
end tell
```

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_880"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_881"></a>You can nest `tell` statements inside other `tell` statements, as long as you follow the syntax and rules described in `tell (compound)`.

When you need to call a handler from within a `tell` statement, there are special terms you use to indicate that the handler is part of the script and not a command that should be sent to the object of the `tell` statement. These terms are described in [The it and me Keywords](https://developer.apple.com/library/archive/applescript-language-guide/conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW4) and in [Calling Handlers in a tell Statement](https://developer.apple.com/library/archive/applescript-language-guide/conceptual/ASLR_about_handlers.md#//apple_ref/doc/uid/TP40000983-CH206-SW1).

A `tell` statement that targets a local application doesn’t cause it to launch, if it is not already running. For example, a script can examine the `running` property of the targeted `application` object to determine if the application is running before attempting to send it any commands. If it is not running it won’t be launched.

If a `tell` statement targets a local application and executes any statements that require a response from the application, then AppleScript will launch the application if it is not already running. The application is launched as hidden, but the script can send it an `activate` command to bring it to the front, if needed.

A `tell` statement that targets a remote application will not cause it to launch—in fact, it will not compile or run unless the application is already running. Nor is it possible to access the `running` property of an application on a remote computer.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-157872"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_882"></a>

tell (simple)

Specifies a target object and a command to send to it.

##### Syntax

|  |
| --- |
| ```  tell referenceToObject to statement   ``` |

##### Placeholders

*referenceToObject*
:   Any object. Typically an object specifier or a `reference` object (which contains an object specifier).

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_193"></a>

##### Examples

This simple `tell` statement closes the front Finder window:

```
tell front window of application "Finder" to close
```

For more information on how to specify an application object, see the `application` class.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-158020"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_883"></a>

tell (compound)

Specifies a target object and one or more commands to send to it. A compound `tell` statement is different from a simple `tell` statement in that it always includes an `end` statement.

##### Syntax

|  |
| --- |
| ```  tell referenceToObject      [ statement ]...  end [ tell ]  ``` |

##### Placeholders

*referenceToObject*
:   Any object. Typically an object specifier or a `reference` object (which contains an object specifier).

*statement*
:   Any AppleScript statement, including another `tell` statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_194"></a>

##### Examples

The following statements show how to close a window using first a compound `tell` statement, then with two variations of a simple `tell` statement:

```
tell application "Finder"
    close front window
end tell
 
tell front window of application "Finder" to close
tell application "Finder" to close front window
```

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_884"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_885"></a>The following example shows a nested `tell` statement:

```
tell application "Finder"
    tell document 1 of application "TextEdit"
        set newName to word 1 -- handled by TextEdit
    end tell
    set len to count characters in newName -- handled by AppleScript
    if (len > 2) and (len < 15) then -- comparisons handled by AppleScript
        set name of first item of disk "HD" to newName -- handled by Finder
    end if
end tell
```

This example works because in each case the terminology understood by a particular application is used within a `tell` block targeting that application. However, it would not compile if you asked the Finder for `word 1` of a document, or told TextEdit to `set name` of the first item on a disk, because those applications do not support those terms.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-128973"></a>

### try Statements

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_886"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_887"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_888"></a>A `try` statement provides the means for scripts to handle potential errors. It attempts to execute one or more statements and, if an error occurs, executes a separate set of statements to deal with the error condition. If an error occurs and there is no `try` statement in the calling chain to handle it, AppleScript displays an error and script execution stops.

For related information, see [error Statements](#//apple_ref/doc/uid/TP40000983-CH6g-129657) and [AppleScript Error Handling](https://developer.apple.com/library/archive/applescript-language-guide/conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW10).

<a id="//apple_ref/doc/uid/TP40000983-CH6g-129232"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_889"></a>

try

Attempts to execute a list of AppleScript statements, calling an error handler if any of the statements results in an error.

A `try` statement is a two-part compound statement that contains a series of AppleScript statements, followed by an error handler to be invoked if any of those statements causes an error. If the statement that caused the error is included in a `try` statement, then AppleScript passes control to the error handler. After the error handler completes, control passes to the statement immediately following the end of the `try` statement.

##### Syntax

|  |
| --- |
| ```  try     [ statement ]...  [ on error [ errorMessage ] [ number errorNumber ] [ from offendingObject ] ¬     [ partial result resultList ] [ to expectedType ]        [ statement ]... ]  end [ error | try ]  ``` |

##### Placeholders

*statement*
:   Any AppleScript statement.

*errorMessage*
:   A `text` object, that describes the error.

*errorNumber*
:   The error number, an integer. For possible values, see [Error Numbers and Error Messages](https://developer.apple.com/library/archive/applescript-language-guide/reference/ASLR_error_codes.md#//apple_ref/doc/uid/TP40000983-CH220-SW5).

*offendingObject*
:   A reference to the object, if any, that caused the error.

*resultList*
:   A list that provides partial results for objects that were handled before the error occurred. The list can contain values of any class. This parameter applies only to commands that return results for multiple objects. This is rarely supported by applications.

*expectedType*
:   The expected class. If the error was caused by a coercion failure, the value of this variable is the class of the coercion that failed. (The second example below shows how this works in a case where AppleScript is unable to coerce a `text` object into an `integer`.)

*variable*
:   Either a global variable or a local variable that can be used in the handler. A variable can contain any class of value. The scope of a local variable is the handler. The scope of a global variable extends to any other part of the script, including other handlers and `script` objects. For related information about local and global variables, see [version](https://developer.apple.com/library/archive/applescript-language-guide/conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW6).

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_195"></a>

##### Examples

The following example shows how you can use a `try` statement to handle the “Cancel” button for a `display alert` command. Canceling returns an error number of -128, but is not really an error. This test handler just displays a dialog to indicate when the user cancels or when some other error occurs.

```
try
    display alert "Hello" buttons {"Cancel", "Yes", "No"} cancel button 1
on error errText number errNum
    if (errNum is equal to -128) then
        -- User cancelled.
        display dialog "User cancelled."
    else
        display dialog "Some other error: " & errNum & return & errText
    end if
end try
```

You can also use a simplified version of the `try` statement that checks for just a single error number. In the following example, only error -128 is handled. Any other error number is ignored by this `try` statement, but is automatically passed up the calling chain, where it may be handled by other `try` statements.

```
try
    display alert "Hello" buttons {"Cancel", "Yes", "No"} cancel button 1
on error number -128
    -- Either do something special to handle Cancel, or just ignore it.
end try
```

The following example demonstrates the use of the `to` keyword to capture additional information about an error that occurs during a coercion failure:

```
try
    repeat with i from 1 to "Toronto"
        -- do something that depends on variable "i"
    end repeat
on error from obj to newClass
    log {obj, newClass} -- Display from and to info in log pane.
end try
```

This `repeat` statement fails because the `text` object `"Toronto"` cannot be coerced to an `integer`. The error handler simply writes the values of `obj` (the offending value, `"Toronto"`) and `newClass` (the class of the coercion that failed, `integer`<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_890"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_891"></a>) to Script Editor’s Event Log History window (and to the script window’s Event Log pane). The result is “(\*Toronto, integer\*)”, indicating the error occurred while trying to coerce “Toronto” to an integer.

For additional examples, see [Working with Errors](https://developer.apple.com/library/archive/applescript-language-guide/reference/ASLR_error_xmpls.md#//apple_ref/doc/uid/TP40000983-CH221-SW1).

<a id="//apple_ref/doc/uid/TP40000983-CH6g-SW4"></a>

### use Statements

A `use` statement declares a required resource for a script—an application, script library, framework, or version of AppleScript itself—and can optionally *import* terminology from the resource for use elsewhere in the script. The effects and syntax of `use` vary slightly depending on the used resource; the different cases are described below.

> <a id="//apple_ref/doc/uid/TP40000983-CH6g-SW7"></a>
>
> **Note:** `use` statements are supported in OS X Mavericks v10.9 (AppleScript 2.3) and later.

The basic function of `use` is to require that a resource be present before the script begins executing. If the requirement cannot be met, the script will fail to run. A `use` statement can also specify a minimum version for the required resource, such as a minimum compatible version of an application. In this example, AppleScript will ensure that Safari version 7.0 or later is available:

```
use application "Safari" version "7.0"
```

`use` statements can also import terminology from the used resource, making the terms available throughout the script without requiring the use of `tell` or `using terms from`. AppleScript tracks where terms were imported from, and sends events that use those terms to that target. Ordinarily, commands are sent to the current target (`it`) as described in [Target](https://developer.apple.com/library/archive/applescript-language-guide/conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW18), but imported terminology overrides this. If…

* the event identifier is imported
* the direct parameter is an imported class or enumeration identifier
* the direct parameter is an object specifier ending with an imported term

…then the command is sent to the import source instead. This happens even if the command is inside a `tell` block for a different target. For example, this script uses a command from Safari:

```
use application "Safari"
search the web for "AppleScript"
```

Importing happens by default, but can be suppressed using the `without importing` parameter, if applicable. You can use this to add requirements to existing scripts without changing anything else about the script:

```
use application "Safari" version "7.0" without importing
```

Because Safari's terms are not imported, the script will still need to use `tell` to send it events.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-SW8"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_892"></a>

use (AppleScript)

Declares a required minimum version of AppleScript, and that the script expects a newer behavior for how scripting additions are handled, described in [use (scripting additions)](#//apple_ref/doc/uid/TP40000983-CH6g-SW5).

##### Syntax

|  |
| --- |
| ``` use AppleScript [ version versionText ]   ``` |

##### Placeholders

versionText
:   The required minimum version of AppleScript, as a version string such as `"2.3.2"`. If omitted, its default value is 2.3, the version in which `use` was introduced. This value is always text, not a number, and is compared as if `considering numeric strings` is in effect. For example, `"2.10"` is greater than `"2.3"`, because 10 is greater than 3.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_196"></a>

##### Examples

In its simplest form, `use` can be used to declare that the script uses AppleScript:

```
use AppleScript
```

This also implicitly means that the script uses AppleScript version 2.3 or later, when `use` was first introduced, and that the script expects a newer behavior for how scripting additions are handled, described in [use (scripting additions)](#//apple_ref/doc/uid/TP40000983-CH6g-SW5).

A `use` command can also explicitly specify a minimum required version of AppleScript:

```
use AppleScript version "2.3.2"
```

<a id="//apple_ref/doc/uid/TP40000983-CH6g-SW5"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_893"></a>

use (scripting additions)

Declares that a script uses scripting additions.

##### Syntax

|  |
| --- |
| ``` use scripting additions ¬     [ with importing | without importing | importing boolean ]  ``` |

##### Placeholders

boolean
:   A boolean value,`true` or `false`. AppleScript will recompile this to `with importing` or `without importing`. The default is `with importing`.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_197"></a>

##### Examples

Use `use scripting additions` to explicitly declare that the script uses scripting addition commands:

```
use scripting additions
```

##### Discussion

Scripting addition commands are handled differently if a script has `use` commands. If a script has one or more `use` commands of any kind, scripting addition commands are *not* available by default. You must explicitly indicate that you wish to use scripting additions, either with a `use` or `using terms from` command.

```
use scripting additions
display dialog "hello world"
```

```
using terms from scripting additions
   display dialog "hello world"
end using terms from
```

If a script uses `use scripting additions`, AppleScript may optimize scripting addition commands, sending them to the current application instead of the current target (`it`) when it does not change the meaning to do so. For example, [random number](https://developer.apple.com/library/archive/applescript-language-guide/reference/ASLR_cmds.md#//apple_ref/doc/uid/TP40000983-CH216-SW42) does not need to be sent to another application to work correctly, and will always be sent to the current application when imported with `use`. Without a `use scripting additions` command, AppleScript must use a less efficient dispatching scheme, so explicitly declaring them is recommended.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-SW9"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_894"></a>

use (application or script)

Declares a required application or script library, and may import its terms for use later in the script.

##### Syntax

|  |
| --- |
| ``` use [ identifier : ] ( script | application ) specifier ¬    [ version versionText ] ¬    [ with importing | without importing | importing boolean ]  ``` |

##### Placeholders

versionText
:   The required minimum version of the resource as a version number, such as `"2.3.2"`. This value is always text, not a number, and is compared as if `considering numeric strings` is in effect. For example, `"2.10"` is greater than `"2.3"`, because 10 is greater than 3.

identifier
:   An optional identifier for the resource.

specifier
:   Specifier data for the resource. This is typically a name, as in `use application "Finder"` or `use script "My Library"`, but may be any valid specifier form, such as by ID, as in `use application id "com.apple.mail"`.

boolean
:   A boolean value,`true` or `false`. AppleScript will recompile this to `with importing` or `without importing`. The default is `with importing`.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_198"></a>

##### Examples

A `use` command may refer to an application:

```
use application "Finder"
```

…or a script library:

```
use script "Happy Fun Ball"
```

If an optional identifier is given, it defines a property whose value is the required resource. This can make it more convenient to refer to the resource, as in this example: the `get` statement uses the identifier `Safari` instead of the full specifier `application "Safari"`.

```
use Safari : application "Safari"
get the name of Safari's front window
```

By using `use` with multiple applications, you can combine terms from different sources in ways impossible using `tell`, because `tell` only makes one terminology source available at a time. For example, the following script, in one statement, uses Mail and Safari to search the web for the sender of the currently selected mail message. The `get` event is sent to Mail because it defines `message viewer`, while the `search the web` event is sent to Safari.

```
use application "Mail"
use application "Safari"
 
search the web for the sender of the first item of ¬
 
   (get selected messages of the front message viewer)
```

<a id="//apple_ref/doc/uid/TP40000983-CH6g-SW6"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_895"></a>

use (framework)

Declares a required framework for use with the AppleScript/Objective-C bridge.

##### Syntax

|  |
| --- |
| ``` use  framework  specifier  ``` |

##### Placeholders

specifier
:   Specifier data for the resource. This may be a base name (`"AppKit"`), a full name (`"AppKit.framework"`), or a POSIX path (`"/System/Library/Frameworks/AppKit.framework"`).

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_199"></a>

##### Examples

Most scripts that use the AppleScript/Objective-C bridge should have at least one of these two `use` statements:

```
use framework "Foundation"
use framework "AppKit"
```

You can also use other frameworks, such as WebKit:

```
use framework "WebKit"
```

##### Discussion

When you declare a required framework, AppleScript ensures the framework is loaded before running your script. To ensure that your AppleScript/Objective-C script libraries work correctly in any application, declare all needed frameworks explicitly; otherwise, there is no guarantee that a given framework will be available, and your script may fail.

The `version` parameter is not supported for frameworks; to check whether or not a framework supports a certain feature, use `NSClassFromString` or `-respondsToSelector:`.

> <a id="//apple_ref/doc/uid/TP40000983-CH6g-SW10"></a>
>
> **Note:** OS X Yosemite v10.10 and later allow using Objective-C frameworks from any script. OS X Mavericks v10.9 only allows using Objective-C frameworks from a script library.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-SW3"></a>

### using terms from Statements

A `using terms from` statement lets you specify which terminology AppleScript should use in compiling the statements in a script. Whereas a `tell` statement specifies the default target (often an application) to which commands are sent *and* the terminology to use, a `using terms from` statement specifies only the terminology.

A `using terms from` statement can be useful in writing application event handler scripts, such as Mail rules.

Another use for this type of statement is with a script that targets an application on a remote computer that may not be available when you compile the script (or the application may not be running). Or, you might be developing locally and only want to test with the remote application at a later time. In either case, you can use a `using terms from` statement to specify a local application (presumably with a terminology that matches the one on the remote computer) to compile against.

Even if a statement contained within a `using terms from` statement compiles, the script may fail when run because the target application’s terminology may differ from that used in compiling.

You can nest `using terms from` statements. When you do so, each script statement is compiled against the terminology of the application named in the innermost enclosing `using terms from` statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-SW1"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_896"></a>

using terms from

Instructs AppleScript to use the terminology from the specified source in compiling the enclosed statements.

##### Syntax

|  |
| --- |
| ``` using terms from ( application  |  script  | scripting additions)     [ statement ]...  end [ using terms from ]  ``` |

##### Placeholders

*application*
:   A specifier for an application object.

script
:   A specifier for a script library.

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_200"></a>

##### Examples

The following example shows how to use a `using terms from` statement in writing a Mail rule action script. These scripts take the following form:

```
using terms from application "Mail"
  on perform mail action with messages theMessages for rule theRule
    tell application "Mail"
        -- statements to process each message in theMessages
    end tell
  end perform mail action with messages
end using terms from
```

To use the script, you open Preferences for the Mail application, create or edit a rule, and assign the script as the action for the rule.

For an example that works with an application on a remote machine, see [Targeting Remote Applications](https://developer.apple.com/library/archive/applescript-language-guide/conceptual/ASLR_fundamentals.md#//apple_ref/doc/uid/TP40000983-CH218-SW35).

As discussed in [use Statements](#//apple_ref/doc/uid/TP40000983-CH6g-SW4), a script with any `use` statements does not make scripting addition terms visible by default. You can enable scripting addition terms for specific parts of a script with `using terms from` as in this example:

```
use AppleScript
-- scripting addition commands such as "display dialog" will not compile here...
using terms from scripting additions -- ...but will compile within this block.
   display dialog "Hello world!"
end using terms from
```

##### Discussion

`using terms from` does not import terms as `use` does, and is subject to the same limits on terminology use as `tell`. `using terms from scripting additions` does not enable optimization of scripting addition commands as `use scripting additions` does.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-130992"></a>

### with timeout Statements

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_897"></a>You can use a `with timeout` statement to control how long AppleScript waits for a command to execute before timing out. By default, <a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_898"></a>when an application fails to respond to a command, AppleScript waits for two minutes before reporting an error and halting execution.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-131094"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_899"></a>

with timeout

Specifies how long AppleScript waits for a response to a command that is sent to another application.

##### Syntax

|  |
| --- |
| ```  with timeout [ of ] integerExpression second[s]     [ statement ]...  end [ timeout ]   ``` |

##### Placeholders

*integerExpression*
:   The amount of time, in seconds, AppleScript should wait before timing out (and interrupting the command).

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_201"></a>

##### Examples

The following script tells TextEdit to close its first document; if the document has been modified, it asks the user if the document should be saved. It includes the statement `with timeout of 20 seconds`, so that if the user doesn’t complete the `close` operation within 20 seconds, the operation times out.

```
tell application "TextEdit"
    with timeout of 20 seconds
        close document 1 saving ask
    end timeout
end tell
```

##### Discussion

When a command fails to complete in the allotted time (whether the default of two minutes, or a time set by a `with timeout` statement), AppleScript stops running the script and returns the error `"event timed out"`.<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_900"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_901"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_902"></a> AppleScript does not cancel the operation—it merely stops execution of the script. If you want the script to continue, you can wrap the statements in a `try` statement. However, whether your script can send a command to cancel an offending lengthy operation after a timeout is dependent on the application that is performing the command.

A `with timeout` statement applies only to commands sent to application objects, not to commands sent to the application that is running the script.

In some situations, you may want to use an `ignoring application responses` statement (instead of a `with timeout` statement) so that your script needn’t wait for application commands to complete. For more information, see [considering and ignoring Statements](#//apple_ref/doc/uid/TP40000983-CH6g-130224).

<a id="//apple_ref/doc/uid/TP40000983-CH6g-131273"></a>

### with transaction Statements

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_903"></a>When you execute a script, AppleScript may send one or more Apple events to targeted applications. A transaction is a set of operations that are applied as a single unit—either all of the changes are applied or none are. This mechanism works only with applications that support it.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-131303"></a><a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_904"></a>

with transaction

Associates a single transaction ID with any events sent to a target application as a result of executing commands in the body of the statement.

##### Syntax

|  |
| --- |
| ```  with transaction [ session ]      [ statement ]...  end [ transaction ]  ``` |

##### Placeholders

*session*
:   An object that identifies a specific session.

*statement*
:   Any AppleScript statement.

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_202"></a>

##### Examples

<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_905"></a>This example uses a `with transaction` statement to ensure that a record can be modified by one user without being modified by another user at the same time. (In the following examples, “Small DB” and “Super DB” are representative database applications.)

```
tell application "Small DB"
    with transaction
        set oldName to Field "Name"
        set oldAddress to Field "Address"
        set newName to display dialog ¬
            "Please type a new name" ¬
            default answer oldName
        set newAddress to display dialog ¬
            "Please type the new address" ¬
            default answer oldAddress
        set Field "Name" to newName
        set Field "Address" to newAddress
    end transaction
end tell
```

The `set` statements obtain the current values of the Name and Address fields and invite the user to change them. Enclosing these `set` statements in a single `with transaction` statement informs the application that other users should not be allowed to access the same record at the same time.

A `with transaction` statement works only with applications that explicitly support it. Some applications only support `with transaction` statements (like the one in the previous example) that do not take a session object as a parameter. Other applications support both `with transaction` statements that have no parameter and `with transaction` statements that take a session parameter.

The following example demonstrates how to specify a session for a `with transaction` statement:<a id="//apple_ref/doc/uid/TP40000983-CH6g-DontLinkElementID_906"></a>

```
tell application "Super DB"
    set mySession to make session with data {user: "Bob", password: "Secret"}
    with transaction mySession
        ...
    end transaction
end tell
```

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
