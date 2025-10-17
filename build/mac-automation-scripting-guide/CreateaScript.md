<a id="//apple_ref/doc/uid/TP40016239-CH12"></a><a id="//apple_ref/doc/uid/TP40016239-CH12-SW1"></a>

## Creating a Script

Generally, most scripts are written in Script Editor documents. Scripts can also be written in Xcode, but this is typically for scripts that require advanced user interfaces.

<a id="//apple_ref/doc/uid/TP40016239-CH12-SW4"></a>

**To write a script in Script Editor**

1. Launch Script Editor in `/Applications/Utilities/`.
2. Press Command-N or select File &gt; New.
3. If the script isn’t configured for the correct language, choose the language in the navigation bar.

   <a id="//apple_ref/doc/uid/TP40016239-CH12-SW3"></a>

   ![image: ../Art/script-editor_langage_selector_2x.png](Art/script-editor_langage_selector_2x.png)

   <a id="//apple_ref/doc/uid/TP40016239-CH12-DontLinkElementID_1"></a>


   Tip

   If you always use the same language, set it as the default language in the General pane of Script Editor preferences. See [General Preferences](ConfigureScriptingPreferences.html#//apple_ref/doc/uid/TP40016239-CH70-SW10).
4. Write your script code in the editing area. Newly written code is uncompiled and formatted as new text.

   <a id="//apple_ref/doc/uid/TP40016239-CH12-SW5"></a>

   ![image: ../Art/scripteditor_uncompiledscript_2x.png](Art/scripteditor_uncompiledscript_2x.png)
5. Click the Compile button (![image: ../Art/icon_compilescript_2x.png](Art/icon_compilescript_2x.png)) to compile the script and check for syntax errors.

   If a syntax error occurs, an alert is displayed.

   <a id="//apple_ref/doc/uid/TP40016239-CH12-SW7"></a>

   ![image: ../Art/scripteditor_syntaxerror_2x.png](Art/scripteditor_syntaxerror_2x.png)

   If the script compiles, code formatting is applied at this time.

   <a id="//apple_ref/doc/uid/TP40016239-CH12-SW6"></a>

   ![image: ../Art/scripteditor_compiledscript_2x.png](Art/scripteditor_compiledscript_2x.png)

<a id="//apple_ref/doc/uid/TP40016239-CH12-DontLinkElementID_2"></a>


Tip

You can change the formatting attributes, such as font and color, of uncompiled and compiled text in the Formatting pane of Script Editor preferences. See [Formatting Preferences](ConfigureScriptingPreferences.html#//apple_ref/doc/uid/TP40016239-CH70-SW11).

<a id="//apple_ref/doc/uid/TP40016239-CH12-SW2"></a>

### Using an AppleScript Template

Script Editor includes a number of built-in templates for creating common types of AppleScripts, including droplets, Mail rule scripts, and Messages handler scripts.

> **Note**
>
>
> Script Editor does not include JavaScript templates at this time.

<a id="//apple_ref/doc/uid/TP40016239-CH12-SW10"></a>

**To create a template-based script**

1. Launch Script Editor in `/Applications/Utilities/`.
2. Choose File &gt; New from Template.

   <a id="//apple_ref/doc/uid/TP40016239-CH12-SW8"></a>

   ![image: ../Art/scripteditor_newtemplate_menu_2x.png](Art/scripteditor_newtemplate_menu_2x.png)
3. Select a script template.

   A new Script Editor document window opens containing prewritten code and preconfigured settings. The following screenshot shows an example of a script created using a template.

   <a id="//apple_ref/doc/uid/TP40016239-CH12-SW9"></a>

   ![image: ../Art/scripteditor_asoc_template_2x.png](Art/scripteditor_asoc_template_2x.png)
4. Customize the script.
