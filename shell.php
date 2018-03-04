<?php
    $directory = "files/";
    $file_name = $directory.$_GET['f'];

    $command = "python svg_to_json.py " . $file_name;
    $output = shell_exec($command);
    echo "<pre>$output</pre>";
?>
