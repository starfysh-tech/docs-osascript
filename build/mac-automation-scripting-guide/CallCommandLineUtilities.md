<a id="//apple_ref/doc/uid/TP40016239-CH43"></a><a id="//apple_ref/doc/uid/TP40016239-CH43-SW1"></a>

## Calling Command-Line Tools

In AppleScript, the `do shell script` command is used to execute command-line tools. This command is implemented by the Standard Additions scripting addition included with OS X.

> **Note**
>
>
> The Terminal app in `/Applications/Utilities/` is scriptable and provides another way to execute command-line tools from scripts.

<a id="//apple_ref/doc/uid/TP40016239-CH43-SW7"></a>

### Executing Commands

The direct parameter of the `do shell script` command is a string containing the shell code you want to execute, as demonstrated in Listing 39-1, which simply lists a directory.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=do%20shell%20script%20%22ls%20%2FApplications%2F%22%0A%28*%0A--%3E%20Result%3A%20%0A%22App%20Store.app%0AAutomator.app%0ACalculator.app%0ACalendar.app%0A...%22%0A*%29)

<a id="//apple_ref/doc/uid/TP40016239-CH43-SW3"></a>
**Listing 39-1**AppleScript: Executing a simple shell command that lists the contents of a directory

1. `do shell script "ls /Applications/"`
2. `(*`
3. `--&gt; Result:`
4. `"App Store.app`
5. `Automator.app`
6. `Calculator.app`
7. `Calendar.app`
8. `..."`
9. `*)`

Since the direct parameter of `do shell script` is a string, you can concatenate it with other strings at run time. Listing 39-2, for example, concatenates a shell command to a previously defined parameter value.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20theHostName%20to%20%22www.apple.com%22%0Ado%20shell%20script%20%22ping%20-c1%20%22%20%26%20theHostName)

<a id="//apple_ref/doc/uid/TP40016239-CH43-SW4"></a>
**Listing 39-2**AppleScript: Concatenating a command with a value

1. `set theHostName to "www.apple.com"`
2. `do shell script "ping -c1 " & theHostName`

<a id="//apple_ref/doc/uid/TP40016239-CH43-SW8"></a>

### Quoting Strings

The shell uses space characters to separate parameters and gives special meaning to certain punctuation marks, such as `$`, `(`, `)`, and `*`. To ensure that strings are treated as expected—for example, spaces aren’t seen as delimiters—it’s best to wrap strings in quotes. This process is known as *quoting*. If your string contains quotes, they must also be *escaped* (preceded by a `/` character) so they are interpreted as part of the string. Listing 39-3 shows an example of an error occurring as a result of a parameter that contains a space.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20thePath%20to%20%22%2FLibrary%2FApplication%20Support%2F%22%0Ado%20shell%20script%20%22ls%20%22%20%26%20thePath%0A--%3E%20Result%3A%20error%20%22ls%3A%20%2FLibrary%2FApplication%3A%20No%20such%20file%20or%20directory%5Crls%3A%20Support%3A%20No%20such%20file%20or%20directory%22%20number%201)

<a id="//apple_ref/doc/uid/TP40016239-CH43-SW5"></a>
**Listing 39-3**AppleScript: An error resulting from a string containing a space

1. `set thePath to "/Library/Application Support/"`
2. `do shell script "ls " & thePath`
3. `--&gt; Result: error "ls: /Library/Application: No such file or directory\\rls: Support: No such file or directory" number 1`

The easiest way to quote a string is to use the `quoted form` property of the text class, as demonstrated in Listing 39-4. This property returns the string in a form that’s safe from further interpretation by the shell, regardless of its contents.

**APPLESCRIPT**

[Open in Script Editor](https://developer.apple.com/library/archive/mac-automation-scripting-guide/applescript:/com.apple.scripteditor?action=new&script=set%20thePath%20to%20quoted%20form%20of%20%22%2FLibrary%2FApplication%20Support%2F%22%0A--%3E%20Result%3A%20%22%27%2FLibrary%2FApplication%20Support%2F%27%22%0Ado%20shell%20script%20%22ls%20%22%20%26%20thePath%0A%28*%0A--%3E%20Result%3A%0A%22App%20Store%0AApple%0A...%0A%22%0A*%29)

<a id="//apple_ref/doc/uid/TP40016239-CH43-SW6"></a>
**Listing 39-4**AppleScript: Quoting a string to prevent errors

1. `set thePath to quoted form of "/Library/Application Support/"`
2. `--&gt; Result: "'/Library/Application Support/'"`
3. `do shell script "ls " & thePath`
4. `(*`
5. `--&gt; Result:`
6. `"App Store`
7. `Apple`
8. `...`
9. `"`
10. `*)`

<a id="//apple_ref/doc/uid/TP40016239-CH43-SW9"></a>

### More Information

For more information about the `do shell script` command, see [Commands Reference](https://developer.apple.com/library/archive/../../AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_cmds.html#//apple_ref/doc/uid/TP40000983-CH216) in *[AppleScript Language Guide](https://developer.apple.com/library/archive/../../AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html#//apple_ref/doc/uid/TP40000983)* and [Technical Note TN2065](http://developer.apple.com/technotes/tn2002/tn2065.html).
