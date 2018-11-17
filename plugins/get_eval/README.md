# Get Eval Function
This plugin provides a new scripting function `$get_eval()` that allows the user to evaluate specified python code within Picard and return the results as a string for use within scripts.

This allows access to all metadata fields and the ability to use native python processing commands directly from a script without having to create and load additional plugins. 


## Usage
The following are examples of some of the functionality provided by this plugin.

### Example 1
Breaks the `parser.context` metadata contents into 80-character "chunks" and creates tags named "Metadata 001", "Metadata 002", "Metadata 003"... containing the data chunks.

    $get_eval(exec\('junk1 = "\%s" \% parser.context\\nfor i in range\(0\, \(len\(junk1\) // 80 \) + 1\, 1\):\\n    parser.context["Metadata {0:03d}".format\(i\)] =  \(junk1\)[i*80:\(i+1\)*80]\\n'\))

### Example 2
Lists composers for the track individually in tags "Composer 01", "Composer 02" and so on.

    $get_eval(exec\('for i\, j in enumerate\(parser.context["composer"].split\("; "\)\): parser.context["Composer {0:02d}".format\(i\)] = j'\))

### Example 3
Set the tag variable %number_of_composers% to the number of composers identified for the track.

    $set(number_of_composers,$get_eval(len\(parser.context["composer"].split\("; "\)\)))


## Technical Notes
Access to the the metadata is provided through the `parser.context` object. All `$some_function()` functions and `%some_variable%` tag variables are expanded prior to evaluating the expression. 

You can even execute code by calling the `exec()` funtion within the `$get_eval()` call. 

