<a id="//apple_ref/doc/uid/TP40000983-CH221-SW1"></a>

# Working with Errors

<a id="//apple_ref/doc/uid/TP40000983-CH221-DontLinkElementID_915"></a><a id="//apple_ref/doc/uid/TP40000983-CH221-DontLinkElementID_916"></a>This appendix provides a detailed example of handling errors with [try Statements](https://developer.apple.com/library/archive/applescript-language-guide/reference/ASLR_control_statements.md#//apple_ref/doc/uid/TP40000983-CH6g-128973) and [error Statements](https://developer.apple.com/library/archive/applescript-language-guide/reference/ASLR_control_statements.md#//apple_ref/doc/uid/TP40000983-CH6g-129657). It shows how to use a `try` statement to check for bad data and other errors, and an `error` statement to pass on any error that can’t be handled. It also shows how to check for just a particular error number that you are interested in.

<a id="//apple_ref/doc/uid/TP40000983-CH221-SW2"></a>

## Catching Errors in a Handler

The `SumIntegerList` handler expects a list of integers. If any item in the passed list is not an integer, `SumIntegerList` signals `error number 750` and returns 0. The handler includes an error handler that displays a dialog if the error number is equal to 750; if the error number is not equal to 750, the handler resignals the error with an `error` statement so that other statements in the call chain can handle the unknown error. <a id="//apple_ref/doc/uid/TP40000983-CH221-DontLinkElementID_917"></a>If no statement handles the error, AppleScript displays an error dialog and execution stops.

```
on SumIntegerList from itemList
    try
        -- Initialize return value.
        set integerSum to 0
        -- Before doing sum, check that all items in list are integers.
        if ((count items in itemList) is not equal to ¬
            (count integers in itemList)) then
            -- If all items aren’t integers, signal an error.
            error number 750
        end if
        -- Use a repeat statement to sum the integers in the list.
        repeat with currentItem in itemList
            set integerSum to integerSum + currentItem
        end repeat
        return integerSum -- Successful completion of handler.
    on error errStr number errorNumber
        -- If our own error number, warn about bad data.
        if the errorNumber is equal to 750 then
            display dialog "All items in the list must be integers."
            return integerSum -- Return the default value (0).
        else
            -- An unknown error occurred. Resignal, so the caller
            -- can handle it, or AppleScript can display the number.
            error errStr number errorNumber
        end if
    end try
end SumIntegerList
```

The `SumIntegerList` handler handles various error conditions. For example, the following call completes without error:

```
set sumList to {1, 3, 5}
set listTotal to SumIntegerList from sumList --result: 9
```

The following call passes bad data—the list contains an item that isn’t an integer:

```
set sumList to {1, 3, 5, "A"}
set listTotal to SumIntegerList from sumList
if listTotal is equal to 0 then
    -- the handler didn’t total the list;
    -- do something to handle the error (not shown)
end if
```

The `SumIntegerList` routine checks the list and signals an error 750 because the list contains at least one non-integer item. The routine’s error handler recognizes error number 750 and puts up a dialog to describe the problem. The `SumIntegerList` routine returns 0. The script checks the return value and, if it is equal to 0, does something to handle the error (not shown).

Suppose some unknown error occurs while `SumIntegerList` is processing the integer list in the previous call. When the unknown error occurs, the `SumIntegerList` error handler calls the `error` command to resignal the error. Since the caller doesn’t handle it, AppleScript displays an error dialog and execution halts. The `SumIntegerList` routine does not return a value.

Finally, suppose the caller has its own error handler, so that if the handler passes on an error, the caller can handle it. Assume again that an unknown error occurs while `SumIntegerList` is processing the integer list.

```
try
    set sumList to {1, 3, 5}
    set listTotal to SumIntegerList from sumList
on error errMsg number errorNumber
    display dialog "An unknown error occurred:  " & errorNumber as text
end try
```

In this case, when the unknown error occurs, the `SumIntegerList` error handler calls the `error` command to resignal the error. Because the caller has an error handler, it is able to handle the error by displaying a dialog that includes the error number. Execution can continue if it is meaningful to do so.

<a id="//apple_ref/doc/uid/TP40000983-CH221-SW3"></a>

## Simplified Error Checking

AppleScript provides a mechanism to streamline the way you can catch and handle individual errors. It is often necessary for a script to handle a particular error, but not others. It is possible to catch an error, check for the error number you are interested in, and use an error statement to resignal for other errors. For example:

```
try
    open for access file "MyFolder:AddressData" with write permission
on error msg number n from f to t partial result p
    if n = -49 then -- File already open error
        display dialog "I'm sorry but the file is already open."
    else
        error msg number n from f to t partial result p
    end if
end try
```

This script tries to open a file with write permission, but if the file is already opened, it just displays a dialog. However, you can instead implement this more concisely as:

```
try
    open for access file "MyFolder:AddressData" with write permission
on error number -49
    display dialog "I'm sorry but the file is already open."
end try
```

In this version, there is no need to list the `message`, `from`, `to`, or `partial result` parameters, in order to pass them along. If the error is not -49 (file <name> is already open), this error handler will not catch the error, and AppleScript will pass the error to the next handler in an outer scope.

One drawback to this approach is that you must use a literal constant for the error number in the `on error` parameter list. You can't use global variable or property names because the number must be known when the script is compiled.<a id="//apple_ref/doc/uid/TP40000983-CH221-DontLinkElementID_918"></a>

  

---

Copyright © 2016 Apple Inc. All Rights Reserved. [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](http://www.apple.com/privacy/) | Updated: 2016-01-25
