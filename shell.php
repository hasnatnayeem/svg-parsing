<?php
    $file_name = "test.svg";
    $command = "python svg_to_json.py " . $file_name;
    $output = shell_exec($command);
    echo "<pre>$output</pre>";
?>
